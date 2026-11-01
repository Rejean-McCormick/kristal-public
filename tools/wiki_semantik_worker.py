#!/usr/bin/env python3
"""Isolated SemantiK SDK invocation (requires a real released RuntimeSet)."""
from __future__ import annotations
import json
from pathlib import Path
import sys


def main(argv: list[str]) -> int:
    if len(argv) != 5:
        print('usage: worker envelope.json runtime_root language locale capability_profile',file=sys.stderr)
        return 2
    envelope_path, runtime_root, language, locale, profile = argv
    try:
        from semantik_architect.adapters.ecosystem import KristalV6Acl
        from semantik_architect.adapters.inbound.python_sdk import SemantikArchitect
        envelope = json.loads(Path(envelope_path).read_text(encoding='utf-8'))
        request = KristalV6Acl().map_request(envelope['projection'],
              target_language=language,target_locale=locale,capability_profile=profile)
        app = SemantikArchitect.from_runtime_root(runtime_root)
        result = app.render(request)
        print(json.dumps(result,ensure_ascii=False,sort_keys=True))
        return 0
    except Exception as exc:
        print('SA_RENDER_BLOCKED: '+str(exc),file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
