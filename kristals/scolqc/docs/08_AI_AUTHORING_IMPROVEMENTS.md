# ScolQc — Éducation Québec — AI authoring improvement review

**State ref:** `urn:kristal:state:education-quebec`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Quebec education rules and pathways.

**Scope:** Map education sectors, curriculum, progression, admission, regulations and dated conditions in Quebec.

**Native model:** `temporal-jurisdictional-education-rule-transition-curriculum-admission-source-governance-graph`. Graphe éducatif québécois typé et temporel, avec règles, transitions conditionnelles, curriculum, admission, provenance et gouvernance des sources.

**Non-equivalence to preserve:** A documented rule must be checked for current applicability.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: A documented rule must be checked for current applicability.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 122 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [high]: PRF: retain School System and Rules Mapping as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: KEEP_DECLARED_WITH_SECONDARY_SCOPE_REVIEW. Earlier scan candidate "Politics and government" is not adopted. Institutional jurisdiction shapes school rules but educational systems and curriculum remain the scope. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Learning Path** (`ARK-10`), declared; not independently approved.
- Usage PRF: **School System and Rules Mapping** (`PRF-19`), declared; not independently approved.
- UNESCO: **Educational systems and levels; Curriculum**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 4 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 122 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `899a667706a9b07965…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `c3f761c48961de8b9c…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `7be14afe1975027ca7…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `492232fcf9f2078be7…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `f5355b4aed9e004d70…`)
- `docs/06_VALIDATION.md` (SHA-256 `f55dede639e43d3d7a…`)
- `README.md` (SHA-256 `8dd6e1b140137b0fd6…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
