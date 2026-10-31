#!/usr/bin/env python3
"""C3 collection preflight. Purely local, fail-closed, no GitHub/network/write side effects except --write-index.

The projection/digest algorithms are intentionally the ones in Kristal Manager alpha.11
and Kristal GitHub Bootstrap alpha.11. Native owners should remain normative.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys

INDEX_FORMAT = 'kristal.github-collection-index/1.0'
MANIFEST_FORMAT = 'kristal.github-sync-manifest/1.0'
SURFACE_FORMAT = 'kristal.github-read-surface/1.0'
POLICY_KEYS = ('derived_read_surface','sync_is_not_publication','activation_is_separate','materialization_blobs_are_not_implicitly_copied')
DIGEST = re.compile(r'^sha256:[0-9a-f]{64}$')
SLUG = re.compile(r'^[a-z0-9][a-z0-9._-]*$')
SENSITIVE_DIRS = {'.git','.ssh','__pycache__','node_modules','.venv'}
SENSITIVE_SUFFIXES = ('.pem','.p12','.pfx','.sqlite','.sqlite3','.db','.key')
SENSITIVE_BASENAMES = {'.env','id_rsa','id_ed25519','credentials.json','secrets.json','secrets.yml','secrets.yaml','private_key'}


class C3Error(Exception):
    pass

def require(condition, message):
    if not condition:
        raise C3Error(message)

def sha(blob):
    return 'sha256:' + hashlib.sha256(blob).hexdigest()

def canonical(obj):
    return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')

def _unique_json_keys(pairs):
    """Reject ambiguous duplicate keys instead of letting JSON use the last value."""
    result = {}
    for key, value in pairs:
        require(key not in result, f'duplicate JSON key: {key}')
        result[key] = value
    return result


def load(path):
    require(path.is_file() and not path.is_symlink(), f'missing or symlink file: {path}')
    try:
        with path.open(encoding='utf-8') as f:
            obj = json.load(f, object_pairs_hook=_unique_json_keys,
                            parse_constant=lambda value: (_ for _ in ()).throw(C3Error('invalid JSON number: ' + value)))
    except (ValueError, OSError) as exc:
        raise C3Error(f'invalid JSON {path}: {exc}') from exc
    require(isinstance(obj, dict), f'JSON object expected: {path}')
    return obj

def relpath(value):
    require(isinstance(value,str) and value and '\\' not in value,'invalid relative path')
    p=PurePosixPath(value)
    require(not p.is_absolute() and all(part not in ('..','.') for part in p.parts) and value==p.as_posix(),'unsafe/noncanonical relative path: '+value)
    return p

def checked_file(root, rel):
    p = relpath(rel)
    require(root.is_dir() and not root.is_symlink(), 'missing/symlink repository root')
    target = root.joinpath(*p.parts)
    cursor = target
    while cursor != root:
        require(not cursor.is_symlink(), 'symlink in path: ' + rel)
        cursor = cursor.parent
        require(cursor != cursor.parent, 'unsafe file path outside repository: ' + rel)
    require(target.is_file(), 'missing file: ' + rel)
    return target

def check_snapshot(root, slug):
    require(bool(SLUG.fullmatch(slug)), 'invalid slug')
    p=checked_file(root,f'kristals/{slug}/state/state-snapshot.json')
    o=load(p)
    require(o.get('schema_version')=='9.0' and o.get('artifact_type')=='kristal_state_snapshot','expected v9 state snapshot at '+str(p))
    commitment=o.get('logical_commitment') or {}
    require(isinstance(commitment,dict) and commitment.get('profile')=='kristal.state-commitment/jcs-sha256-v1' and DIGEST.fullmatch(str(commitment.get('digest') or '')),'invalid v9 state commitment')
    require(isinstance(o.get('state_ref'),str) and o['state_ref'],'missing state_ref')
    require(isinstance(o.get('members'),list) and len(o['members'])>0,'state has no members: '+slug)
    seen_artifacts = set()
    for member in o['members']:
        require(isinstance(member,dict) and isinstance(member.get('artifact_id'),str) and member['artifact_id'],'malformed member artifact id: '+slug)
        require(member['artifact_id'] not in seen_artifacts, 'duplicate member artifact id: '+slug)
        seen_artifacts.add(member['artifact_id'])
        contract=member.get('logical_contract')
        commitment=member.get('logical_commitment')
        require(isinstance(contract,dict) and isinstance(contract.get('id'),str) and isinstance(contract.get('version'),str),'malformed logical contract: '+slug)
        require(isinstance(commitment,dict) and commitment.get('profile')=='kristal.logical/jcs-sha256-v1' and DIGEST.fullmatch(str(commitment.get('digest') or '')),'malformed member commitment: '+slug)
    return o

def row_from_manifest(root, slug):
    require(bool(SLUG.fullmatch(slug)),'invalid slug')
    prefix=f'kristals/{slug}'
    m=load(checked_file(root,prefix+'/.kristal/sync-manifest.json'))
    require(m.get('format')==MANIFEST_FORMAT,'missing/invalid sync manifest: '+slug)
    require(m.get('read_surface_format')==SURFACE_FORMAT,'invalid read_surface_format: '+slug)
    require(m.get('slug')==slug and m.get('target_root')==prefix,'sync manifest path/slug drift: '+slug)
    require(m.get('entrypoint')=='AI_START_HERE.md','unsupported entrypoint: '+slug)
    require(isinstance(m.get('state_ref'),str) and m['state_ref'],'missing state_ref: '+slug)
    require(isinstance(m.get('title'),str) and m['title'].strip(),'missing title: '+slug)
    require(isinstance(m.get('manager_version'),str) and m['manager_version'],'missing manager version: '+slug)
    sc=m.get('state_logical_commitment')
    require(isinstance(sc,dict) and sc.get('profile')=='kristal.state-commitment/jcs-sha256-v1' and DIGEST.fullmatch(str(sc.get('digest') or '')),'invalid logical commitment: '+slug)
    sd=m.get('surface_digest')
    require(isinstance(sd,str) and DIGEST.fullmatch(sd),'invalid surface digest: '+slug)
    policy = m.get('policy')
    require(isinstance(policy, dict), 'missing sync safety policy object: '+slug)
    for key in POLICY_KEYS:
        require(policy.get(key) is True,'missing sync safety policy '+key+': '+slug)
    # The Kit binds materialization metadata through ai/INDEX.json, not through
    # the sync manifest. Referenced blob bytes are NEVER implicitly hosted.
    # Validate the exact inventory below; defer external blob qualification.
    require(type(m.get('materialization_object_count')) is int and m['materialization_object_count'] >= 0,
            'bad materialization metadata count: '+slug)
    files=m.get('files')
    require(isinstance(files,list) and files,'empty sync manifest files: '+slug)
    seen=set(); ordered=[]; total=0; actual=set()
    folder=root/prefix
    require(folder.is_dir() and not folder.is_symlink(),'missing/symlink surface dir: '+slug)
    for current,dirs,names in os.walk(folder,followlinks=False):
        for d in dirs:
            require(not (Path(current)/d).is_symlink(),'symlink directory in surface: '+d)
        for name in names:
            fp=Path(current)/name
            require(not fp.is_symlink(),'symlink file in surface: '+str(fp))
            actual.add(fp.relative_to(folder).as_posix())
    for item in files:
        require(isinstance(item,dict),'invalid file row: '+slug)
        rel=relpath(item.get('path'))
        parts=[x.lower() for x in rel.parts]
        basename=parts[-1]
        require(not any(x in SENSITIVE_DIRS for x in parts) and basename not in SENSITIVE_BASENAMES and not basename.startswith('.env.') and not basename.endswith(SENSITIVE_SUFFIXES),'sensitive file cannot be in public read surface: '+str(rel))
        require(rel.as_posix() not in seen,'duplicate surface path: '+str(rel))
        seen.add(rel.as_posix())
        f=checked_file(folder,rel.as_posix())
        actualsize=f.stat().st_size
        require(type(item.get('size')) is int and item['size']==actualsize,'size drift: '+str(rel))
        require(isinstance(item.get('role'),str) and item['role'],'missing file role: '+str(rel))
        digest=sha(f.read_bytes())
        require(item.get('sha256')==digest,'file checksum drift: '+str(rel))
        ordered.append({'path':rel.as_posix(),'role':item['role'],'size':actualsize,'sha256':digest})
        total+=actualsize
    unmanaged = actual - seen - {'.kristal/sync-manifest.json'}
    require(seen == actual - {'.kristal/sync-manifest.json'},
            'unmanaged or missing paths under '+prefix+': '+str(sorted(unmanaged)))
    require(type(m.get('file_count')) is int and m['file_count']==len(files),'file_count drift: '+slug)
    require(type(m.get('total_bytes')) is int and m['total_bytes']==total,'total_bytes drift: '+slug)
    for essential in ('AI_START_HERE.md','AI_MANIFEST.json','ai/INDEX.json','state/state-snapshot.json'):
        require(essential in seen,'missing required read file '+essential+': '+slug)
    ai_manifest=load(checked_file(folder,'AI_MANIFEST.json'))
    require(ai_manifest.get('state_ref')==m['state_ref'] and ai_manifest.get('state_logical_commitment')==sc,'AI manifest/state drift: '+slug)
    ai_index=load(checked_file(folder,'ai/INDEX.json'))
    require(isinstance(ai_index.get('files'),list),'ai/INDEX.json missing files array: '+slug)
    for listed in ai_index['files']:
        require(isinstance(listed,dict) and isinstance(listed.get('path'),str) and relpath(listed['path']).as_posix() in seen,'AI index references an unhosted path: '+slug)
        hosted = next(item for item in ordered if item['path'] == listed['path'])
        require(listed.get('sha256',hosted['sha256']) == hosted['sha256'] and
                listed.get('size',hosted['size']) == hosted['size'],
                'AI index file bytes mismatch: '+listed['path'])
    objects = ai_index.get('materialization_blobs', [])
    require(isinstance(objects, list) and len(objects) == m['materialization_object_count'],
            'materialization metadata/AI index count drift: '+slug)
    for i, obj in enumerate(objects):
        require(isinstance(obj, dict), f'invalid materialization metadata [{i}]: '+slug)
        require(isinstance(obj.get('sha256'),str) and DIGEST.fullmatch(obj['sha256']) and
                type(obj.get('size')) is int and obj['size'] >= 0,
                f'invalid materialization object digest/size [{i}]: '+slug)
        key = obj.get('key')
        require(isinstance(key,str) and key and '\\' not in key and not key.startswith('/') and
                not re.match(r'^[A-Za-z]:',key) and '..' not in PurePosixPath(key).parts,
                f'unsafe materialization key [{i}]: '+slug)
        locator = obj.get('locator')
        require(locator is None or isinstance(locator, (str,dict)),
                f'invalid materialization locator [{i}]: '+slug)
        if isinstance(locator,str):
            require(not locator.startswith(('file:', '/', '\\')) and
                    not re.match(r'^[A-Za-z]:',locator),
                    f'local materialization locator cannot be published [{i}]: '+slug)
    ordered.sort(key=lambda x:x['path'].encode('utf-8'))
    projection={'format':SURFACE_FORMAT,'slug':slug,'state_ref':m['state_ref'],'state_logical_commitment':sc,'entrypoint':m['entrypoint'],'files':ordered,'materialization_objects':objects}
    require(sha(canonical(projection))==sd,'surface digest drift: '+slug)
    state=check_snapshot(root,slug)
    require(m['state_ref']==state['state_ref'] and sc==state['logical_commitment'],'state/manifest mismatch: '+slug)
    return dict(slug=slug,title=m['title'],path=prefix,entrypoint=prefix+'/AI_START_HERE.md',state_ref=m['state_ref'],state_logical_commitment=sc,surface_digest=sd,file_count=len(files),total_bytes=total,materialization_object_count=len(objects))

def scan_slugs(root):
    folder = root/'kristals'
    require(folder.is_dir() and not folder.is_symlink(), 'missing kristals/ directory')
    out = []
    for p in folder.iterdir():
        require(not p.is_symlink(), 'symlink in kristals/: '+p.name)
        if p.is_dir():
            require(bool(SLUG.fullmatch(p.name)), 'unsafe folder: '+p.name)
            out.append(p.name)
        else:
            require(p.is_file() and p.name == 'index.json',
                    'unrecognized entry in collection root: '+p.name)
    return sorted(out, key=lambda slug: slug.encode('utf-8'))

def index_for_rows(rows):
    ordered=sorted(rows,key=lambda x:(x['slug'].encode('utf-8'),x['path'].encode('utf-8')))
    projection={'format':INDEX_FORMAT,'kristals':ordered}
    return {**projection,'count':len(ordered),'index_digest':sha(canonical(projection)),'note':'Derived navigation index for GitHub/AI discovery; not semantic authority.'}

def create_candidate_index(root):
    slugs=scan_slugs(root)
    require(slugs,'no hosted Kristals')
    rows=[row_from_manifest(root,x) for x in slugs]
    require(len({x['state_ref'] for x in rows})==len(rows),'duplicate state_ref across Kristals')
    return index_for_rows(rows)

def validate_index(root):
    p=root/'kristals/index.json'
    require(p.is_file(),'kristals/index.json absent: collection NOT QUALIFIED')
    doc=load(p)
    require(set(doc)=={'format','kristals','count','index_digest','note'},'unexpected or missing collection index keys')
    require(doc.get('format')==INDEX_FORMAT,'invalid collection index format')
    require(isinstance(doc.get('kristals'),list),'invalid collection index rows')
    expected=create_candidate_index(root)
    require(doc['kristals']==expected['kristals'],'collection index rows do not exactly match hosted read surfaces')
    require(doc['count']==expected['count'] and doc['index_digest']==expected['index_digest'],'index count/digest mismatch')
    require(len(doc['kristals'])>0,'empty index cannot qualify a public Kristal release')
    return expected

def main(argv=None):
    ap=argparse.ArgumentParser(description='C3 offline validation (NOT publication authorization/independent qualification)')
    ap.add_argument('--repo',default='.')
    sub=ap.add_subparsers(dest='command',required=True)
    sub.add_parser('scan',help='report incomplete public collection; return nonzero if incomplete')
    bi=sub.add_parser('build-index',help='print canonical candidate index; only write with --write')
    bi.add_argument('--write',action='store_true')
    sub.add_parser('validate-index',help='strict all surfaces + index')
    cp=sub.add_parser('candidate',help='strict preflight for one public Kristal; never publishes')
    cp.add_argument('--slug',required=True)
    args=ap.parse_args(argv)
    root=Path(args.repo).resolve()
    try:
        if args.command=='scan':
            print(json.dumps({'slugs':scan_slugs(root),'has_index':(root/'kristals/index.json').is_file(),'qualification':'NOT ESTABLISHED'},ensure_ascii=False))
            result=validate_index(root)
        elif args.command=='build-index':
            result=create_candidate_index(root)
            if args.write:
                target=root/'kristals/index.json'
                target.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
                print('candidate index written locally; this is NOT publication authorization',file=sys.stderr)
        elif args.command=='validate-index':
            result=validate_index(root)
        else:
            result=validate_index(root)
            row=next((x for x in result['kristals'] if x['slug']==args.slug),None)
            require(row is not None,'slug absent from validated index: '+args.slug)
            require(len(check_snapshot(root,args.slug)['members'])>0,'empty semantic state')
            result={'slug':args.slug,'state_ref':row['state_ref'],'state_logical_commitment':row['state_logical_commitment'],'integrity':'PASS','publication_authorized':False,'independent_qualification':False}
        print(json.dumps(result,sort_keys=True,ensure_ascii=False))
        return 0
    except (C3Error, OSError, ValueError,TypeError) as e:
        print('C3 BLOCKED: '+str(e),file=sys.stderr)
        return 2
if __name__=='__main__':raise SystemExit(main())
