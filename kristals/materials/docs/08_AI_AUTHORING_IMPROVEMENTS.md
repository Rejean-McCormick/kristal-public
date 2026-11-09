# Materials — AI authoring improvement review

**State ref:** `urn:kristal:state:materials`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Materials structure and properties reference.

**Scope:** Relate material composition and structure to properties, tests, states and applications.

**Native model:** `condition_scoped_material_property_graph`. Structure, propriété, comportement, usage, méthode de mesure et état du matériau

**Non-equivalence to preserve:** A test value must retain conditions and method provenance.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: A test value must retain conditions and method provenance.
2. **Native Contract** [high]: Audit the unit, method, time, locale/reference frame and applicability attached to every value; do not merge contextual observations into universal facts.
3. **Source Provenance** [normal]: Review the 10 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Semantic Reference** (`ARK-01`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Materials and products; Chemical sciences**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 9 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 10 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `5d6de2b9fb74c3ece5…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `c1d537f46db08a2148…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `dab3a0bbd067b74fb4…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `809066eed5b7c0c659…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `2d9fc5fc1a569f8b4c…`)
- `docs/06_VALIDATION.md` (SHA-256 `929298bc91364e4c44…`)
- `README.md` (SHA-256 `0f5472edd9d80d23e1…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
