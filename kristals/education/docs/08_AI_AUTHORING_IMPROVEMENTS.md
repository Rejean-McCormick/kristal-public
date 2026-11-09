# Education — AI authoring improvement review

**State ref:** `urn:kristal:state:kristal-education`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Learning progression and evidence model.

**Scope:** Relate learner state, objectives, activities, evidence, interpretation and progression decisions.

**Native model:** `learner_objective_activity_evidence_progression_cycle`. learner-state / objective / activity / evidence / progression cycle

**Non-equivalence to preserve:** An educational pathway is not automatically an LMS export or individual school casefile.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: An educational pathway is not automatically an LMS export or individual school casefile.
2. **Native Contract** [high]: Test the declared native shape against its source payloads; preserve typed identities, collections, applicability and evidence rather than converting to a generic untyped table.
3. **Source Provenance** [normal]: Review the 7 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Learning Path** (`ARK-10`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Teaching and training; Curriculum**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 1 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 7 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `4ee9e40014cde7eeb6…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `a6ea9ca31f03e8455a…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `625b1a37bc58905fc2…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `b7068fa758be2dcd71…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `b3ed0863928c9de698…`)
- `docs/06_VALIDATION.md` (SHA-256 `df161a783fafbfacca…`)
- `README.md` (SHA-256 `ad5e427227e4938f58…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
