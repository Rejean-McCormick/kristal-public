"""Offline boundary tests: no GF imitation or fake public authorization."""
from pathlib import Path
import json
import sys
import tempfile
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from wiki_semantik import WikiSemantikError, _request_and_binding, _check_result, realize_page
from wiki_export import render_semantik

REV = 'a'*40
ROW = {'slug':'demo', 'title':'Demo', 'state_ref':'urn:kristal:state:demo',
       'state_logical_commitment':{'digest':'sha256:'+'b'*64},
       'surface_digest':'sha256:'+'c'*64, 'file_count':4}
ASSERTION = 'sha256:'+'d'*64
PROJECTION = {
    'contract':'semantik.kristal-v6.communication-projection/1.0',
    'kristal_standard':'6.0.0',
    'state_ref':{'state_id':'sha256:'+'e'*64,'artifact_type':'kristal_state','schema_version':'6.0'},
    'selected_assertions':[{'assertion_id':ASSERTION}],
    'communication_request':{
        'schema_version':'1.0','request_id':'demo:wikipage',
        'semantic_graph':{'graph_id':'g','nodes':[],'statements':[{
            'id':'s','predicate_ref':'example:predicate','arguments':[],
            'source_refs':[ASSERTION]}]},
        'obligations':[{'obligation_id':'o','semantic_refs':['s'],
                        'force':'PRESENT','ordering':'FIXED','source_refs':[ASSERTION]}],
        'supporting_context':[],
        'context':{'target_language':'fr','target_locale':'fr-CA'},
        'constraints':{'allowed_block_kinds':['utterance'],'opening_policy':'forbidden',
                       'closing_policy':'forbidden','list_policy':'forbidden',
                       'output_format':'structured'},
        'capability_profile':'konstellation-explorer-3',
        'runtime_selector':{'runtime_set_id':'konstellation-fr-3'}
    }
}
ENVELOPE = {
    'format':'kristal.semantik-wiki-page/1.0',
    'binding':{'slug':'demo','state_ref':ROW['state_ref'],
       'state_logical_commitment':ROW['state_logical_commitment']['digest'],
       'surface_digest':ROW['surface_digest'],'published_revision':REV},
    'language':'fr','locale':'fr-CA','capability_profile':'konstellation-explorer-3',
    'projection':PROJECTION,
}
RESULT = {'language':'fr','blocks':[{'block_id':'b','kind':'utterance',
        'obligation_ids':['o'],'text':'Ceci est une phrase générée par SA.'}],
    'runtime':{'runtime_set_id':'konstellation-fr-3',
               'capability_profile':'konstellation-explorer-3'},
    'source_refs':[ASSERTION],
    'coverage':[{'obligation_id':'o','block_ids':['b'],'realization_unit_ids':['u']}],
    'deterministic_result_id':'sha256:'+'f'*64}

class WikiSemantikBoundaryTests(unittest.TestCase):
    def test_binding_and_contract_are_mandatory(self):
        self.assertEqual(_request_and_binding(ENVELOPE,ROW,REV)[1],'fr')
        payload = json.loads(json.dumps(ENVELOPE))
        payload['binding']['surface_digest']='sha256:'+'0'*64
        with self.assertRaisesRegex(WikiSemantikError,'not bound'):
            _request_and_binding(payload,ROW,REV)
        payload=json.loads(json.dumps(ENVELOPE));payload['projection']['contract']='raw-kristal-state'
        with self.assertRaisesRegex(WikiSemantikError,'Kristal-v6'):
            _request_and_binding(payload,ROW,REV)

    def test_missing_semantik_coverage_is_rejected(self):
        result=json.loads(json.dumps(RESULT));result['coverage']=[]
        with self.assertRaisesRegex(WikiSemantikError,'coverage'):
            _check_result(PROJECTION,'fr','konstellation-explorer-3',result)
        result=json.loads(json.dumps(RESULT));result['source_refs']=[]
        with self.assertRaisesRegex(WikiSemantikError,'provenance'):
            _check_result(PROJECTION,'fr','konstellation-explorer-3',result)

    def test_no_silent_language_fallback(self):
        result=json.loads(json.dumps(RESULT));result['language']='en'
        with self.assertRaisesRegex(WikiSemantikError,'language mismatch'):
            _check_result(PROJECTION,'fr','konstellation-explorer-3',result)

    def test_realization_worker_boundary(self):
        # Stub subprocess is for ADAPTER validation only: not a language/runtime test.
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            projections=root/'projections';projections.mkdir()
            (projections/'demo.json').write_text(json.dumps(ENVELOPE),encoding='utf8')
            semantik=root/'SemantiK-Architect';(semantik/'src/semantik_architect/adapters/ecosystem').mkdir(parents=True)
            (semantik/'src/semantik_architect/adapters/ecosystem/kristal_v6.py').touch()
            runtime=semantik/'runtime';runtime.mkdir();(runtime/'activation.json').write_text('{}')
            worker=root/'fake_output_worker.py'
            worker.write_text('import json\nprint(json.dumps('+repr(RESULT)+'))\n',encoding='utf8')
            text,meta=realize_page(row=ROW,revision=REV,projections=projections,
                    semantik_root=semantik,runtime_root=runtime,worker=worker)
            self.assertIn('Ceci est une phrase générée',text)
            self.assertEqual(meta['runtime_set_id'],'konstellation-fr-3')
            (projections/'demo.json').unlink()
            with self.assertRaisesRegex(WikiSemantikError,'Missing explicit'):
                realize_page(row=ROW,revision=REV,projections=projections,
                    semantik_root=semantik,runtime_root=runtime,worker=worker)

    def test_page_requires_semantik_and_keeps_pinned_links(self):
        index={'kristals':[ROW]}
        with self.assertRaises(WikiSemantikError):
            render_semantik(index,'ExampleOwner/kristal-public',REV,
                projections=Path('missing'),semantik_root=Path('missing'),runtime_root=Path('missing'))
        def fake(**kwargs):
            return 'Texte SemantiK contrôlé',{'projection_digest':'sha256:'+'a'*64,
                  'semantik_result_id':'sha256:'+'b'*64,'runtime_set_id':'set-1'}
        pages,evidence=render_semantik(index,'ExampleOwner/kristal-public',REV,
                    projections=Path('unused'),semantik_root=Path('unused'),
                    runtime_root=Path('unused'),realize=fake)
        self.assertIn('Texte SemantiK contrôlé',pages['Kristal-demo.md'])
        self.assertIn('blob/'+REV+'/kristals/demo',pages['Kristal-demo.md'])
        self.assertIn('demo',evidence)

if __name__ == '__main__':unittest.main()
