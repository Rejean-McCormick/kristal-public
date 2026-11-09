# HomeCare — AI authoring improvement review

**State ref:** `urn:kristal:state:homecare`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Home-care services and contexts model.

**Scope:** Organize service roles, resources, care contexts and structured follow-up records without merging authorities.

**Native model:** `property-functional-diagnostic-temporal-graph`. Native model declared by the historical v9 domain-state logical artifact; not replaced with a universal schema.

**Non-equivalence to preserve:** Home-care reference is not an individual patient's medical record or authorization.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: Home-care reference is not an individual patient's medical record or authorization.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [high]: The normalized source catalog currently has zero entries. Inspect the historical corpus/sources before proposing any import, never invent source records.
4. **Classification** [normal]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: evaluate alternative ARK-19 only as a question; A casefile/follow-up structure appears in historical review notes, but do not infer a real individual casefile or consent.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Hybrid Composition** (`ARK-15`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Services; Family**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 2 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 0 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `ef5a872ac35fc9ebf3…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `9020d1699d163dd984…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `a6163b3add9728a214…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `2a61150f428ce57193…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `8ecaf8a62b3cba7857…`)
- `docs/06_VALIDATION.md` (SHA-256 `ae05d2153dd5e2ac0c…`)
- `README.md` (SHA-256 `b47576ad4913acd52e…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
