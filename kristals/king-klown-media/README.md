# Kristal — King Klown 4.2.0 MEDIA — Local 3.2.2 / State v9

**Workspace:** `kristal.local-workspace/3.2.0`  
**State architecture:** `kristal.state/9.0`  
**State ref:** `urn:kristal:state:king-klown-media`  
**Preserved State Logical Commitment:** `sha256:f237db441d6946b45b7cc06a82e96afe3f43d00dbb6192274e27785bb4f599ba`  
**Normalization:** architectural only; no semantic rewrite

## Local 3.2.2 workflow

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
```

The authoritative authoring registry is `canon/state.index.json`. The nine files in `canon/artifacts/` are byte-identical copies of the prior `.kristal/v9/artifacts/` canon, registered with precomputed v9 commitments. Legacy v6, v8 and `.kristal/v9/` surfaces are retained for compatibility and auditability.

See `docs/00_INTENT_AND_SCOPE.md` through `docs/07_HOSTING_AND_PUBLICATION.md` and `validation/local-3.2.2/`.

---

## Historical package README (preserved)

# Kristal — King Klown 4.2.0 MEDIA — Kristal v9

**Domain version:** `4.2.0-MEDIA`  
**Architecture:** Kristal v9 Semantic State Architecture  
**V9 logical state:** `.kristal/v9/state-snapshot.json`  
**Legacy v6 state:** `sha256:dc1d33eaf27eb7d54878dbb12ffbe5de704fde7aefeda71a6eb2ca405b903e27`  
**Media manifestations:** 77 = 66 YouTube + 8 Spotify + 3 SoundCloud  
**Works:** 24  
**Universe events:** 60

## V9 architecture

The migration is architectural only: the domain knowledge was not revised. Kristal v9 now commits the native knowledge model as multiple Logical Artifacts rather than treating the expanded v6 assertion state as the only canonical shape.

```text
State Snapshot
├─ entities
├─ works
├─ universe events
├─ media semantic layer
├─ aliases
├─ epistemic core claims
├─ contradictions
├─ reader policy
└─ creator clarifications
```

The existing v6 state remains byte-identical as the portable compatibility surface, and `.kristal/v8/` remains a derived language/query/read-model package.

See [`knowledge-base/documentation/KRISTAL_V9.md`](knowledge-base/documentation/KRISTAL_V9.md) and [`.kristal/v9/migration-report.json`](.kristal/v9/migration-report.json).

## Media authority

UCKK Médiathèque remains the primary URL/media catalog. This Kristal stores the semantic layer: `media_id → work_id → event_ids / arcs`. Multiple platform manifestations do not create duplicate works.

SoundCloud exact URLs remain delegated to UCKK Médiathèque because the account path contains a civil-name token forbidden by the King Klown reader policy. The Kristal retains safe set locators and stable Médiathèque item IDs.

## Notable source-state facts preserved

- `W_LB / Lumière blanche`: **media-source-available-partial**.
- `W_RAOUL`: full source remains missing; the media cycle **Raoul et Colin** remains related media rather than a silently merged work.
- Media-only works remain registered for Barok, Knowledge Pact, Pi/Éthérisme, Le Rire Cosmique, Pohénécoco, Rap Konscient, King Klown Kronicles V1, Surreal, language/politics audio, papal letter and Klown Évolutionnaire.

## Validate / rebuild v9

```bash
python knowledge-base/tools/build_v9.py
python knowledge-base/tools/validate.py
```

## Query

```bash
python knowledge-base/tools/query.py 'Lumière Blanche'
python knowledge-base/tools/query.py 'Le Rire Cosmique' --kind media
python knowledge-base/tools/query.py Konvergence
python knowledge-base/tools/query.py ouigours
```
