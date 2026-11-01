"""Two-phase local Wiki deployment. Never skips the independent Manager C1/C2 gate.

prepare: render exact Markdown release files for human review (no network)
publish: require a reviewed SHA256 receipt and a confirmation from Manager's gate;
         then use local git credentials to push the separate native GitHub Wiki.
"""
from __future__ import annotations
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

class WikiDeployError(ValueError):pass
VALID_FILE=re.compile(r'[A-Za-z0-9_-]+\.md\Z')
SHA40=re.compile(r'[a-f0-9]{40}\Z')
HEXDIGEST=re.compile(r'[a-f0-9]{64}\Z')
REPO='Rejean-McCormick/kristal-public'
BANNERS={
  '**Brouillon privé, non autorisé à la publication**': '**Projection publique dérivée des Kristals autorisés**',
  '**Private draft, not authorized for publication**': '**Public derived projection of approved Kristals**',
  '**Bozza privata, pubblicazione non autorizzata**': '**Proiezione pubblica derivata dai Kristals autorizzati**',
  '**Brouillon privé — aucune publication ni autorisation C1/C2 effectuée**':'**Projection publique dérivée — contrôles de publication effectués séparément**',
  '**Private draft — no publication or C1/C2 authorization performed**':'**Public derived projection — authorization verified separately**',
}

def _read(path:Path)->dict:
    if path.is_symlink() or not path.is_file():raise WikiDeployError('Missing regular file: '+str(path))
    try:result=json.loads(path.read_text(encoding='utf8'))
    except (OSError,ValueError) as exc:raise WikiDeployError('Invalid JSON: '+str(path)) from exc
    if not isinstance(result,dict):raise WikiDeployError('Expected JSON object')
    return result

def _pages(private:Path)->tuple[dict,dict]:
    private=private.resolve(strict=True)
    wiki=private/'wiki'
    man=_read(wiki/'manifest.json')
    pipe=_read(private/'pipeline-receipt.json')
    if (man.get('format')!='spek.wiki-collection-candidate/1.0' or
        pipe.get('format')!='kristal.spek-semantic-pipeline/1.0' or
        man.get('status')!='PRIVATE_NOT_PUBLISHED' or
        pipe.get('status')!='PRIVATE_CANDIDATE' or
        pipe.get('publication')!='NOT_PERFORMED' or
        man.get('repository')!=REPO or pipe.get('repository')!=REPO or
        man.get('revision')!=pipe.get('revision') or not SHA40.fullmatch(str(pipe.get('revision')))):
        raise WikiDeployError('Unqualified/inconsistent private Wiki receipts')
    files=man.get('files')
    if not isinstance(files,dict) or not files or not {'Home.md','_Sidebar.md'}<=set(files):
        raise WikiDeployError('No verified Wiki pages')
    if set(files)!={p.name for p in wiki.iterdir() if p.is_file() and p.name!='manifest.json'}:
        raise WikiDeployError('Unexpected/missing Wiki output file')
    if len([x for x in files if x.startswith('Kristal-')])!=len(pipe.get('kristals',{})):
        raise WikiDeployError('Wiki does not cover all published Kristals')
    output={}
    for name,digest in files.items():
        if not VALID_FILE.fullmatch(name) or not HEXDIGEST.fullmatch(str(digest)):
            raise WikiDeployError('Unsafe filename/digest')
        p=wiki/name
        if p.is_symlink() or not p.is_file() or sha256(p.read_bytes()).hexdigest()!=digest:
            raise WikiDeployError('A Wiki page has been modified: '+name)
        raw=p.read_text(encoding='utf8')
        for a,b in BANNERS.items():raw=raw.replace(a,b)
        if 'Brouillon privé' in raw or 'Private draft' in raw or 'Bozza privata' in raw or 'DÉMONSTRATION' in raw:
            raise WikiDeployError('Private/demo marker persists in '+name)
        output[name]=raw
    return output,pipe

def prepare(*,private:Path,output:Path,write:bool=False)->dict:
    pages,receipt=_pages(private)
    output=Path(output).expanduser().resolve()
    if output.exists() or not output.parent.is_dir() or any((p/'.git').exists() for p in output.parents):
        raise WikiDeployError('A new private review directory outside Git is mandatory')
    hashes={k:sha256(v.encode('utf8')).hexdigest() for k,v in pages.items()}
    release={'format':'kristal.wiki-release-candidate/1.0','repository':REPO,
             'revision':receipt['revision'],'status':'REQUIRES_INDEPENDENT_REVIEW',
             'files':hashes,'source':'speK_derived_semantik_runtime'}
    if write:
        with tempfile.TemporaryDirectory(prefix='wiki-review-stage-',dir=output.parent) as td:
            temp=Path(td)
            for name,body in pages.items():(temp/name).write_text(body,encoding='utf8')
            (temp/'release-manifest.json').write_text(json.dumps(release,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
            review={'format':'kristal.wiki-review/1.0','status':'PENDING',
                    'reviewer':'','scope':'Wiki release pages only; does not replace signed C1/C2',
                    'repository':REPO,'revision':receipt['revision'],'files':hashes}
            (temp/'wiki-review-PENDING.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
            os.rename(temp,output)
    return {'status':'REQUIRES_INDEPENDENT_WIKI_REVIEW', 'write':write,
        'pages':len(pages),'source_revision':receipt['revision'],'output':str(output) if write else None}

def _git(folder:Path,*args:str,timeout:int=120)->str:
    try:
        p=subprocess.run(['git','-C',str(folder),*args],capture_output=True,
                         text=True,encoding='utf8',errors='replace',timeout=timeout,check=False)
    except (OSError,subprocess.TimeoutExpired) as exc:raise WikiDeployError('Git unavailable') from exc
    if p.returncode:raise WikiDeployError('Git '+str(args[0])+' refused: '+(p.stderr or p.stdout)[-700:])
    return p.stdout.strip()

def publish(*,release:Path,review:Path,revision:str,
            checkout:Path|None=None,manager_root:Path|None=None,
            trust:Path|None=None,c1_dir:Path|None=None,c2_dir:Path|None=None,
            policy_dir:Path|None=None,authorization_confirmed:bool=False,
            push:bool=False,gate_verifier=None)->dict:
    """CALL ONLY AFTER Manager has independently verified C1/C2/C3 for main.

    This extra review is a human attestation over exact wiki page bytes, not a
    replacement for cryptographic C1/C2. Never provide automatic approval.
    """
    if not authorization_confirmed or not SHA40.fullmatch(revision):
        raise WikiDeployError('Independent C1/C2/C3 and Wiki review confirmation required')
    if not all(x is not None for x in (checkout,manager_root,trust,c1_dir,c2_dir,policy_dir)) and gate_verifier is None:
        raise WikiDeployError('Independent signed C1/C2/C3 evidence paths are mandatory even for direct CLI')
    if gate_verifier is None:
        if not (Path(manager_root)/'kristal_manager'/'publication_flow.py').is_file():
            raise WikiDeployError('Trusted Manager checkout unavailable')
        manager_root=Path(manager_root).resolve(strict=True)
        sys.path.insert(0,str(manager_root))
        from kristal_manager.publication_flow import publish_approved_commit,_git,_assert_checkout
        checked=_assert_checkout(Path(checkout).resolve(strict=True),require_clean=True)
        verified=publish_approved_commit(checkout=Path(checkout),trust=Path(trust),
            c1_dir=Path(c1_dir),c2_dir=Path(c2_dir),policy_dir=Path(policy_dir),
            external_approval_confirmed=True,push=False)
        remote=_git(Path(checkout),'ls-remote','origin','refs/heads/main',timeout=60)
        if not remote or remote.split()[0]!=checked:
            raise WikiDeployError('Public main HEAD not confirmed online')
    else:
        # Test-only dependency injection. CLI never exposes a gate bypass.
        verified=gate_verifier()
    if verified.get('status')!='PRE_PUBLICATION_GATES_PASS' or verified.get('revision')!=revision:
        raise WikiDeployError('Independent signed gates do not attest this exact revision')
    release=Path(release).resolve(strict=True)
    r=_read(release/'release-manifest.json');review_data=_read(Path(review))
    files=r.get('files')
    if (r.get('format')!='kristal.wiki-release-candidate/1.0' or r.get('status')!='REQUIRES_INDEPENDENT_REVIEW'
        or r.get('repository')!=REPO or r.get('revision')!=revision
        or review_data.get('format')!='kristal.wiki-review/1.0'
        or review_data.get('status')!='APPROVED' or review_data.get('repository')!=REPO
        or review_data.get('revision')!=revision or review_data.get('files')!=files
        or not review_data.get('reviewer')):
        raise WikiDeployError('No matching manual Wiki review for exact public page digests')
    for name,digest in files.items():
        if not VALID_FILE.fullmatch(name) or not HEXDIGEST.fullmatch(digest):
            raise WikiDeployError('Invalid reviewed file path/hash')
        p=release/name
        if not p.is_file() or p.is_symlink() or sha256(p.read_bytes()).hexdigest()!=digest:
            raise WikiDeployError('Reviewed Wiki page bytes changed')
    status={'status':'READY_TO_PUSH_WIKI','revision':revision,'files':sorted(files),
            'wiki_url':'https://github.com/'+REPO+'/wiki','push_performed':False}
    if not push:return status
    wiki_url='https://github.com/'+REPO+'.wiki.git'
    # GitHub rejects clone until wiki enabled/initialized in repository Settings.
    with tempfile.TemporaryDirectory(prefix='kristal-wiki-push-') as tmp:
        tmp=Path(tmp);local=tmp/'repo'
        try:
            cp=subprocess.run(['git','clone','--',wiki_url,str(local)],capture_output=True,
                              text=True,encoding='utf8',errors='replace',timeout=120)
        except (OSError,subprocess.TimeoutExpired) as exc:raise WikiDeployError('Cannot clone native GitHub Wiki') from exc
        if cp.returncode:
            raise WikiDeployError('GitHub Wiki not enabled/initialized or Git authentication failed: '+(cp.stderr or cp.stdout)[-500:])
        branch=_git(local,'branch','--show-current')
        if branch not in ('master','main'):raise WikiDeployError('Unknown Wiki branch')
        origin=_git(local,'remote','get-url','origin')
        if origin.rstrip('/')!=wiki_url:raise WikiDeployError('Wiki remote mismatch')
        if _git(local,'status','--porcelain'):
            raise WikiDeployError('Wiki checkout unexpectedly dirty')
        # Never delete unrelated wiki pages; deny divergent overwrite without review.
        for name in files:
            target=local/name
            if target.exists() and target.read_bytes()!= (release/name).read_bytes():
                raise WikiDeployError('Wiki page already exists and differs: '+name+'. Explicit update review needed.')
            shutil.copy2(release/name,target)
        _git(local,'add','--',*files)
        if not _git(local,'diff','--cached','--name-only'):
            return {**status,'status':'WIKI_ALREADY_CURRENT','push_performed':False}
        hooks=tmp/'no-hooks';hooks.mkdir()
        _git(local,'-c','core.hooksPath='+str(hooks),'commit','-m',
             'Publish approved Kristal Wiki from '+revision[:12])
        newsha=_git(local,'rev-parse','HEAD')
        # Regular fast-forward push only, no force.
        _git(local,'push','origin','HEAD:refs/heads/'+branch,timeout=150)
        posted=_git(local,'ls-remote','origin','refs/heads/'+branch).split()[0]
        if posted!=newsha:raise WikiDeployError('Wiki push not confirmed by remote SHA')
        return {**status,'status':'WIKI_PUBLISHED','push_performed':True,'wiki_commit':posted}

def main(argv=None)->int:
    p=argparse.ArgumentParser(description='GitHub Wiki release with independent review')
    sub=p.add_subparsers(dest='cmd',required=True)
    a=sub.add_parser('prepare');a.add_argument('--private',required=True);a.add_argument('--output',required=True);a.add_argument('--write',action='store_true')
    b=sub.add_parser('publish');b.add_argument('--release',required=True);b.add_argument('--review',required=True);b.add_argument('--revision',required=True);b.add_argument('--external-gates-confirmed',action='store_true');b.add_argument('--push',action='store_true')
    for field in ('checkout','manager-root','trust','c1-dir','c2-dir','policy-dir'):b.add_argument('--'+field,required=True)
    x=p.parse_args(argv)
    try:
        r=prepare(private=Path(x.private),output=Path(x.output),write=x.write) if x.cmd=='prepare' else publish(
             release=Path(x.release),review=Path(x.review),revision=x.revision,
             checkout=Path(x.checkout),manager_root=Path(x.manager_root),
             trust=Path(x.trust),c1_dir=Path(x.c1_dir),c2_dir=Path(x.c2_dir),policy_dir=Path(x.policy_dir),
             authorization_confirmed=x.external_gates_confirmed,push=x.push)
        print(json.dumps(r,ensure_ascii=False,indent=2));return 0
    except (WikiDeployError,OSError,ValueError,KeyError,TypeError) as exc:
        print('BLOCKED: '+str(exc),file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())
