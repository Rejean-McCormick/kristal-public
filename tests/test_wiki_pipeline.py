"""Self-contained fail-closed checks. Mock realizations are NOT SemantiK qualification."""
from __future__ import annotations
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from wiki_pipeline import WikiPipelineError, _safe_file, _source, _text, _workspace, _plan_for_row


def wr(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(data),encoding='utf8')

class WikiPipelineTests(unittest.TestCase):
    def test_source_selection_ambiguous_identity_must_not_be_silently_accepted(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            wr(root/'.kristal/v8/portable-state.kristal-state.json',{
                'schema_version':'6.0','artifact_type':'kristal_state',
                'assertions':[{'assertion_id':'same','assertion_status':'reviewed'},
                              {'assertion_id':'same','assertion_status':'reviewed'},
                              {'assertion_id':'unique','assertion_status':'validated'}]})
            result=_source(root,'test')
            self.assertEqual(result['ambiguous'],{'same'})
            self.assertIn('unique',result['ids'])

    def test_workspace_resolution_uses_declared_slug(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            wr(root/'Kristal-AI/kristal.workspace.json',{'slug':'kristal-ai'})
            self.assertEqual(_workspace(root,'kristal-ai').name,'Kristal-AI')
            with self.assertRaisesRegex(WikiPipelineError,'one local workspace'):
                _workspace(root,'missing')

    def test_malformed_safe_file(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            for name in ('../secret.json','/tmp/x.json','..\\secret.json','a.txt'):
                with self.assertRaises(WikiPipelineError):_safe_file(root,name)

    def test_communication_must_fit_one_spek_slot(self):
        with self.assertRaisesRegex(WikiPipelineError,'exactly one'):
            _text({'blocks':[{'kind':'utterance','text':'a'},{'kind':'utterance','text':'b'}]})
        self.assertEqual(_text({'blocks':[{'kind':'utterance','text':'Une idée.'}]}),'Une idée.')

    def test_plan_without_approvals_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);locals=root/'locals';plans=root/'plans'
            wr(locals/'K/kristal.workspace.json',{'slug':'kristal-ai'})
            wr(locals/'K/.kristal/v8/portable-state.kristal-state.json',{
                'schema_version':'6.0','artifact_type':'kristal_state',
                'assertions':[{'assertion_id':'a','assertion_status':'reviewed'}]})
            wr(plans/'kristal-ai/plan.json',{'format':'kristal.wiki-editorial-plan/1.0',
                'slug':'kristal-ai','language':'fr','archetype':'referentiel-semantique',
                'source':{'scientific_review':'pending'}})
            row={'slug':'kristal-ai','state_ref':'urn:kristal:ai',
                'state_logical_commitment':{'digest':'sha256:'+'a'*64}}
            with self.assertRaisesRegex(WikiPipelineError,'approvals'):
                _plan_for_row(row=row,locals_root=locals,plan_root=plans,
                              language='fr',revision='b'*40)

if __name__=='__main__':unittest.main()
