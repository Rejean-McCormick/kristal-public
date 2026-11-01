"""Offline Wiki navigation tests; never publish or call GitHub."""
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from wiki_export import render,generate
from test_c3_collection import C3CollectionTests

class WikiTests(unittest.TestCase):
    def setUp(self):
        self.test=C3CollectionTests('test_valid_collection_and_candidate')
        self.test.setUp()
        self.addCleanup(self.test.tmp.cleanup)
        self.index=self.test.write_index()

    def test_wiki_is_navigation_only(self):
        pages=render(self.index,'ExampleOwner/kristal-public','f'*40)
        self.assertEqual(sorted(pages),['Home.md','Kristal-zoology.md','_Sidebar.md'])
        self.assertIn('blob/'+'f'*40+'/kristals/zoology/AI_START_HERE.md',pages['Kristal-zoology.md'])
        self.assertIn('[Zoology](Kristal-zoology)',pages['Home.md'])
        self.assertNotIn('data:application',str(pages))

    def test_no_live_wiki_sync_and_safe_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'new-wiki'
            with self.assertRaisesRegex(ValueError,'SemantiK Architect REQUIRED'):
                generate(self.test.root,path,'ExampleOwner/kristal-public','a'*40)
            self.assertFalse(path.exists())
            with self.assertRaisesRegex(ValueError,'SemantiK Architect REQUIRED'):
                generate(self.test.root,path,'ExampleOwner/kristal-public','a'*40,write=True)

    def test_reject_unpinned_branch_and_markup(self):
        with self.assertRaises(ValueError):render(self.index,'ExampleOwner/kristal-public','main')
        self.index['kristals'][0]['title']='<script>alert(1)</script>'
        text=render(self.index,'ExampleOwner/kristal-public','a'*40)['Home.md']
        self.assertNotIn('<script>',text)

if __name__=='__main__':unittest.main()
