# EngineeringConstraints — AI authoring improvement review

**State ref:** `urn:kristal:state:kristal-engineeringconstraints`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Requirements and verification traceability.

**Scope:** Connect needs, requirements, architectural trade-offs and verification evidence.

**Native model:** `engineering_constraints_traceability_model`. requirements / architecture / tradeoff / verification traceability graph

**Non-equivalence to preserve:** A traced requirement is not necessarily satisfied or approved.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: A traced requirement is not necessarily satisfied or approved.
2. **Native Contract** [high]: Test the declared native shape against its source payloads; preserve typed identities, collections, applicability and evidence rather than converting to a generic untyped table.
3. **Source Provenance** [normal]: Review the 5 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Milestone and Proof Map** (`ARK-03`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Civil, military, and mining engineering; Manufacturing and transport engineering**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 1 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 5 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `afa72cc6d74de0f677…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `5ecde2f594c8ab9e17…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `aa76d51b6e4af1f822…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `d520ad3f35a2c746ca…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `8f4a5ab891b02c378d…`)
- `docs/06_VALIDATION.md` (SHA-256 `3c4b61f8a3174746f1…`)
- `README.md` (SHA-256 `19bbe173df33b0a280…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
