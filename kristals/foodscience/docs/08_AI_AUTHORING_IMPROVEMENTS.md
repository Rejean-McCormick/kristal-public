# FoodScience — AI authoring improvement review

**State ref:** `urn:kristal:state:foodscience`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Food composition and transformations model.

**Scope:** Connect food matrices, composition, processing, structure, properties, stability and safety considerations.

**Native model:** `food_system_multicontext_graph`. Systèmes alimentaires : matrice, composition, transformation, structure, propriétés et stabilité/sécurité.

**Non-equivalence to preserve:** A modeled transformation is not verified food safety.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: A modeled transformation is not verified food safety.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [high]: The normalized source catalog currently has zero entries. Inspect the historical corpus/sources before proposing any import, never invent source records.
4. **Classification** [normal]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Multiplex / Organizational Model** (`ARK-09`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Industry; Chemical sciences**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 13 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 0 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `64e74904b94326dc59…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `7bad7059740b20822a…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `4146c7a50c2d88ed31…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `e2d653e6229aa2bca9…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `4433febe7ef5184491…`)
- `docs/06_VALIDATION.md` (SHA-256 `3f71906417bc017c50…`)
- `README.md` (SHA-256 `ef8581bb2efc6bad3b…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
