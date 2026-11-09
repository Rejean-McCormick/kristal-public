# Logic — AI authoring improvement review

**State ref:** `urn:kristal:state:logic`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Formal inference and validity model.

**Scope:** Relate propositions, inference rules, models, validity and proof structures.

**Native model:** `typed_formal_syntax_semantics_proof_graph`. Formes de propositions, règles d’inférence, modèles, validité et preuves logiques

**Non-equivalence to preserve:** Logical validity is different from the truth of premises.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: Logical validity is different from the truth of premises.
2. **Native Contract** [high]: Separate recorded observations, formal results, interpretations and hypotheses; require a source or proof artifact for any claim of mathematical or logical validity.
3. **Source Provenance** [normal]: Review the 8 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Invariant / Formal Theory** (`ARK-07`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Mathematics and statistics; Philosophy and ethics**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 1 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 8 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `26f067ac8936e7360d…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `6edc72688a8b10d630…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `b51ccceb8d62ec27b4…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `8835013f8013d4cb8f…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `33055ede90700c3dab…`)
- `docs/06_VALIDATION.md` (SHA-256 `9983ff2c5f5fbf4f51…`)
- `README.md` (SHA-256 `0d573baa04002883ca…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
