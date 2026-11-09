# CivilEngineering — AI authoring improvement review

**State ref:** `urn:kristal:state:civilengineering`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Civil infrastructure design constraints.

**Scope:** Connect loads, materials, geometry and ground conditions to structures, limit states and service lives.

**Native model:** `coupled_civil_design_and_limit_states_graph`. charge × matériau × géométrie × sol → ouvrage, avec états limites, géotechnique et cycle de vie

**Non-equivalence to preserve:** Design assumptions must not be confused with verified safety.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: Design assumptions must not be confused with verified safety.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 17 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [high]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: REJECT_UNSUPPORTED_SUGGESTION. Earlier scan candidate "History" is not adopted. The model is about engineering loads, structures, materials, ground conditions and limit states; History does not describe its scope. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Semantic Reference** (`ARK-01`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Civil, military, and mining engineering**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 1 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 17 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `c196f3a20148c25208…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `cdaec85bcf29735f02…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `242ea2935e4fdccf55…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `e7adcb7afa07600704…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `39039ae9b319ae3066…`)
- `docs/06_VALIDATION.md` (SHA-256 `8a696fe17b798fa242…`)
- `README.md` (SHA-256 `c403c574fb1dd61160…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
