from __future__ import annotations
import hashlib,json
from pathlib import Path
import sys,tempfile,unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from wiki_deploy import WikiDeployError, prepare, publish

def wr(p,o):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o),encoding='utf8')

class WikiDeployTests(unittest.TestCase):
    REV='a'*40
    def fixture(self,r:Path):
        private=r/'private';wiki=private/'wiki'
        pages={'Home.md':'# Home\n\n**Brouillon privé — aucune publication ni autorisation C1/C2 effectuée**\n',
               '_Sidebar.md':'# Menu\n','Kristal-ai.md':'# AI\n\n**Brouillon privé, non autorisé à la publication**\n'}
        for name,body in pages.items():p=wiki/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(body)
        wr(wiki/'manifest.json',{'format':'spek.wiki-collection-candidate/1.0',
            'status':'PRIVATE_NOT_PUBLISHED','repository':'Rejean-McCormick/kristal-public',
            'revision':self.REV,'files':{n:hashlib.sha256(t.encode()).hexdigest() for n,t in pages.items()}})
        wr(private/'pipeline-receipt.json',{'format':'kristal.spek-semantic-pipeline/1.0',
            'status':'PRIVATE_CANDIDATE','publication':'NOT_PERFORMED',
            'repository':'Rejean-McCormick/kristal-public','revision':self.REV,'kristals':{'ai':{}}})
        return private
    def test_review_gating(self):
        with tempfile.TemporaryDirectory() as td:
            r=Path(td);candidate=self.fixture(r);out=r/'review'
            status=prepare(private=candidate,output=out,write=True)
            self.assertEqual(status['status'],'REQUIRES_INDEPENDENT_WIKI_REVIEW')
            self.assertNotIn('Brouillon privé',(out/'Kristal-ai.md').read_text())
            template=out/'wiki-review-PENDING.json'
            with self.assertRaisesRegex(WikiDeployError,'confirmation required'):
                publish(release=out,review=template,revision=self.REV,push=False)
            with self.assertRaisesRegex(WikiDeployError,'manual Wiki review'):
                publish(release=out,review=template,revision=self.REV,
                        authorization_confirmed=True,push=False,gate_verifier=lambda:{'status':'PRE_PUBLICATION_GATES_PASS','revision':self.REV})
            approve=json.loads(template.read_text());approve.update({'status':'APPROVED','reviewer':'Example reviewer'})
            wr(r/'review.json',approve)
            ready=publish(release=out,review=r/'review.json',revision=self.REV,
                    authorization_confirmed=True,push=False,gate_verifier=lambda:{'status':'PRE_PUBLICATION_GATES_PASS','revision':self.REV})
            self.assertEqual(ready['status'],'READY_TO_PUSH_WIKI')
            (out/'Home.md').write_text('tamper')
            with self.assertRaisesRegex(WikiDeployError,'changed'):
                publish(release=out,review=r/'review.json',revision=self.REV,
                        authorization_confirmed=True,push=False,gate_verifier=lambda:{'status':'PRE_PUBLICATION_GATES_PASS','revision':self.REV})

if __name__=='__main__':unittest.main()
