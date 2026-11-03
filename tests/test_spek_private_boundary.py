import importlib.util
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('wiki_deploy_guard',ROOT/'tools/wiki_deploy.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)


def test_no_private_handoff_fields_in_public_markdown():
    denied=['urn:kristal:assertion:agriculture:sha256:'+'a'*64,
            'source_assertion_refs', 'request_sha256',
            'spek.private-editorial-handoff/1.0',
            'sha256:'+'a'*64]
    assert all(module.PRIVATE_SPEK_MARKERS.search(x) for x in denied)
    assert not module.PRIVATE_SPEK_MARKERS.search('Le sol contient de la matière organique.')
