"""Synthetic, independently signed offline C1/C2 receipt fixtures. Not real approval."""
import base64
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'tools'))
import c3_collection as c3
import c123_offline as gate
import test_c3_collection as fixture

try:
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
except ImportError:
    Ed25519PrivateKey = None


@unittest.skipIf(Ed25519PrivateKey is None, 'optional cryptography dependency not installed')
class OfflineGateTests(unittest.TestCase):
    def setUp(self):
        fixture.C3CollectionTests.setUp(self)
        self.index=fixture.C3CollectionTests.write_index(self)
        self.private=tempfile.TemporaryDirectory()
        self.addCleanup(self.private.cleanup)
        ext=Path(self.private.name)
        self.trust=ext/'trusted.json'; self.c1path=ext/'c1.json'; self.c2path=ext/'c2.json'
        def git(*args):
            subprocess.run(['git','-C',str(self.root),*args],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        git('init','-q')
        git('config','user.name','Synthetic Test')
        git('config','user.email','synthetic@example.invalid')
        git('add','-A')
        git('commit','-qm','Synthetic C3 fixture')
        self.commit=subprocess.run(['git','-C',str(self.root),'rev-parse','HEAD'],check=True,capture_output=True,text=True).stdout.strip()
        self.c1key=Ed25519PrivateKey.generate()
        self.c2key=Ed25519PrivateKey.generate()
        b64=lambda v:base64.b64encode(v).decode('ascii')
        self.policy={'format':gate.TRUST_FORMAT,'repository':gate.REPO,
                     'keys':[{'key_id':name,'role':role,'status':'active',
                              'public_key_base64':b64(key.public_key().public_bytes(Encoding.Raw,PublicFormat.Raw))}
                             for name,role,key in [('c1-independent','C1',self.c1key),('c2-owner','C2',self.c2key)]],
                     'revoked_keys':[],'revoked_receipts':[]}
        self.subject=gate.exact_subject(self.index['kristals'][0],self.index,self.commit)
        common={'issuer_key_id':'c1-independent','subject':self.subject,
                'issued_at':'2026-10-26T00:00:00Z','not_before':'2026-10-26T00:00:00Z',
                'expires_at':'2026-11-30T00:00:00Z'}
        self.c1={**common,'format':gate.C1_FORMAT,'decision':'qualified'}
        self.sign(self.c1, self.c1key)
        self.c2={**{**common,'issuer_key_id':'c2-owner'},'format':gate.C2_FORMAT,
                 'decision':'approved','c1_receipt_digest':c3.sha(c3.canonical(self.c1)),
                 'allowed_paths':gate.exact_paths(self.root,'zoology'),'visibility':'public'}
        self.sign(self.c2,self.c2key)
        self.flush()

    def sign(self, receipt, key):
        receipt['signature']=base64.b64encode(key.sign(c3.canonical({k:v for k,v in receipt.items() if k!='signature'}))).decode('ascii')

    def flush(self):
        for path,obj in [(self.trust,self.policy),(self.c1path,self.c1),(self.c2path,self.c2)]:
            path.write_text(json.dumps(obj),encoding='utf-8')

    def verify(self):
        self.flush()
        return gate.verify(self.root,'zoology',self.trust,self.c1path,self.c2path,
                           now=datetime(2026,10,27,tzinfo=timezone.utc))

    def test_valid_independent_receipts_undeniably_not_publication(self):
        report=self.verify()
        self.assertEqual(report['status'],'SIGNED_EVIDENCE_MATCHES_LOCAL_POLICY')
        self.assertFalse(report['public_exposure_authorized'])
        self.assertFalse(report['publication_performed'])
        self.assertEqual(report['scope_paths_count'],6)
        self.assertEqual(report['remote_immutability'],'NOT_VERIFIED')

    def test_tampered_signature_rejected(self):
        self.c1['subject']['slug']='another'
        with self.assertRaisesRegex(gate.GateError,'signature'):
            self.verify()

    def test_different_subject_after_valid_resign_rejected(self):
        self.c1['subject']={**self.subject,'source_commit':'0'*40}
        self.sign(self.c1,self.c1key)
        self.c2['c1_receipt_digest']=c3.sha(c3.canonical(self.c1))
        self.sign(self.c2,self.c2key)
        with self.assertRaisesRegex(gate.GateError,'subject differs'):
            self.verify()

    def test_expired_receipt_rejected(self):
        self.c2['expires_at']='2026-10-26T00:00:00Z'
        self.sign(self.c2,self.c2key)
        with self.assertRaisesRegex(gate.GateError,'expired'):
            self.verify()

    def test_revoked_c1_receipt_rejected(self):
        self.policy['revoked_receipts'].append(c3.sha(c3.canonical(self.c1)))
        with self.assertRaisesRegex(gate.GateError,'revoked'):
            self.verify()

    def test_revoked_c2_key_rejected(self):
        self.policy['revoked_keys'].append('c2-owner')
        with self.assertRaises(gate.GateError):
            self.verify()

    def test_allowed_path_subset_rejected(self):
        self.c2['allowed_paths']=self.c2['allowed_paths'][:-1]
        self.sign(self.c2,self.c2key)
        with self.assertRaisesRegex(gate.GateError,'scope'):
            self.verify()

    def test_wrong_c1_digest_rejected(self):
        self.c2['c1_receipt_digest']='sha256:'+'0'*64
        self.sign(self.c2,self.c2key)
        with self.assertRaisesRegex(gate.GateError,'bind exact'):
            self.verify()

    def test_same_key_bytes_c1_c2_rejected(self):
        self.policy['keys'][1]['public_key_base64']=self.policy['keys'][0]['public_key_base64']
        with self.assertRaisesRegex(gate.GateError,'distinct'):
            self.verify()

    def test_malformed_trust_inside_public_repo_rejected(self):
        inside=self.root/'trust-policy.json'
        inside.write_text(json.dumps(self.policy),encoding='utf8')
        with self.assertRaisesRegex(gate.GateError,'outside public checkout'):
            gate.read_policy(self.root,inside)

    def test_no_index_rejected(self):
        (self.root/'kristals/index.json').unlink()
        with self.assertRaises(gate.GateError):
            self.verify()

    def test_dirty_checkout_rejected(self):
        (self.root/'kristals/zoology/AI_START_HERE.md').write_text('tamper')
        with self.assertRaisesRegex(gate.GateError,'changed or untracked'):
            self.verify()

    def test_gitless_checkout_rejected(self):
        import shutil
        shutil.rmtree(self.root/'.git')
        with self.assertRaisesRegex(gate.GateError,'missing or unusable Git'):
            self.verify()

    def test_missing_crypto_package_fails_closed(self):
        original=__import__
        def deny_crypto(name, *args, **kwargs):
            if name.startswith('cryptography'):
                raise ImportError('synthetic dependency failure')
            return original(name, *args, **kwargs)
        self.flush()
        with patch('builtins.__import__', side_effect=deny_crypto):
            with self.assertRaisesRegex(gate.GateError,'dependency unavailable'):
                gate.verify(self.root,'zoology',self.trust,self.c1path,self.c2path,
                            now=datetime(2026,10,27,tzinfo=timezone.utc))


if __name__=='__main__':
    unittest.main()
