#!/usr/bin/env python3
"""Generate a *private* GitHub Wiki markdown candidate from a C3-validated collection.

This tool does NOT clone, push, deploy or authorize public disclosure. The GitHub
Wiki is a separate Git repository. Export only after C1/C2 authorizes the same
collection revision; never use the local canonical workspace as wiki source.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote

sys.path.insert(0,str(Path(__file__).resolve().parent))
from c3_collection import validate_index, C3Error

REPO=re.compile(r'^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$')
REV=re.compile(r'^[0-9a-f]{40}$')


def _safe_text(value: str) -> str:
    # Treat source titles as text, never as Markdown links/markup or HTML.
    text=re.sub(r'[\x00-\x1f\x7f<>\[\]()*_!`#]', ' ', str(value))
    return ' '.join(text.split())[:140]


def _safe_code(value: str) -> str:
    return _safe_text(value).replace('\n',' ')


def render(index: dict, repository: str, revision: str) -> dict[str,str]:
    if not REPO.fullmatch(repository) or not REV.fullmatch(revision):
        raise ValueError('Expected owner/repo and an exact 40-hex published commit')
    rows=index.get('kristals') or []
    if not rows:raise ValueError('A real, nonempty C3 collection index is required')
    names=[]
    pages={}
    for row in rows:
        slug=row['slug']
        title=_safe_text(row['title'])
        page='Kristal-'+slug
        names.append((title,page))
        root='https://github.com/'+repository+'/blob/'+revision+'/kristals/'+quote(slug,safe='')
        lines=[f'# {title}', '',
            '**Projection de lecture du Kristal, pas une autorité sémantique.**', '',
            f'- État logique : `{_safe_code(row["state_ref"])}`',
            f'- Empreinte de surface : `{row["surface_digest"]}`',
            f'- Empreinte d’état : `{row["state_logical_commitment"]["digest"]}`',
            f'- Fichiers de lecture vérifiés : {row["file_count"]}', '',
            f'[Commencer la lecture]({root}/AI_START_HERE.md)', '',
            f'[Index IA]({root}/ai/INDEX.json)', '',
            f'[Contexte]({root}/ai/CONTEXT.md)', '',
            f'[État v9]({root}/state/state-snapshot.json)', '',
            '[Retour au catalogue](Home)', '',
            '> Les références de matérialisation ne signifient pas que les données externes ont été publiées.', '']
        pages[page+'.md']='\n'.join(lines)
    home=['# Catalogue public Kristal', '',
          'Ce wiki présente des **projections de lecture vérifiables** du dépôt de collection.',
          'Il ne remplace ni les sources locales, ni la qualification indépendante, ni l’activation.', '',
          '## Kristals', '']
    sidebar=['# Navigation', '', '[Accueil](Home)', '']
    for title,page in names:
        home.append(f'- [{title}]({page})')
        sidebar.append(f'- [{title}]({page})')
    pages['Home.md']='\n'.join(home+[''])
    pages['_Sidebar.md']='\n'.join(sidebar+[''])
    return pages


def generate(repo_root: Path, output: Path, repository: str, revision: str, *,write: bool=False) -> dict:
    repo_root=Path(repo_root).resolve()
    output=Path(output).expanduser().resolve()
    index=validate_index(repo_root)
    pages=render(index,repository,revision)
    if write:
        if output.exists():raise ValueError('Refusing to overwrite existing Wiki destination')
        if not output.parent.is_dir() or any((part/'.git').exists() for part in (output,*output.parents)):
            raise ValueError('Wiki output must be a new folder outside any Git checkout')
        # A candidate can be prepared only outside the *public* repository.
        if output.is_relative_to(repo_root) or repo_root.is_relative_to(output):
            raise ValueError('Wiki output must be outside the source collection')
        output.mkdir(parents=False)
        for name,body in pages.items():
            (output/name).write_text(body,encoding='utf8')
    return {'status':'WIKI_CANDIDATE_ONLY' if write else 'DRY_RUN',
            'deployment':'NOT_PERFORMED','c1_c2':'NOT_VERIFIED',
            'repository':repository,'revision':revision,
            'pages':sorted(pages),'count':len(index['kristals'])}


def main(argv=None) -> int:
    parser=argparse.ArgumentParser(description='Private GitHub Wiki Markdown candidate; never pushes')
    parser.add_argument('--collection',type=Path,required=True,help='Verified hosted collection candidate')
    parser.add_argument('--output',type=Path,required=True,help='New output directory')
    parser.add_argument('--repository',required=True,help='Exact GitHub owner/repo')
    parser.add_argument('--revision',required=True,help='Published commit SHA, not a floating branch')
    parser.add_argument('--write',action='store_true',help='Write private draft; dry run otherwise')
    args=parser.parse_args(argv)
    try:
        print(json.dumps(generate(args.collection,args.output,args.repository,args.revision,write=args.write),
                         ensure_ascii=False,indent=2))
        return 0
    except (C3Error,OSError,ValueError,KeyError,TypeError) as exc:
        print('WIKI BLOCKED: '+str(exc),file=sys.stderr)
        return 2

if __name__=='__main__':raise SystemExit(main())
