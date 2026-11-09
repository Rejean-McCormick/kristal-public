# Manufacturing — AI authoring improvement review

**State ref:** `urn:kristal:state:manufacturing`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Manufacturing process and quality model.

**Scope:** Connect raw materials, processes, geometry, tolerances, manufactured parts and quality controls.

**Native model:** `traceable_process_measurement_dag`. Matière brute, procédé, géométrie, tolérance, pièce et contrôle qualité

**Non-equivalence to preserve:** A procedure specification is not evidence of a conforming part.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: A procedure specification is not evidence of a conforming part.
2. **Native Contract** [high]: Audit the unit, method, time, locale/reference frame and applicability attached to every value; do not merge contextual observations into universal facts.
3. **Source Provenance** [normal]: Review the 17 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [high]: PRF: EXPLORE_SECONDARY_NOT_PRIMARY. Earlier alternative PRF-02 is an **unapproved hypothesis**. The source has a manufacturing process DAG and quality constraints. A procedural usage profile would require an actual authorized stepwise protocol, roles, conditions and exception outcomes, not merely a flow model. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Procedure / Protocol** (`ARK-04`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Industry; Manufacturing and transport engineering**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 1 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 17 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `096bccf3d9066d3ef4…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `477e4f5be804bb19c7…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `b43be75ad247313e04…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `7e31136331651d5c75…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `8da358a4dc1adb4b06…`)
- `docs/06_VALIDATION.md` (SHA-256 `ca1e7002c285918fdd…`)
- `README.md` (SHA-256 `761563a34b3893b56f…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
