# Pharmacology — AI authoring improvement review

**State ref:** `urn:kristal:state:pharmacology`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Drug exposure and response mechanisms.

**Scope:** Connect substances, targets, pharmacokinetics, pharmacodynamics, effects, exposures and risks.

**Native model:** `pharmacology_exposure_mechanism_risk_graph`. Graphe mécanistique substance/cible/exposition/effet/risque, distinguant PK, PD et unités d’exposition.

**Non-equivalence to preserve:** Mechanistic reference does not justify individual prescriptions.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: Mechanistic reference does not justify individual prescriptions.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 19 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Semantic Reference** (`ARK-01`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Medical sciences**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 9 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 19 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `6a959abad5170a2e25…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `7204ebdfa36a7090b5…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `885f1e021d0bd2198f…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `3ac3333da7d9cd369b…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `d606f7cd5966c1ef4d…`)
- `docs/06_VALIDATION.md` (SHA-256 `00dafc1214c9bf6570…`)
- `README.md` (SHA-256 `7dd73a9bceca136da1…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
