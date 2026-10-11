import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import hashlib

SPEC=importlib.util.spec_from_file_location('c3_collection',Path(__file__).resolve().parents[1]/'tools/c3_collection.py')
c3=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(c3)

class C3CollectionTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        d=self.root/'kristals/zoology'
        (d/'state').mkdir(parents=True)
        (d/'.kristal').mkdir()
        state={'schema_version':'9.0','artifact_type':'kristal_state_snapshot','state_ref':'urn:kristal:state:zoology','logical_commitment':{'profile':'kristal.state-commitment/jcs-sha256-v1','digest':'sha256:'+'a'*64},'members':[{'artifact_id':'urn:kristal:artifact:test','logical_contract':{'id':'test','version':'1.0'},'logical_commitment':{'profile':'kristal.logical/jcs-sha256-v1','digest':'sha256:'+'b'*64}}],'parents':[],'references':[]}
        (d/'state/state-snapshot.json').write_text(json.dumps(state),encoding='utf8')
        (d/'AI_START_HERE.md').write_text('# Zoology\n',encoding='utf8')
        (d/'ai').mkdir()
        (d/'AI_MANIFEST.json').write_text(json.dumps({'state_ref':state['state_ref'],'state_logical_commitment':state['logical_commitment']}),encoding='utf8')
        (d/'ai/INDEX.json').write_text(json.dumps({'files':[{'path':'AI_START_HERE.md'}]}),encoding='utf8')
        files=[]
        for rel in ['AI_MANIFEST.json','AI_START_HERE.md','ai/INDEX.json','state/state-snapshot.json']:
            b=(d/rel).read_bytes()
            files.append(dict(path=rel,role='ai_entrypoint' if rel=='AI_START_HERE.md' else 'state_snapshot',size=len(b),sha256=c3.sha(b)))
        projection={'format':c3.SURFACE_FORMAT,'slug':'zoology','state_ref':state['state_ref'],'state_logical_commitment':state['logical_commitment'],'entrypoint':'AI_START_HERE.md','files':files,'materialization_objects':[]}
        manifest={'format':c3.MANIFEST_FORMAT,'manager_version':'0.1.0-alpha.11','read_surface_format':c3.SURFACE_FORMAT,'slug':'zoology','title':'Zoology','target_root':'kristals/zoology','entrypoint':'AI_START_HERE.md','state_ref':state['state_ref'],'state_logical_commitment':state['logical_commitment'],'surface_digest':c3.sha(c3.canonical(projection)),'file_count':len(files),'total_bytes':sum(x['size'] for x in files),'materialization_object_count':0,'files':files,'policy':{k:True for k in c3.POLICY_KEYS}}
        self.manifest_path=d/'.kristal/sync-manifest.json'
        self.manifest_path.write_text(json.dumps(manifest),encoding='utf8')

    def write_index(self):
        i=c3.create_candidate_index(self.root)
        (self.root/'kristals/index.json').write_text(json.dumps(i),encoding='utf8')
        return i

    def test_valid_collection_and_candidate(self):
        i=self.write_index()
        self.assertEqual(c3.validate_index(self.root)['index_digest'],i['index_digest'])
        self.assertEqual(c3.check_snapshot(self.root,'zoology')['state_ref'],'urn:kristal:state:zoology')

    def test_missing_index_blocks(self):
        with self.assertRaisesRegex(c3.C3Error,'NOT QUALIFIED'):
            c3.validate_index(self.root)

    def test_unindexed_snapshot_only_blocks(self):
        self.manifest_path.unlink()
        with self.assertRaises(c3.C3Error):
            c3.create_candidate_index(self.root)

    def test_checksum_drift_blocks(self):
        self.write_index()
        (self.root/'kristals/zoology/AI_START_HERE.md').write_text('tampered',encoding='utf8')
        with self.assertRaisesRegex(c3.C3Error,'size drift|checksum drift'):
            c3.validate_index(self.root)

    def test_extra_file_blocks(self):
        self.write_index()
        (self.root/'kristals/zoology/SECRET.md').write_text('not listed',encoding='utf8')
        with self.assertRaisesRegex(c3.C3Error,'unmanaged'):
            c3.validate_index(self.root)

    def test_index_digest_drift_blocks(self):
        i=self.write_index()
        i['index_digest']='sha256:'+'0'*64
        (self.root/'kristals/index.json').write_text(json.dumps(i),encoding='utf8')
        with self.assertRaisesRegex(c3.C3Error,'index count/digest'):
            c3.validate_index(self.root)

    def test_symlink_blocks(self):
        self.write_index()
        import os
        target=self.root/'kristals/zoology/secret'
        try:target.symlink_to('AI_START_HERE.md')
        except (OSError,NotImplementedError):self.skipTest('symlinks disabled')
        with self.assertRaisesRegex(c3.C3Error,'symlink'):
            c3.validate_index(self.root)

    def test_sensitive_file_is_blocked_even_if_declared(self):
        d=self.root/'kristals/zoology'
        sensitive=d/'.env'
        sensitive.write_text('TOPSECRET',encoding='utf8')
        manifest=json.loads(self.manifest_path.read_text())
        data=sensitive.read_bytes()
        manifest['files'].append({'path':'.env','role':'supporting_content','size':len(data),'sha256':c3.sha(data)})
        manifest['files'].sort(key=lambda f:f['path'].encode('utf8'))
        manifest['file_count']=len(manifest['files'])
        manifest['total_bytes']=sum(x['size'] for x in manifest['files'])
        self.manifest_path.write_text(json.dumps(manifest),encoding='utf8')
        with self.assertRaisesRegex(c3.C3Error,'sensitive file'):
            c3.create_candidate_index(self.root)

    def test_wrong_root_snapshot_never_qualifies(self):
        self.write_index()
        with self.assertRaises(c3.C3Error):
            c3.check_snapshot(self.root,'../state')

    def test_zero_members_blocks(self):
        i=self.write_index()
        p=self.root/'kristals/zoology/state/state-snapshot.json'
        o=json.loads(p.read_text());o['members']=[]
        p.write_text(json.dumps(o),encoding='utf8')
        with self.assertRaises(c3.C3Error):
            c3.validate_index(self.root)

if __name__=='__main__':unittest.main()
