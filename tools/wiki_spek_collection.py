"""Compose a private multi-Kristal wiki draft with Spek's Arketype templates.

No Git write, push, C1/C2 issuance or SemantiK language generation occurs here.
A caller supplies *already realized* Spek article/realizations pairs from SemantiK,
one per C3-indexed Kristal. All C3 entries must have a corresponding bundle.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

from c3_collection import validate_index

SHA=re.compile(r'[0-9a-f]{40}\Z')
REPO=re.compile(r'[a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+\Z')
SLUG=re.compile(r'[a-z0-9][a-z0-9.-]*\Z')
PRIVATE_PROVENANCE=re.compile(r'(?i)(?:source_assertion_refs|request_sha256|source_sha256|spek\.private-editorial-handoff|PRIVATE_UNQUALIFIED_NOT_PUBLISHABLE|urn:kristal:assertion:|sha256:[a-f0-9]{64})')

class WikiSpekError(ValueError):pass

def _sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()

def _safe_title(row:dict)->str:
    name=str(row.get('title') or row['slug'])
    # Only a safe Markdown label; does not infer facts or article prose.
    return re.sub(r'[\x00-\x1f<>\\\[\]()*_`!#|]',' ',name).strip()[:140]

def generate(*,collection:Path,packages:Path,spek_root:Path,output:Path,
             repository:str,revision:str,language:str='fr',write:bool=False,
             renderer=None, validator=validate_index)->dict:
    """Private candidate with all C3 rows, no implicit omission."""
    if not REPO.fullmatch(repository) or not SHA.fullmatch(revision):
        raise WikiSpekError('Exact GitHub owner/repo and published 40-char SHA required')
    if language not in {'fr','en','it'}:raise WikiSpekError('Unsupported language')
    collection=Path(collection).resolve(strict=True)
    packages=Path(packages).resolve(strict=True)
    spek_root=Path(spek_root).resolve(strict=True)
    output=Path(output).expanduser().resolve()
    if not packages.is_dir() or not (spek_root/'spek'/'wiki.py').is_file():
        raise WikiSpekError('Missing private SemantiK/Spek bundles or Spek checkout')
    if packages.is_relative_to(collection) or collection.is_relative_to(packages):
        raise WikiSpekError('Private input packages cannot be inside public checkout')
    if output.exists() or not output.parent.is_dir():
        raise WikiSpekError('Output must be a new private directory')
    if any((p/'.git').exists() for p in output.parents):
        raise WikiSpekError('Wiki private output cannot be inside a Git checkout')
    index=validator(collection)
    rows=index.get('kristals') or []
    if not rows:raise WikiSpekError('C3 collection is empty')
    slugs=[r['slug'] for r in rows]
    if len(slugs)!=len(set(slugs)) or not all(SLUG.fullmatch(s) for s in slugs):
        raise WikiSpekError('Invalid C3 slugs')
    # Fresh temp directory, never a tracked repository or a public host.
    with tempfile.TemporaryDirectory(prefix='spek-wiki-',dir=str(output.parent)) as temp:
        tmp=Path(temp)
        pages={};bindings={}
        for row in rows:
            slug=row['slug'];bundle=packages/slug
            if bundle.is_symlink() or not bundle.is_dir() or not bundle.resolve().is_relative_to(packages):
                raise WikiSpekError('Missing safe private Spek bundle: '+slug)
            article=bundle/'article.json';realizations=bundle/'realizations.json';binding=bundle/'archetype.json'
            for file in (article,realizations,binding):
                if file.is_symlink() or not file.is_file():
                    raise WikiSpekError('Missing safe Spek input '+str(file))
            profile=json.loads(binding.read_text(encoding='utf8'))
            if profile.get('format')!='spek.wiki-archetype-binding/1.0':
                raise WikiSpekError('Missing typed archetype binding for '+slug)
            archetype=profile.get('archetype')
            if not isinstance(archetype,str) or not SLUG.fullmatch(archetype):
                raise WikiSpekError('Invalid declared archetype '+slug)
            state=collection/'kristals'/slug/'state'/'state-snapshot.json'
            if state.is_symlink() or not state.is_file():
                raise WikiSpekError('Missing public state snapshot '+slug)
            out=tmp/slug
            if renderer is None:
                cmd=[sys.executable,'-m','spek','build-wiki','--source',str(article),
                  '--realizations',str(realizations),'--archetype',archetype,'--slug',slug,
                  '--language',language,'--state-snapshot',str(state),'--out',str(out)]
                proc=subprocess.run(cmd,cwd=str(spek_root),capture_output=True,
                         text=True,encoding='utf8',errors='replace',timeout=180,check=False)
                if proc.returncode:
                    raise WikiSpekError('Spek refused '+slug+': '+(proc.stderr or proc.stdout)[-750:])
            else:
                renderer(slug,out)
            page=out/('Kristal-'+slug+'.md')
            if not page.is_file() or not (out/'manifest.json').is_file():
                raise WikiSpekError('Incomplete Spek result '+slug)
            # Trust boundary: a real renderer must create this as private, never 'published'.
            import_context=json.loads((out/'manifest.json').read_text(encoding='utf8'))
            if import_context.get('format')!='spek.wiki-draft/1.0' or import_context.get('archetype')!=archetype or import_context.get('demonstration'):
                raise WikiSpekError('Unqualified or mismatched Spek output '+slug)
            page_text=page.read_text(encoding='utf8')
            if PRIVATE_PROVENANCE.search(page_text):
                raise WikiSpekError('Private provenance in proposed Wiki page '+slug)
            pages[page.name]=page_text
            bindings[slug]={'archetype':archetype,'spek_draft_sha256':_sha(page),
                'article_sha256':_sha(article),'realizations_sha256':_sha(realizations)}
        if len(pages)!=len(rows):raise WikiSpekError('Missing Wiki page: C3 coverage incomplete')
        header='Catalogue public Kristal' if language=='fr' else 'Kristal catalog'
        note='Brouillon privé — aucune publication ni autorisation C1/C2 effectuée' if language=='fr' else 'Private draft — no publication or C1/C2 authorization performed'
        home=[f'# {header}','','**'+note+'**','',f'Révision de référence : `{revision}`','', '## Kristals','']
        sidebar=['# Navigation','','[Accueil](Home)','']
        for row in rows:
            slug=row['slug'];title=_safe_title(row);name='Kristal-'+slug
            home.append(f'- [{title}]({name})');sidebar.append(f'- [{title}]({name})')
        pages['Home.md']='\n'.join(home+['']);pages['_Sidebar.md']='\n'.join(sidebar+[''])
        hashes={k:hashlib.sha256(v.encode('utf8')).hexdigest() for k,v in sorted(pages.items())}
        receipt={'format':'spek.wiki-collection-candidate/1.0','status':'PRIVATE_NOT_PUBLISHED',
                 'c1_c2':'NOT_VERIFIED_HERE','semantik_runtime_authority':'EXTERNAL',
                 'repository':repository,'revision':revision,'language':language,
                 'kristals':bindings,'files':hashes}
        if write:
            stage=tmp/'final';stage.mkdir()
            for name,content in pages.items():(stage/name).write_text(content,encoding='utf8')
            (stage/'manifest.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf8')
            # Verify locally before any file leaves private staging.
            for name,digest in hashes.items():
                if _sha(stage/name)!=digest:raise WikiSpekError('Generated page digest mismatch')
            os.rename(stage,output)
    return {'status':'PRIVATE_WIKI_CANDIDATE' if write else 'DRY_RUN',
            'deployment':'NOT_PERFORMED','revision':revision,
            'repository':repository,'pages':sorted(pages), 'archetypes':bindings,
            'output':str(output) if write else None}

def main(argv=None)->int:
    p=argparse.ArgumentParser(description='Spek-composed private Wiki for a validated C3 collection; never pushes')
    for key in ('collection','packages','spek-root','output','repository','revision'):
        p.add_argument('--'+key,required=True)
    p.add_argument('--language',default='fr',choices=('fr','en','it'))
    p.add_argument('--write',action='store_true')
    a=p.parse_args(argv)
    try:
        result=generate(collection=Path(a.collection),packages=Path(a.packages),
            spek_root=Path(a.spek_root),output=Path(a.output),
            repository=a.repository,revision=a.revision,language=a.language,write=a.write)
        print(json.dumps(result,ensure_ascii=False,indent=2));return 0
    except (WikiSpekError,OSError,ValueError,KeyError,TypeError,subprocess.TimeoutExpired) as exc:
        print('BLOCKED: '+str(exc),file=sys.stderr);return 2

if __name__=='__main__':raise SystemExit(main())
