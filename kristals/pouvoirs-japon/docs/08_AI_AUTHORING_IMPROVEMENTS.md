# Pouvoirs-Japon — AI authoring improvement review

**State ref:** `urn:kristal:state:pouvoirs-japon`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Japanese state powers map.

**Scope:** Represent Japanese institutions, public powers, scope, checks and dated sources.

**Native model:** `jurisdictional_legal_power_relational_graph`. Graphe d’assertions juridico-institutionnelles typées et sourcées : institutions, fonctions, compétences, normes, limitations, recours et contrôles ; contextualisé par juridiction et temporalité.

**Non-equivalence to preserve:** Comparisons across countries must not erase legal differences.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: Comparisons across countries must not erase legal differences.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 16 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Contextual Social Organizations as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Multiplex / Organizational Model** (`ARK-09`), declared; not independently approved.
- Usage PRF: **Contextual Social Organizations** (`PRF-09`), declared; not independently approved.
- UNESCO: **Politics and government; Legal systems**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 1 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 16 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `f8e92e30282cd6dcb2…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `5b96ff106630f2f7e8…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `160d3be822f324cb61…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `3ac83b3c657866cd1c…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `e7ba190b12cea888f2…`)
- `docs/06_VALIDATION.md` (SHA-256 `737ec8261df2e484da…`)
- `README.md` (SHA-256 `bb59877b4a23374509…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
