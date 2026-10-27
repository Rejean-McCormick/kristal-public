#!/usr/bin/env python3
"""Local C1/C2 Ed25519 receipt verifier bound to the actual C3 Git tree.

This is a *pre-publication inspection tool*, not a publisher or a trusted
central authorization service. The caller must independently protect its
out-of-repository trust policy, refresh revocation state and review approvals.
"""
from __future__ import annotations

import argparse
import base64
import binascii
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys

# Reading a clean checkout must not create new __pycache__ files.
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import c3_collection as c3

REPO = 'Rejean-McCormick/kristal-public'
TRUST_FORMAT = 'kristal-public.local-trust-policy/1.0'
C1_FORMAT = 'kristal.c1-qualification/1.0'
C2_FORMAT = 'kristal.c2-public-authorization/1.0'
COMMIT_RE = re.compile(r'[0-9a-f]{40}\Z')
KEY_ID_RE = re.compile(r'[A-Za-z0-9][A-Za-z0-9._:-]{0,127}\Z')
DATE_RE = re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z\Z')


class GateError(ValueError):
    pass


def require(test, reason):
    if not test:
        raise GateError(reason)


def outside_json(root: Path, value: Path, description: str) -> dict:
    """Private trust and receipts may not be taken from the public candidate tree."""
    require(value.is_file() and not value.is_symlink(), description + ' file absent or symlink')
    real = value.resolve(strict=True)
    root = root.resolve(strict=True)
    require(not real.is_relative_to(root), description + ' must be outside public checkout')
    try:
        return c3.load(real)
    except (c3.C3Error, OSError) as exc:
        raise GateError(str(exc)) from exc


def checked_time(value: str) -> datetime:
    require(isinstance(value, str) and DATE_RE.fullmatch(value), 'UTC time must be YYYY-MM-DDTHH:MM:SSZ')
    try:
        return datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError as exc:
        raise GateError('invalid UTC time') from exc


def verified_checkout(root: Path) -> str:
    def run(*arguments):
        try:
            res = subprocess.run(['git', '-C', str(root), *arguments], capture_output=True,
                                 text=True, check=False, timeout=15)
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise GateError('cannot inspect Git checkout') from exc
        require(res.returncode == 0, 'missing or unusable Git checkout')
        return res.stdout.strip()
    toplevel=run('rev-parse', '--show-toplevel')
    require(bool(toplevel) and Path(toplevel).resolve() == root.resolve(),
            'Git checkout root mismatch')
    require(not run('status', '--porcelain=v1', '--untracked-files=all'),
            'Git checkout has changed or untracked files; do not qualify moving bytes')
    commit = run('rev-parse', 'HEAD')
    require(bool(COMMIT_RE.fullmatch(commit)), 'expected exact SHA-1 Git commit')
    return commit


def decode_b64(value, size: int, what: str) -> bytes:
    require(isinstance(value, str) and len(value) < 4096, what + ' is missing or oversized')
    try:
        decoded = base64.b64decode(value, validate=True)
    except (binascii.Error, ValueError) as exc:
        raise GateError(what + ' is invalid base64') from exc
    require(len(decoded) == size, what + ' has invalid length')
    return decoded


def receipt_signature(receipt: dict, role: str, keys: dict, revoked: set, at: datetime):
    try:
        from cryptography.exceptions import InvalidSignature
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
    except ImportError as exc:
        raise GateError('cryptography dependency unavailable; cannot verify signatures') from exc
    expected = ({'format','issuer_key_id','subject','issued_at','not_before',
                 'expires_at','decision','signature'} if role == 'C1' else
                {'format','issuer_key_id','subject','issued_at','not_before',
                 'expires_at','decision','c1_receipt_digest','allowed_paths','visibility','signature'})
    require(set(receipt) == expected, role + ' unexpected/missing signed fields')
    require(receipt['format'] == (C1_FORMAT if role == 'C1' else C2_FORMAT), role + ' wrong format')
    require(receipt['decision'] == ('qualified' if role == 'C1' else 'approved'), role + ' decision not positive')
    keyid = receipt['issuer_key_id']
    require(isinstance(keyid,str) and keyid in keys and keys[keyid]['role']==role,
            role + ' untrusted issuer/role')
    require(keyid not in revoked, role + ' signing key is revoked')
    issued = checked_time(receipt['issued_at'])
    beginning = checked_time(receipt['not_before'])
    end = checked_time(receipt['expires_at'])
    require(issued <= at and beginning <= at < end and issued <= end,
            role + ' receipt is future-dated, inactive or expired')
    signing_bytes = c3.canonical({k:v for k,v in receipt.items() if k != 'signature'})
    signature = decode_b64(receipt['signature'], 64, role + ' signature')
    try:
        Ed25519PublicKey.from_public_bytes(keys[keyid]['key_bytes']).verify(signature, signing_bytes)
    except InvalidSignature as exc:
        raise GateError(role + ' signature verification failed') from exc
    except (ValueError, TypeError) as exc:
        raise GateError(role + ' invalid key/signature') from exc


def read_policy(root: Path, trustfile: Path):
    policy = outside_json(root,trustfile,'Trust policy')
    require(set(policy) == {'format','repository','keys','revoked_keys','revoked_receipts'},
            'trust policy unexpected fields')
    require(policy['format'] == TRUST_FORMAT and policy['repository'] == REPO,
            'trust policy identity mismatch')
    require(isinstance(policy['keys'], list) and len(policy['keys']) >= 2, 'expected independent C1 and C2 trust keys')
    require(isinstance(policy['revoked_keys'],list) and all(isinstance(x,str) for x in policy['revoked_keys']), 'invalid revoked_keys')
    require(isinstance(policy['revoked_receipts'],list) and all(isinstance(x,str) and c3.DIGEST.fullmatch(x) for x in policy['revoked_receipts']), 'invalid revoked_receipts')
    require(len(policy['revoked_keys'])==len(set(policy['revoked_keys'])), 'duplicate revoked key')
    require(len(policy['revoked_receipts'])==len(set(policy['revoked_receipts'])), 'duplicate revoked receipt')
    keys = {}
    seen_bytes = set()
    roles = set()
    for entry in policy['keys']:
        require(isinstance(entry,dict) and set(entry)=={'key_id','role','public_key_base64','status'},'invalid policy key record')
        kid = entry['key_id']
        require(isinstance(kid,str) and KEY_ID_RE.fullmatch(kid) and kid not in keys,'invalid or duplicate key ID')
        require(entry['role'] in ('C1','C2') and entry['status'] in ('active','disabled'),'invalid key role or status')
        binary = decode_b64(entry['public_key_base64'],32,'trusted public key')
        require(binary not in seen_bytes,'C1/C2 must have distinct public key bytes')
        seen_bytes.add(binary)
        keys[kid]={'role':entry['role'],'status':entry['status'],'key_bytes':binary}
        if entry['status']=='active' and kid not in policy['revoked_keys']:
            roles.add(entry['role'])
    require(roles=={'C1','C2'},'both C1/C2 roles need independently trusted active keys')
    return keys,set(policy['revoked_keys']),set(policy['revoked_receipts'])


def exact_subject(row: dict, index: dict, commit: str) -> dict:
    return {'repository':REPO,'slug':row['slug'],'source_commit':commit,
            'index_digest':index['index_digest'],'surface_digest':row['surface_digest'],
            'state_ref':row['state_ref'],'state_logical_commitment':row['state_logical_commitment']}


def exact_paths(root: Path, slug: str) -> list[str]:
    manifest = c3.load(c3.checked_file(root, f'kristals/{slug}/.kristal/sync-manifest.json'))
    files = [f'kristals/{slug}/'+x['path'] for x in manifest['files']]
    files.extend([f'kristals/{slug}/.kristal/sync-manifest.json','kristals/index.json'])
    require(len(files)==len(set(files)),'duplicate publication path')
    return sorted(files, key=lambda x:x.encode('utf-8'))


def verify(root: Path, slug: str, trustfile: Path, c1file: Path, c2file: Path,
           *, now: datetime | None = None) -> dict:
    """Check evidence only. Never returns a publication permission/grant."""
    root=root.resolve(strict=True)
    require(bool(c3.SLUG.fullmatch(slug)), 'invalid slug')
    now=now or datetime.now(timezone.utc)
    require(now.tzinfo is not None,'timezone-aware clock required')
    # No release or public upload may proceed solely from this local check.
    commit=verified_checkout(root)
    try:
        index=c3.validate_index(root)
    except (c3.C3Error,OSError,TypeError,ValueError) as exc:
        raise GateError('C3 structural verification BLOCKED: '+str(exc)) from exc
    row=next((r for r in index['kristals'] if r['slug']==slug),None)
    require(row is not None, 'slug not in C3 validated collection')
    keys,revoked_keys,revoked_receipts=read_policy(root,trustfile)
    c1=outside_json(root,c1file,'C1 receipt')
    c2=outside_json(root,c2file,'C2 receipt')
    require(keys.get(c1.get('issuer_key_id'),{}).get('status')=='active' and
            keys.get(c2.get('issuer_key_id'),{}).get('status')=='active','signing key inactive')
    require(c1.get('issuer_key_id')!=c2.get('issuer_key_id'),'same C1/C2 issuer key')
    c1_digest=c3.sha(c3.canonical(c1));c2_digest=c3.sha(c3.canonical(c2))
    require(c1_digest not in revoked_receipts and c2_digest not in revoked_receipts,
            'attestation explicitly revoked')
    receipt_signature(c1,'C1',keys,revoked_keys,now)
    receipt_signature(c2,'C2',keys,revoked_keys,now)
    subject=exact_subject(row,index,commit)
    require(c1['subject']==subject and c2['subject']==subject,
            'signed C1/C2 subject differs from checked-out exact Git/C3 bytes')
    require(c2['c1_receipt_digest']==c1_digest,'C2 does not bind exact signed C1 receipt')
    require(c2['visibility']=='public','C2 does not authorize public visibility')
    paths=c2['allowed_paths']
    require(isinstance(paths,list) and paths and all(isinstance(x,str) for x in paths),
            'C2 scope paths malformed')
    expected=exact_paths(root,slug)
    require(paths==expected,'C2 signed path scope is not exact hosted surface and index')
    return {'format':'kristal-public.offline-attestation-preflight/1.0',
            'status':'SIGNED_EVIDENCE_MATCHES_LOCAL_POLICY',
            'subject':subject,'c1_receipt_digest':c1_digest,'c2_receipt_digest':c2_digest,
            'scope_paths_count':len(paths),
            'external_issuer_validation':'NOT_PERFORMED',
            'revocation_freshness':'NOT_ESTABLISHED_OFFLINE',
            'remote_immutability':'NOT_VERIFIED',
            'public_exposure_authorized':False,'publication_performed':False}


def main(argv=None) -> int:
    parser=argparse.ArgumentParser(description='Read-only local verification; never authorizes publication')
    parser.add_argument('--repo',default='.')
    parser.add_argument('--slug',required=True)
    parser.add_argument('--trust',type=Path,required=True,help='externally managed trust policy outside the public checkout')
    parser.add_argument('--c1',type=Path,required=True,help='externally delivered signed C1 receipt')
    parser.add_argument('--c2',type=Path,required=True,help='externally delivered signed C2 receipt')
    args=parser.parse_args(argv)
    try:
        result=verify(Path(args.repo),args.slug,args.trust,args.c1,args.c2)
        print(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False))
        return 0
    except (GateError,c3.C3Error,OSError,TypeError,ValueError,KeyError) as exc:
        print(json.dumps({'status':'BLOCKED','reason':str(exc),'public_exposure_authorized':False,
                          'publication_performed':False},ensure_ascii=False),file=sys.stderr)
        return 3


if __name__=='__main__':
    raise SystemExit(main())
