"""Create *private* editorial-plan skeletons; never select/approve assertions."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
from wiki_pipeline import _source, _workspace, _canonical_v9, WikiPipelineError
from c3_collection import validate_index


def scaffold(*,collection:Path,locals_root:Path,output:Path,language:str='fr',write:bool=False,
             validator=validate_index):
    collection=Path(collection).resolve(strict=True)
    locals_root=Path(locals_root).resolve(strict=True)
    output=Path(output).expanduser().resolve()
    if output.exists() or not output.parent.is_dir() or any((p/'.git').exists() for p in output.parents):
        raise WikiPipelineError('Use a NEW private output directory outside Git')
    if output.is_relative_to(collection) or output.is_relative_to(locals_root):
        raise WikiPipelineError('Source and output must be separate')
    if language not in ('fr','en','it'):raise WikiPipelineError('Language not supported')
    rows=validator(collection)['kristals']
    if not rows:raise WikiPipelineError('No C3 index entries')
    summary={}
    with tempfile.TemporaryDirectory(prefix='wiki-plans-stage-',dir=str(output.parent)) as td:
        stage=Path(td)
        for row in rows:
            slug=row['slug']; ws=_workspace(locals_root,slug); portable=_source(ws,slug); s=portable['data']
            snap=_canonical_v9(ws,row)
            if snap.get('state_ref')!=row['state_ref'] or snap.get('logical_commitment',{}).get('digest')!=row['state_logical_commitment']['digest']:
                raise WikiPipelineError('Local/C3 snapshot divergence: '+slug)
            folder=stage/slug;folder.mkdir()
            source={'origin':'kristal_v9','state_ref':row['state_ref'],
              'state_commitment':row['state_logical_commitment']['digest'],
              'artifact_refs':[], # Operator must explicitly identify reviewed v9 members.
              'scientific_review':'pending', 'disclosure':'pending',
              'language_review':{language:'pending'}}
            plan={'format':'kristal.wiki-editorial-plan/1.0','slug':slug,
                 'language':language,'locale':'fr-CA' if language=='fr' else None,
                 'archetype':None,'capability_profile':None,'runtime_set_id':None,
                 'source':source,'content':{'article':None,'units':[],'evidence':[],'sections':[]},
                 'projections':{}}
            items=[]
            for a in s['assertions']:
                statement=a.get('statement') if isinstance(a,dict) else None
                items.append({'assertion_id':a.get('assertion_id'),
                              'predicate':statement.get('predicate') if isinstance(statement,dict) else None,
                              'assertion_status':a.get('assertion_status'),
                              'record_role':a.get('record_role'),
                              'evidence_refs_count':len(a.get('evidence_refs') or [])})
            (folder/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
            (folder/'assertion-inventory.json').write_text(json.dumps({'source':'portable-kristal-v6',
             'state_id':s.get('state_id'),'assertion_count':len(items),'assertions':items},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
            summary[slug]={'workspace':ws.name,'assertion_count':len(items),
                'ambiguous_assertion_ids':sorted(portable['ambiguous']),'status':'REVIEW_REQUIRED'}
        (stage/'LIRE_AVANT.md').write_text('''# Plans Wiki privés — sélection requise\n\nCes fichiers ne sont **pas** des autorisations de publier et ne sont pas des textes générés par SemantiK.\n\nPour chaque Kristal : sélectionner les assertions à communiquer, produire une vraie projection `semantik.kristal-v6.communication-projection/1.0` par clé Spek et renseigner `projections` dans `plan.json`.\nLa projection doit pointer vers le `state_id` et `content_hash` du portable v6 et conserver les `source_refs` des assertions choisies.\nPréciser les champs éditoriaux (`article`, `units`, `evidence`, `sections`) selon les `layouts/*.json` de Spek et un archétype du registre Spek.\nLes statuts `pending` NE DOIVENT PAS être remplacés par `approved` sans vérification réelle.\nConfigurer un RuntimeSet SemantiK/GF RELEASED qui sait exprimer les prédicats concernés.\nExécuter le pipeline seulement après publication C1/C2/C3 de la collection ciblée, et vérifier séparément la diffusion des pages Wiki.\n''',encoding='utf8')
        if write:os.rename(stage,output)
    return {'status':'PRIVATE_PLANS_CREATED' if write else 'DRY_RUN','kristals':summary,
            'output':str(output) if write else None, 'publication':'NOT_PERFORMED'}

def main(argv=None):
    p=argparse.ArgumentParser()
    for x in ('collection','locals-root','output'):p.add_argument('--'+x,required=True)
    p.add_argument('--language',choices=('fr','en','it'),default='fr')
    p.add_argument('--write',action='store_true')
    a=p.parse_args(argv)
    try:
        ret=scaffold(collection=Path(a.collection),locals_root=Path(a.locals_root),
          output=Path(a.output),language=a.language,write=a.write)
        print(json.dumps(ret,ensure_ascii=False,indent=2));return 0
    except (WikiPipelineError,KeyError,ValueError,OSError) as exc:
        print('BLOCKED: '+str(exc),file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())
