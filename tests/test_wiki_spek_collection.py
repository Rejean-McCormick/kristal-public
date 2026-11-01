"""Focused, offline tests of the collection→Spek private candidate hand-off."""
from __future__ import annotations
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from wiki_spek_collection import generate, WikiSpekError

class CollectionWikiTests(unittest.TestCase):
    REV='b'*40
    def setup_fixture(self,root:Path):
        col=root/'public';col.mkdir()
        (col/'kristals/ai/state').mkdir(parents=True)
        (col/'kristals/ai/state/state-snapshot.json').write_text('{}')
        packs=root/'private';(packs/'ai').mkdir(parents=True)
        for n in ('article.json','realizations.json'):(packs/'ai'/n).write_text('{}')
        (packs/'ai/archetype.json').write_text(json.dumps({'format':'spek.wiki-archetype-binding/1.0','archetype':'composition-hybride'}))
        spek=root/'Spek';(spek/'spek').mkdir(parents=True);(spek/'spek/wiki.py').write_text('')
        return col,packs,spek
    def render_stub(self,slug:str,out:Path):
        out.mkdir()
        (out/('Kristal-'+slug+'.md')).write_text('# Test\n\nApproved slot content\n')
        (out/'manifest.json').write_text(json.dumps({'format':'spek.wiki-draft/1.0',
          'demonstration':False,'archetype':'composition-hybride'}))

    def test_composes_exact_index_and_no_git_write(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);col,packs,spek=self.setup_fixture(root)
            out=root/'candidate'
            kw=dict(collection=col,packages=packs,spek_root=spek,output=out,
                repository='a/kristal-public',revision=self.REV,language='fr',
                renderer=self.render_stub,validator=lambda _: {'kristals':[{'slug':'ai','title':'AI'}]})
            preview=generate(**kw)
            self.assertEqual(preview['status'],'DRY_RUN');self.assertFalse(out.exists())
            r=generate(**kw,write=True)
            self.assertEqual(r['status'],'PRIVATE_WIKI_CANDIDATE')
            self.assertIn('AI',(out/'Home.md').read_text())
            self.assertEqual(len(json.loads((out/'manifest.json').read_text())['kristals']),1)
            self.assertFalse((col/'Home.md').exists())
            with self.assertRaisesRegex(WikiSpekError,'new private'):
                generate(**kw,write=True)

    def test_missing_archetype_mapping_refuses(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);col,packs,spek=self.setup_fixture(root)
            (packs/'ai/archetype.json').unlink()
            with self.assertRaisesRegex(WikiSpekError,'Missing safe Spek input'):
                generate(collection=col,packages=packs,spek_root=spek,output=root/'x',
                    repository='a/b',revision=self.REV,
                    renderer=self.render_stub,validator=lambda _:{'kristals':[{'slug':'ai'}]})

    def test_c3_requires_every_kristal_to_have_realizations(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);col,packs,spek=self.setup_fixture(root)
            with self.assertRaisesRegex(WikiSpekError,'Missing safe private Spek bundle'):
                generate(collection=col,packages=packs,spek_root=spek,output=root/'x',
                    repository='a/b',revision=self.REV,renderer=self.render_stub,
                    validator=lambda _:{'kristals':[{'slug':'ai'},{'slug':'other'}]})

if __name__=='__main__':unittest.main()
