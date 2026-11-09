# Architecture — AI authoring improvement review

**State ref:** `urn:kristal:architecture:state`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Built-environment design model.

**Scope:** Connect site, building programme, space, envelope, structure, use and performance over time.

**Native model:** `iterative_built_environment_graph`. Site/contexte → programme → espace → enveloppe → structure → usage, avec performance/temps

**Non-equivalence to preserve:** Design intent and measured building performance are distinct.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: Design intent and measured building performance are distinct.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 9 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Multiplex / Organizational Model** (`ARK-09`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Human settlements and land use; Civil, military, and mining engineering**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 10 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 9 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `222f1c3a0f342c2efa…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `beb80f2290aff55ad6…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `24a2673a3e9bc3e889…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `0ad28731458791870c…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `c4e88ed9c224ef9875…`)
- `docs/06_VALIDATION.md` (SHA-256 `6adc79cbf837950de5…`)
- `README.md` (SHA-256 `7f268da7ad65d1100e…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
