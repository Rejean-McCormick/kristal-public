# Chemistry — AI authoring improvement review

**State ref:** `urn:kristal:state:chemistry`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Chemical entities and reactions model.

**Scope:** Relate chemical entities, states and reactions under thermodynamic, kinetic and observed conditions.

**Native model:** `multiscale_epistemic_entity_state_process_graph`. ENTITY ↔ STATE ↔ PROCESS, sous conditions thermodynamiques, cinétiques et observations ; processus de réaction potentiellement cycliques

**Non-equivalence to preserve:** A possible reaction is not evidence that it occurred.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: A possible reaction is not evidence that it occurred.
2. **Native Contract** [high]: Separate recorded observations, formal results, interpretations and hypotheses; require a source or proof artifact for any claim of mathematical or logical validity.
3. **Source Provenance** [normal]: Review the 32 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.

## 3. Present classifications, not approvals

- Arketype: **Multiplex / Organizational Model** (`ARK-09`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Chemical sciences**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 12 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 32 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `17952f5c154f256b16…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `eb76a3207343eb5de9…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `6e139ee2201ebe87ac…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `e307f9b2b28f018b4a…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `db88373af7ddad39f8…`)
- `docs/06_VALIDATION.md` (SHA-256 `eac9f2ae3df9a058db…`)
- `README.md` (SHA-256 `49f73b6f2f819079ed…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
