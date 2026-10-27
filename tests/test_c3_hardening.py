"""Adversarial regressions for the C3 structural verifier (not C1/C2)."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'tools'))
import test_c3_collection as fixture_module
c3 = fixture_module.c3
import repository_audit

class HardeningTests(unittest.TestCase):
    def setUp(self):
        fixture_module.C3CollectionTests.setUp(self)

    def write_index(self):
        return fixture_module.C3CollectionTests.write_index(self)

    def test_member_duplicate_id_is_rejected(self):
        path = self.root/'kristals/zoology/state/state-snapshot.json'
        obj=json.loads(path.read_text())
        obj['members'].append(dict(obj['members'][0]))
        path.write_text(json.dumps(obj))
        with self.assertRaisesRegex(c3.C3Error,'duplicate member'):
            c3.check_snapshot(self.root,'zoology')

    def test_member_wrong_commitment_profile_is_rejected(self):
        path=self.root/'kristals/zoology/state/state-snapshot.json'
        obj=json.loads(path.read_text());obj['members'][0]['logical_commitment']['profile']='wrong'
        path.write_text(json.dumps(obj))
        with self.assertRaisesRegex(c3.C3Error,'malformed member commitment'):
            c3.check_snapshot(self.root,'zoology')

    def test_duplicate_json_keys_fail_closed(self):
        p=self.root/'kristals/zoology/AI_MANIFEST.json'
        p.write_text('{"state_ref":"old","state_ref":"new"}')
        with self.assertRaisesRegex(c3.C3Error,'duplicate JSON key'):
            c3.load(p)

    def test_malformed_policy_fails_cleanly(self):
        m=json.loads(self.manifest_path.read_text());m['policy']=42
        self.manifest_path.write_text(json.dumps(m))
        with self.assertRaisesRegex(c3.C3Error,'policy object'):
            c3.create_candidate_index(self.root)

    def test_unlisted_root_file_blocks(self):
        (self.root/'kristals/untracked.log').write_text('surprise')
        with self.assertRaisesRegex(c3.C3Error,'unrecognized entry'):
            c3.create_candidate_index(self.root)

    def test_wrong_manifest_commitment_blocks(self):
        m=json.loads(self.manifest_path.read_text());m['state_logical_commitment']['digest']='sha256:'+'c'*64
        self.manifest_path.write_text(json.dumps(m))
        with self.assertRaises(c3.C3Error):
            c3.create_candidate_index(self.root)

    def test_wrong_ai_manifest_state_blocks(self):
        p=self.root/'kristals/zoology/AI_MANIFEST.json';d=json.loads(p.read_text())
        d['state_ref']='urn:kristal:state:some-other-state';p.write_text(json.dumps(d))
        with self.assertRaises(c3.C3Error):
            c3.create_candidate_index(self.root)

    def test_repo_audit_is_read_only_and_not_authorization(self):
        root = Path(__file__).resolve().parents[1]
        before=(root/'.kristal/bootstrap-state.json').read_bytes()
        result=repository_audit.audit(root)
        self.assertEqual(result['repository'],'kristal-public')
        self.assertEqual(result['collection_integrity'],'BLOCKED')
        self.assertFalse(result['collection_index_present'])
        self.assertFalse(result['approval_to_publish'])
        self.assertEqual(result['c1_independent_qualification'],'NOT_VERIFIED')
        self.assertEqual(result['bootstrap_managed_hashes'],'DRIFT')
        self.assertEqual(len(result['managed_file_drift']),5)
        self.assertEqual(before,(root/'.kristal/bootstrap-state.json').read_bytes())

    def test_unattended_gitsink_is_fail_closed(self):
        script=(Path(__file__).resolve().parents[1]/'GitSink.bat').read_text(encoding='utf-8')
        self.assertIn('BLOCKED',script)
        self.assertNotIn('git add --all',script.lower().replace('do not stage, commit, or push all files automatically from this script.',''))
        self.assertNotIn('\ngit push\n',script.lower())

    def test_audit_does_not_confuse_genesis_with_zoology(self):
        result=repository_audit.audit(Path(__file__).resolve().parents[1])
        self.assertNotEqual(result['observed_root_state_ref'],'urn:kristal:state:kristal-zoology')
        self.assertIn('zoology',result['slugs'])

if __name__=='__main__': unittest.main()
