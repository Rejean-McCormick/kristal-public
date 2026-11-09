# SolarSystem — AI authoring improvement review

**State ref:** `urn:kristal:state:solar-system`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Solar-system bodies and orbits.

**Scope:** Relate celestial bodies, orbits, composition, surfaces and interactions.

**Native model:** `solar_system_reference_relational_graph`. corps → orbite → composition → surface → interactions. Les positions/éléments orbitaux de haute précision dépendent d’une époque et d’un référentiel, distincts des propriétés stables.

**Non-equivalence to preserve:** Orbital predictions and observed positions carry different evidence.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: Orbital predictions and observed positions carry different evidence.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 24 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [high]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: REJECT_UNSUPPORTED_SUGGESTION. Earlier scan candidate "Europe" is not adopted. The canon is about Solar System bodies, orbits and composition. Europe as a geographic microthesaurus is not supported. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.

## 3. Present classifications, not approvals

- Arketype: **Semantic Reference** (`ARK-01`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Space sciences**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 12 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 24 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `1af9ba5a6d22a2d3b1…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `434310bf0bc495acda…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `dcaf52716cfa880156…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `a0df29089bbc8c0014…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `8b2515868b1673a6b6…`)
- `docs/06_VALIDATION.md` (SHA-256 `1d718fe997c2d14b4e…`)
- `README.md` (SHA-256 `6c4c3c360a739fdd6a…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
