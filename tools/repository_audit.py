#!/usr/bin/env python3
"""Read-only readiness inventory for the kristal-public repository.

This report is *not* C1 qualification, C2 authorization, an approval to push,
or v10 network publication. It never edits files or accesses GitHub.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import c3_collection as c3


def audit(root: Path) -> dict:
    root = root.resolve()
    result = {
        'format': 'kristal-public.local-readiness-report/1.0-non-normative',
        'repository': 'kristal-public',
        'scope': 'offline-files-only',
        'remote_revision': 'NOT_CHECKED',
        'c1_independent_qualification': 'NOT_VERIFIED',
        'c2_public_authorization': 'NOT_VERIFIED',
        'immutable_publication': 'NOT_VERIFIED',
        'activation': 'NOT_VERIFIED',
        'approval_to_publish': False,
        'collection_index_present': (root/'kristals/index.json').is_file(),
        'collection_integrity': 'BLOCKED',
        'collection_reason': '',
        'managed_file_drift': [],
        'bootstrap_managed_hashes': 'NOT_CHECKED',
        'observed_node_id': None,
        'observed_root_state_ref': None,
        'observed_host_visibility': None,
        'slugs': [],
        'errors': [],
    }
    try:
        node = c3.load(c3.checked_file(root,'.kristal/node.json'))
        binding = c3.load(c3.checked_file(root,'.kristal/bindings/github.json'))
        state = c3.load(c3.checked_file(root,'state/state-snapshot.json'))
        result['observed_node_id'] = node.get('node_id')
        result['observed_root_state_ref'] = state.get('state_ref')
        result['observed_host_visibility'] = binding.get('resource',{}).get('visibility')
        if node.get('node_id') != binding.get('node_id'):
            result['errors'].append('node/binding node_id mismatch')
        if node.get('schema_version') != '10.0' or binding.get('schema_version') != '10.0':
            result['errors'].append('unsupported local v10 node/binding version')
        if state.get('artifact_type') != 'kristal_state_snapshot':
            result['errors'].append('root state snapshot format invalid')
    except (c3.C3Error, OSError, TypeError) as exc:
        result['errors'].append(str(exc))

    try:
        baseline = c3.load(c3.checked_file(root,'.kristal/bootstrap-state.json'))
        managed = baseline.get('managed_files')
        if not isinstance(managed,dict):
            raise c3.C3Error('bootstrap managed_files must be a map')
        for name, expected in sorted(managed.items()):
            rel = c3.relpath(name)
            if rel.as_posix() != name or not isinstance(expected,str):
                raise c3.C3Error('invalid managed-file record: '+str(name))
            try:
                f = c3.checked_file(root,name)
                actual = hashlib.sha256(f.read_bytes()).hexdigest()
            except c3.C3Error:
                result['managed_file_drift'].append({'path':name, 'status':'MISSING_OR_UNSAFE'})
                continue
            if actual != expected:
                result['managed_file_drift'].append({'path':name, 'status':'HASH_DRIFT'})
        result['bootstrap_managed_hashes'] = 'DRIFT' if result['managed_file_drift'] else 'MATCH'
    except (c3.C3Error,OSError,TypeError) as exc:
        result['errors'].append('bootstrap inventory: '+str(exc))
        result['bootstrap_managed_hashes'] = 'BLOCKED'

    try:
        result['slugs'] = c3.scan_slugs(root)
        c3.validate_index(root)
        result['collection_integrity'] = 'STRUCTURALLY_VALID_ONLY'
        result['collection_reason'] = 'C3 structural checks passed locally; C1/C2 still not verified.'
    except (c3.C3Error,OSError,ValueError,TypeError) as exc:
        result['collection_reason'] = str(exc)

    if result['errors']:
        result['collection_integrity'] = 'BLOCKED'
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description='Read-only local status (never qualifies or publishes)')
    parser.add_argument('--repo', default='.')
    parser.add_argument('--strict', action='store_true', help='nonzero exit on collection BLOCKED, metadata errors, or bootstrap drift')
    args = parser.parse_args(argv)
    report = audit(Path(args.repo))
    print(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True))
    if args.strict and (report['collection_integrity'] == 'BLOCKED' or report['errors'] or report['bootstrap_managed_hashes'] != 'MATCH'):
        return 2
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
