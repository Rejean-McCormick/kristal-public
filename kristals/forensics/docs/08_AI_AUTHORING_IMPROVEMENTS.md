# Forensics — AI authoring improvement review

**State ref:** `urn:kristal:state:forensics`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Forensic trace-to-interpretation chain.

**Scope:** Separate trace acquisition, analysis, comparison, interpretation and bounded conclusions.

**Native model:** `evidence_workflow_typed_graph`. Trace, acquisition, analyse, comparaison, interprétation et conclusion limitée.

**Non-equivalence to preserve:** A forensic inference is not proof of responsibility.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: A forensic inference is not proof of responsibility.
2. **Native Contract** [high]: Review transition guards, prerequisites, exception paths and actor authority; do not equate a documented procedure with permission to execute it.
3. **Source Provenance** [normal]: Review the 12 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: evaluate alternative ARK-08 only as a question; Trace-to-interpretation structure may warrant a Causal Diagnosis supporting view, but forensic interpretation is not itself causation.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Semantic Reference** (`ARK-01`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Scientific approach; Legal systems**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 1 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 12 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `55f491e652eb86b120…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `e52bb754e47df3e397…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `cb6b76e306e9b7cadf…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `41ab46d4df7bc67d6b…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `19922084cc44ad2eab…`)
- `docs/06_VALIDATION.md` (SHA-256 `529047c9b1d7d17632…`)
- `README.md` (SHA-256 `1cc3465fca8a6b4b54…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
