"""Strict SemantiK Architect NLG adapter for *private* Kristal wiki drafts.

Only an explicit, upstream-selected Kristal v6 communication projection may be
realized. Never infer facts or a communication obligation from C3 metadata.
Every Wiki page remains private until *separate* publication authorization.
"""
from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Any

CONTRACT = 'semantik.kristal-v6.communication-projection/1.0'
ENVELOPE = 'kristal.semantik-wiki-page/1.0'
SLUG = re.compile(r'^[a-z0-9][a-z0-9._-]*$')
HEX_SHA = re.compile(r'^[0-9a-f]{40}$')


class WikiSemantikError(ValueError):
    pass


def _read_projection(projections: Path, slug: str) -> dict[str, Any]:
    if not SLUG.fullmatch(slug):
        raise WikiSemantikError('Invalid Kristal slug')
    path = projections / (slug + '.json')
    if not path.is_file() or path.is_symlink():
        raise WikiSemantikError(f'Missing explicit SemantiK projection: {slug}.json')
    if not path.resolve().is_relative_to(projections.resolve()):
        raise WikiSemantikError('Projection escapes private directory')
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        raise WikiSemantikError(f'Invalid projection for {slug}: {exc}') from exc
    if not isinstance(data, dict):
        raise WikiSemantikError(f'Projection must be an object: {slug}')
    return data


def _request_and_binding(envelope: dict, row: dict, revision: str) -> tuple[dict, str, str, str]:
    if envelope.get('format') != ENVELOPE:
        raise WikiSemantikError('Unsupported wiki semantic envelope contract')
    binding = envelope.get('binding')
    projection = envelope.get('projection')
    if not isinstance(binding, dict) or not isinstance(projection, dict):
        raise WikiSemantikError('Binding and explicit projection are required')
    if (binding.get('slug') != row['slug'] or
        binding.get('state_ref') != row['state_ref'] or
        binding.get('state_logical_commitment') != row['state_logical_commitment']['digest'] or
        binding.get('surface_digest') != row['surface_digest'] or
        binding.get('published_revision') != revision):
        raise WikiSemantikError('Projection is not bound to the exact published C3 revision/state')
    if projection.get('contract') != CONTRACT or projection.get('kristal_standard') != '6.0.0':
        raise WikiSemantikError('Explicit Kristal-v6 communication-projection/1.0 required')
    chosen = projection.get('selected_assertions')
    request = projection.get('communication_request')
    if not isinstance(chosen, list) or not chosen or not isinstance(request, dict):
        raise WikiSemantikError('No explicit selected assertions / communication request')
    language = envelope.get('language')
    locale = envelope.get('locale')
    profile = envelope.get('capability_profile')
    if not isinstance(language, str) or not re.fullmatch(r'[a-z]{2,3}', language):
        raise WikiSemantikError('Explicit target language is required')
    if not isinstance(locale, str) or not re.fullmatch(r'[a-z]{2,3}(?:-[A-Za-z]{2,4})?', locale):
        raise WikiSemantikError('Explicit target locale is required')
    if not isinstance(profile, str) or not profile or len(profile) > 128:
        raise WikiSemantikError('Explicit released capability profile is required')
    selector = request.get('runtime_selector')
    if not isinstance(selector, dict) or not isinstance(selector.get('runtime_set_id'), str):
        raise WikiSemantikError('Request must pin the exact runtime_set_id')
    return projection, language, locale, profile


def _escape_markdown_literal(value: Any) -> str:
    # Treat an NLG output block as *text*, not user-supplied Markdown/HTML.
    s = ' '.join(str(value).split())
    return re.sub(r'([\\`*_{}\[\]<>!|#])', r'\\\1', s)


def _blocks_to_markdown(blocks: list[dict]) -> str:
    parts = []
    for block in blocks:
        if not isinstance(block, dict) or block.get('kind') not in (
            'utterance', 'notice', 'heading', 'label_value', 'list', 'question', 'paragraph'
        ):
            raise WikiSemantikError('Unsupported or malformed SemantiK block')
        kind = block['kind']
        if kind == 'list':
            items = block.get('items')
            if not isinstance(items, list) or not items:
                raise WikiSemantikError('Empty SemantiK list block')
            parts.append('\n'.join('- ' + _escape_markdown_literal(x.get('text', '')) for x in items))
        elif kind == 'label_value':
            parts.append('**'+_escape_markdown_literal(block.get('label',''))+':** '+_escape_markdown_literal(block.get('value','')))
        elif kind == 'heading':
            parts.append('## '+_escape_markdown_literal(block.get('text','')))
        else:
            value = _escape_markdown_literal(block.get('text',''))
            if not value:raise WikiSemantikError('Empty SemantiK block')
            parts.append(value)
    return '\n\n'.join(parts)


def _check_result(projection: dict, language: str, profile: str, result: dict) -> None:
    if not isinstance(result, dict) or result.get('language') != language:
        raise WikiSemantikError('SemantiK result language mismatch')
    req = projection['communication_request']
    runtime = result.get('runtime')
    if (not isinstance(runtime, dict) or
        runtime.get('runtime_set_id') != req['runtime_selector']['runtime_set_id'] or
        runtime.get('capability_profile') != profile):
        raise WikiSemantikError('SemantiK RuntimeSet/profile not pinned as requested')
    blocks = result.get('blocks')
    if not isinstance(blocks, list) or not blocks:
        raise WikiSemantikError('No realized blocks: do not synthesize fallback content')
    obligations = req.get('obligations') or []
    expected = {x['obligation_id'] for x in obligations}
    if not expected or len(expected) != len(obligations):
        raise WikiSemantikError('Invalid or empty communication obligations')
    cover = result.get('coverage') or []
    covered = {x['obligation_id'] for x in cover if isinstance(x, dict) and x.get('block_ids')}
    if not expected.issubset(covered):
        raise WikiSemantikError('Missing SemantiK obligation coverage')
    chosen = {x['assertion_id'] for x in projection['selected_assertions']}
    refs = set(result.get('source_refs') or [])
    if not chosen.issubset(refs):
        raise WikiSemantikError('Selected assertion provenance was lost in the realized output')
    if not isinstance(result.get('deterministic_result_id'), str) or not re.fullmatch(r'sha256:[0-9a-f]{64}',result['deterministic_result_id']):
        raise WikiSemantikError('SemantiK result identity missing')


def realize_page(*, row: dict, revision: str, projections: Path,
                 semantik_root: Path, runtime_root: Path,
                 worker: Path | None = None, timeout: int = 120) -> tuple[str, dict]:
    """No silent fallback; a genuine SA RuntimeSet must render the explicit request."""
    if not HEX_SHA.fullmatch(revision):
        raise WikiSemantikError('Exact published revision required')
    try:
        projections = Path(projections).expanduser().resolve(strict=True)
        semantik_root = Path(semantik_root).expanduser().resolve(strict=True)
        runtime_root = Path(runtime_root).expanduser().resolve(strict=True)
    except (OSError, ValueError) as exc:
        raise WikiSemantikError('Private projections or SemantiK runtime directory unavailable') from exc
    if not (semantik_root/'src/semantik_architect/adapters/ecosystem/kristal_v6.py').is_file():
        raise WikiSemantikError('SemantiK Architect SDK source not found')
    if not (runtime_root/'activation.json').is_file():
        raise WikiSemantikError('SemantiK RuntimeSet activation.json missing')
    envelope = _read_projection(projections, row['slug'])
    projection, language, locale, profile = _request_and_binding(envelope,row,revision)
    projection_path = projections/(row['slug']+'.json')
    script = (worker or Path(__file__).with_name('wiki_semantik_worker.py')).resolve(strict=True)
    env = os.environ.copy()
    env['PYTHONPATH'] = str(semantik_root/'src') + os.pathsep + env.get('PYTHONPATH','')
    try:
        p = subprocess.run([sys.executable,str(script),str(projection_path),str(runtime_root),language,locale,profile],
                           cwd=str(semantik_root),env=env,capture_output=True,text=True,
                           encoding='utf-8',errors='replace',timeout=timeout,check=False)
    except (OSError,subprocess.TimeoutExpired) as exc:
        raise WikiSemantikError('SemantiK execution unavailable or timed out') from exc
    if p.returncode:
        raise WikiSemantikError('SemantiK rejected the communication / runtime: '+(p.stderr or p.stdout)[-700:])
    try:result = json.loads(p.stdout)
    except ValueError as exc:raise WikiSemantikError('SemantiK did not return JSON') from exc
    _check_result(projection,language,profile,result)
    markdown = _blocks_to_markdown(result['blocks'])
    digest = 'sha256:'+sha256(json.dumps(projection,sort_keys=True,ensure_ascii=False,
                                        separators=(',',':')).encode('utf-8')).hexdigest()
    meta = {'semantik_result_id':result['deterministic_result_id'],
            'projection_digest':digest,'runtime_set_id':result['runtime']['runtime_set_id'],
            'capability_profile':profile,'language':language,'locale':locale,
            'selected_assertions':len(projection['selected_assertions'])}
    return markdown,meta
