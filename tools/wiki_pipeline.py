"""Fail-closed orchestration: curated Kristal v6 assertions → SA → Spek Wiki.

Only consumes explicit, reviewed editorial plans; it never chooses claims, invents
communication requests, issues C1/C2 certificates, or performs a Git/network push.
The resulting Wiki is always a PRIVATE candidate.
"""
from __future__ import annotations
import argparse
from collections import Counter
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Callable

from c3_collection import validate_index
from wiki_semantik import _check_result
from wiki_spek_collection import generate as compose_collection

SLUG=re.compile(r'[a-z0-9](?:[a-z0-9-]{0,75}[a-z0-9])?\Z')
SAFE_ID=re.compile(r'[A-Za-z][A-Za-z0-9_.:-]{0,120}\Z')
REV=re.compile(r'[a-f0-9]{40}\Z')
REPO=re.compile(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z')
PLAN_FORMAT='kristal.wiki-editorial-plan/1.0'
SA_FORMAT='semantik.kristal-v6.communication-projection/1.0'
BINDING_FORMAT='spek.wiki-archetype-binding/1.0'

class WikiPipelineError(ValueError):pass

def _json(path:Path)->dict:
    if not path.is_file() or path.is_symlink():raise WikiPipelineError('Required regular file missing: '+str(path))
    try:r=json.loads(path.read_text(encoding='utf-8'))
    except (OSError,ValueError) as exc:raise WikiPipelineError('Invalid JSON: '+str(path)) from exc
    if not isinstance(r,dict):raise WikiPipelineError('JSON object required: '+str(path))
    return r

def _safe_file(base:Path,name:str)->Path:
    if not isinstance(name,str) or not name.endswith('.json') or '\\' in name or '/' in name or name.startswith('.'):
        raise WikiPipelineError('Invalid relative JSON file name')
    path=base/name
    if path.is_symlink() or not path.resolve().is_relative_to(base.resolve()):
        raise WikiPipelineError('Unsafe private input path')
    return path

def _workspace(root:Path,slug:str)->Path:
    """Map lowercase publication slug to Kristal-* workspace without guessing."""
    matches=[]
    for folder in root.iterdir():
        if folder.is_dir() and not folder.is_symlink():
            workspace=folder/'kristal.workspace.json'
            if workspace.is_file() and not workspace.is_symlink():
                if _json(workspace).get('slug')==slug:matches.append(folder)
    if len(matches)!=1:raise WikiPipelineError('Expected one local workspace for '+slug)
    return matches[0]

def _source(workspace:Path, slug:str)->dict:
    """Use portable v6 for ALL Kristals, including Accounting (no v11 graph)."""
    if any(p.is_symlink() for p in (workspace,workspace/'.kristal',workspace/'.kristal/v8')):
        raise WikiPipelineError('Local source symlink is forbidden')
    raw=_json(workspace/'.kristal/v8/portable-state.kristal-state.json')
    if raw.get('schema_version')!='6.0' or raw.get('artifact_type')!='kristal_state':
        raise WikiPipelineError('No portable Kristal v6 state for '+slug)
    assertions=raw.get('assertions')
    if not isinstance(assertions,list) or not assertions:raise WikiPipelineError('Empty source assertions: '+slug)
    ids=[x.get('assertion_id') for x in assertions if isinstance(x,dict)]
    if not all(isinstance(v,str) and v for v in ids):
        raise WikiPipelineError('Invalid canonical assertion identities in '+slug)
    freq=Counter(ids)
    status={v.get('assertion_id'):v.get('assertion_status') for v in assertions if isinstance(v,dict)}
    return {'data':raw,'ids':set(ids),'ambiguous':{k for k,v in freq.items() if v>1},
            'statuses':status}

def _used_keys(article:dict)->set[str]:
    try:
        all_keys={article['article'][k] for k in ('title_key','subtitle_key','abstract_key')}
        all_keys.update(s['heading_key'] for s in article['sections'])
        for unit in [*article['units'],*article['evidence']]: all_keys.add(unit['realization_key'])
    except (KeyError,TypeError) as exc:raise WikiPipelineError('Incomplete editorial source') from exc
    if not all(SAFE_ID.fullmatch(x or '') for x in all_keys):
        raise WikiPipelineError('Invalid editorial realization key')
    return all_keys

def _text(result:dict)->str:
    """A Spek slot is one bounded communication, not a complete article.

    Reject multi-block outputs so no clause/list hierarchy can be silently lost
    by Spek's single-string realization input contract.
    """
    blocks=result['blocks']
    if len(blocks)!=1 or blocks[0].get('kind') not in ('utterance','notice','paragraph','heading','question'):
        raise WikiPipelineError('A Spek slot requires exactly one plain language block')
    value=blocks[0].get('text')
    if not isinstance(value,str) or not value.strip() or len(value)>5000:
        raise WikiPipelineError('Unusable SemantiK realization text')
    return value

def _render_real(*,projection:dict, path:Path, semantik_root:Path, runtime_root:Path,
                 language:str, locale:str, profile:str, worker:Path, timeout:int=120)->dict:
    # The worker calls the real SDK + KristalV6Acl, no mock or grammar fallback.
    env=os.environ.copy()
    env['PYTHONPATH']=str(semantik_root/'src')+os.pathsep+env.get('PYTHONPATH','')
    command=[sys.executable,str(worker),str(path),str(runtime_root),language,locale,profile]
    try:
        p=subprocess.run(command,cwd=str(semantik_root),env=env,capture_output=True,
                         text=True,encoding='utf-8',errors='replace',timeout=timeout,check=False)
    except (OSError,subprocess.TimeoutExpired) as exc:
        raise WikiPipelineError('SemantiK process unavailable or timed out') from exc
    if p.returncode:raise WikiPipelineError('SemantiK refused the request: '+(p.stderr or p.stdout)[-650:])
    try:return json.loads(p.stdout)
    except ValueError as exc:raise WikiPipelineError('SemantiK did not return JSON') from exc

def _canonical_v9(workspace:Path,row:dict)->dict:
    """Source state can be active (state/) or build materialization (build/v9)."""
    matches=[]
    for rel in ('state/state-snapshot.json','build/v9/state-snapshot.json',
                '.kristal/v9/state-snapshot.json'):
        p=workspace/rel
        if p.is_file() and not p.is_symlink():
            snap=_json(p)
            if (snap.get('state_ref')==row['state_ref'] and
                snap.get('logical_commitment',{}).get('digest')==row['state_logical_commitment']['digest']):
                matches.append(snap)
    if not matches:raise WikiPipelineError('No local v9 state pinned to published C3 digest for '+row['slug'])
    return matches[0]

def _plan_for_row(*,row:dict,locals_root:Path,plan_root:Path,language:str,revision:str)->tuple[dict,dict,dict,dict]:
    slug=row['slug'];folder=plan_root/slug
    if folder.is_symlink() or not folder.is_dir() or not folder.resolve().is_relative_to(plan_root):
        raise WikiPipelineError('Missing private editorial plan for '+slug)
    plan=_json(folder/'plan.json')
    if plan.get('format')!=PLAN_FORMAT or plan.get('slug')!=slug or plan.get('language')!=language:
        raise WikiPipelineError('Wrong plan format/slug/language for '+slug)
    arch=plan.get('archetype')
    if not isinstance(arch,str) or not SLUG.fullmatch(arch):raise WikiPipelineError('Missing explicit Arketype profile for '+slug)
    workspace=_workspace(locals_root,slug)
    local=_source(workspace,slug)
    original=local['data']
    metadata=plan.get('source')
    if not isinstance(metadata,dict):raise WikiPipelineError('Missing publication review metadata in '+slug)
    if (metadata.get('origin')!='kristal_v9' or
        metadata.get('state_ref')!=row['state_ref'] or
        metadata.get('state_commitment')!=row['state_logical_commitment']['digest'] or
        metadata.get('scientific_review')!='approved' or
        metadata.get('disclosure')!='approved' or
        metadata.get('language_review',{}).get(language)!='approved'):
        raise WikiPipelineError('Source pin or independent editorial approvals incomplete for '+slug)
    src_state=_canonical_v9(workspace,row)
    # Compare original canonical v9 snapshot to published C3 v9 snapshot on critical fields.
    if (src_state.get('state_ref')!=row['state_ref'] or
        src_state.get('logical_commitment',{}).get('digest')!=row['state_logical_commitment']['digest']):
        raise WikiPipelineError('Local canonical v9 snapshot diverges from the C3 publication for '+slug)
    members={m.get('artifact_id') for m in src_state.get('members',[]) if isinstance(m,dict)}
    if not isinstance(metadata.get('artifact_refs'),list) or not metadata['artifact_refs'] or not set(metadata['artifact_refs'])<=members:
        raise WikiPipelineError('No valid pinned v9 source artifact_refs in '+slug)
    content=plan.get('content')
    if not isinstance(content,dict):raise WikiPipelineError('No explicit editorial Spek content for '+slug)
    article={k:content.get(k) for k in ('article','units','evidence','sections')}
    article.update({'format':'kristal.layout-article-source/0.1','source':metadata})
    keys=_used_keys(article)
    if not isinstance(plan.get('locale'),str) or not re.fullmatch(r'[a-z]{2,3}(?:-[A-Za-z]{2,4})?',plan['locale']):
        raise WikiPipelineError('Explicit BCP47 locale required: '+slug)
    if not isinstance(plan.get('capability_profile'),str) or not plan['capability_profile']:
        raise WikiPipelineError('Explicit SemantiK capability profile required: '+slug)
    if not isinstance(plan.get('runtime_set_id'),str) or not plan['runtime_set_id']:
        raise WikiPipelineError('Pinned SemantiK RuntimeSet required: '+slug)
    refs=plan.get('projections')
    if not isinstance(refs,dict) or set(refs)!=keys:
        raise WikiPipelineError('Every Spek text key must have exactly one explicit SemantiK projection: '+slug)
    if len(refs)>500:raise WikiPipelineError('Too many Wiki slots; split the article')
    for key,filename in refs.items():
        p=_safe_file(folder,filename);payload=_json(p)
        if payload.get('contract')!=SA_FORMAT or payload.get('kristal_standard')!='6.0.0':
            raise WikiPipelineError('Nonportable SemantiK v6 projection at '+key)
        state=payload.get('state_ref')
        if (not isinstance(state,dict) or state.get('state_id')!=original.get('state_id') or
            state.get('artifact_type')!='kristal_state' or str(state.get('schema_version'))!='6.0'):
            raise WikiPipelineError('SA projection not pinned to the local portable v6 state: '+key)
        if state.get('content_hash')!=original.get('content_hash'):
            raise WikiPipelineError('SA projection v6 content hash mismatch: '+key)
        chosen=payload.get('selected_assertions')
        ids={x.get('assertion_id') for x in chosen if isinstance(x,dict)} if isinstance(chosen,list) else set()
        if not chosen or len(ids)!=len(chosen) or not ids<=local['ids'] or ids&local['ambiguous']:
            raise WikiPipelineError('SA selected assertions missing or ambiguous in the original Kristal: '+key)
        if any(local['statuses'].get(x) not in ('reviewed','validated') for x in ids):
            raise WikiPipelineError('SA selected assertion lacks reviewed/validated status: '+key)
        request=payload.get('communication_request')
        if not isinstance(request,dict) or not request.get('obligations'):
            raise WikiPipelineError('Missing explicit SA communication obligations: '+key)
        if request.get('capability_profile')!=plan.get('capability_profile'):
            raise WikiPipelineError('SA capability profile changed: '+key)
        if request.get('runtime_selector',{}).get('runtime_set_id')!=plan.get('runtime_set_id'):
            raise WikiPipelineError('SA runtime changed: '+key)
        if request.get('context',{}).get('target_language')!=language:
            raise WikiPipelineError('SA language changed: '+key)
    return plan,article,refs,original

def run(*,collection:Path,locals_root:Path,plans:Path,spek_root:Path,
        semantik_root:Path,runtime_root:Path,output:Path,repository:str,revision:str,
        language:str='fr',write:bool=False, renderer:Callable|None=None,
        spek_builder:Callable|None=None,collection_builder:Callable|None=None,
        validator=validate_index)->dict:
    if not REPO.fullmatch(repository) or not REV.fullmatch(revision):
        raise WikiPipelineError('Exact GitHub repository and 40-character commit revision required')
    if language not in ('fr','en','it'):raise WikiPipelineError('Unsupported language')
    collection=Path(collection).resolve(strict=True)
    locals_root=Path(locals_root).resolve(strict=True)
    plans=Path(plans).resolve(strict=True)
    spek_root=Path(spek_root).resolve(strict=True)
    semantik_root=Path(semantik_root).resolve(strict=True)
    runtime_root=Path(runtime_root).resolve(strict=True)
    output=Path(output).expanduser().resolve()
    for folder in (locals_root,plans,spek_root,semantik_root,runtime_root):
        if not folder.is_dir() or folder.is_symlink() or folder.is_relative_to(collection) or collection.is_relative_to(folder):
            raise WikiPipelineError('All source/tool inputs must be private and outside the published checkout')
    if not (spek_root/'spek/wiki.py').is_file():raise WikiPipelineError('Spek Wiki templates not installed')
    if not (semantik_root/'src/semantik_architect/adapters/ecosystem/kristal_v6.py').is_file():
        raise WikiPipelineError('SemantiK v6 adapter not installed')
    if not (runtime_root/'activation.json').is_file():raise WikiPipelineError('SemantiK RuntimeSet not configured')
    if output.exists() or not output.parent.is_dir() or any((x/'.git').exists() for x in output.parents):
        raise WikiPipelineError('Output must be a NEW private directory outside Git checkouts')
    if any(output.is_relative_to(x) or x.is_relative_to(output) for x in (collection,locals_root,plans,spek_root,semantik_root,runtime_root)):
        raise WikiPipelineError('Output must not overlap inputs')
    index=validator(collection)
    rows=index.get('kristals') or []
    if not rows or len({r['slug'] for r in rows})!=len(rows):
        raise WikiPipelineError('Empty or duplicated C3 index')
    configs={}
    for row in rows:
        slug=row['slug']
        if not SLUG.fullmatch(slug):raise WikiPipelineError('Unsafe C3 slug')
        plan,article,refs,src=_plan_for_row(row=row,locals_root=locals_root,
             plan_root=plans,language=language,revision=revision)
        configs[slug]=(plan,article,refs,src)
    if not write:
        return {'status':'READY_FOR_REAL_SEMANTIK_RENDER','write':False,
                'publishing':'NOT_PERFORMED','kristals':sorted(configs),
                'communication_requests':sum(len(v[2]) for v in configs.values()),
                'note':'Only input/pins/approvals checked. Real RuntimeSet render requires --write.'}
    worker=collection/'tools/wiki_semantik_worker.py'
    if not worker.is_file():raise WikiPipelineError('SemantiK worker not installed in kristal-public')
    with tempfile.TemporaryDirectory(prefix='kristal-spek-stage-',dir=str(output.parent)) as td:
        stage=Path(td)
        bundles=stage/'bundles';bundles.mkdir()
        render_root=stage/'rendered';render_root.mkdir()
        receipts={}
        for row in rows:
            slug=row['slug'];plan,article,refs,original=configs[slug]
            dest=bundles/slug;dest.mkdir()
            entries={}
            for key,path in sorted(refs.items()):
                projection=_json(_safe_file(plans/slug,path))
                env={'projection':projection}
                inp=dest/('input-'+sha256(key.encode()).hexdigest()[:24]+'.json')
                inp.write_text(json.dumps(env,ensure_ascii=False,sort_keys=True),encoding='utf-8')
                lang=language;locale=plan['locale'];profile=plan['capability_profile']
                if renderer is None:
                    result=_render_real(projection=projection,path=inp,semantik_root=semantik_root,
                           runtime_root=runtime_root,language=lang,locale=locale,
                           profile=profile,worker=worker)
                else:result=renderer(slug,key,projection)
                _check_result(projection,language,profile,result)
                entries[key]={lang:{'text':_text(result),'status':'qualified',
                             'provider':'semantik_architect','channel':'semantik_architect',
                             'request_id':projection['communication_request']['request_id'],
                             'runtime_set_id':result['runtime']['runtime_set_id']}}
                inp.unlink() # The private input requests remain under plans only.
            (dest/'article.json').write_text(json.dumps(article,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
            (dest/'realizations.json').write_text(json.dumps({'format':'kristal.layout-realizations/0.1','entries':entries},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
            (dest/'archetype.json').write_text(json.dumps({'format':BINDING_FORMAT,'archetype':plan['archetype']})+'\n',encoding='utf-8')
            snap=collection/'kristals'/slug/'state/state-snapshot.json'
            if spek_builder is None:
                cmd=[sys.executable,'-m','spek','build-wiki','--source',str(dest/'article.json'),
                    '--realizations',str(dest/'realizations.json'),'--archetype',plan['archetype'],
                    '--slug',slug,'--language',language,'--state-snapshot',str(snap),
                    '--out',str(render_root/slug)]
                proc=subprocess.run(cmd,cwd=str(spek_root),capture_output=True,text=True,
                     encoding='utf-8',errors='replace',timeout=120)
                if proc.returncode:raise WikiPipelineError('Spek rejected '+slug+': '+(proc.stderr or proc.stdout)[-900:])
            else:spek_builder(slug,dest,render_root/slug,article,entries)
            receipts[slug]={'archetype':plan['archetype'],'keys':len(entries)}
        wiki_out=stage/'wiki'
        if collection_builder is None:
            compose_collection(collection=collection,packages=bundles,spek_root=spek_root,
             output=wiki_out,repository=repository,revision=revision,language=language,write=True,
             validator=validator)
        else:collection_builder(stage,rows)
        if not (wiki_out/'Home.md').is_file() or not (wiki_out/'manifest.json').is_file():
            raise WikiPipelineError('Wiki composition is incomplete')
        receipt={'format':'kristal.spek-semantic-pipeline/1.0','status':'PRIVATE_CANDIDATE',
                 'repository':repository,'revision':revision,'language':language,
                 'kristals':receipts,'publication':'NOT_PERFORMED'}
        (stage/'pipeline-receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        # Atomic publication ONLY to a new private directory; never to Git or a web root.
        os.rename(stage,output)
    return {'status':'PRIVATE_WIKI_READY','publishing':'NOT_PERFORMED',
            'kristals':sorted(configs),'output':str(output),
            'wiki_home':str(output/'wiki/Home.md')}

def main(argv=None)->int:
    p=argparse.ArgumentParser(description='Curated Kristal→real SemantiK→Spek→private Wiki')
    for name in ('collection','locals-root','plans','spek-root','semantik-root','runtime-root','output','repository','revision'):
        p.add_argument('--'+name,required=True)
    p.add_argument('--language',choices=('fr','en','it'),default='fr')
    p.add_argument('--write',action='store_true')
    a=p.parse_args(argv)
    kw={k.replace('-','_'):Path(getattr(a,k.replace('-','_'))) for k in
        ('collection','locals-root','plans','spek-root','semantik-root','runtime-root','output')}
    try:
        r=run(**kw,repository=a.repository,revision=a.revision,language=a.language,write=a.write)
        print(json.dumps(r,ensure_ascii=False,indent=2));return 0
    except (WikiPipelineError,OSError,KeyError,TypeError,ValueError,subprocess.TimeoutExpired) as exc:
        print('BLOCKED: '+str(exc),file=sys.stderr);return 2

if __name__=='__main__':raise SystemExit(main())
