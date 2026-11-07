# Zoology — AI authoring improvement review

**State ref:** `urn:kristal:state:kristal-zoology`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Animal taxonomy and adaptations.

**Scope:** Relate lineages, body plans, adaptation, convergence and uncertainty in animal classification.

**Native model:** `lineage_dag_body_plan_adaptation_graph`. lignée ↔ plan corporel ↔ adaptation ; convergence et incertitude. Fonction similaire ≠ homologie ; convergence ≠ origine commune ; incertitude ≠ négation ; la lignée forme un DAG éditorial.

**Non-equivalence to preserve:** Similar function does not prove common ancestry.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: Similar function does not prove common ancestry.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 6 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Nature Taxonomy as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.

## 3. Present classifications, not approvals

- Arketype: **Taxonomy / Natural Classification** (`ARK-17`), declared; not independently approved.
- Usage PRF: **Nature Taxonomy** (`PRF-03`), declared; not independently approved.
- UNESCO: **Biology**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 12 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 6 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `b0453ac0d67b28833f…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `4cc144f049698df203…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `9be99f577117c49ddb…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `891db0790d54cd1294…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `9fc0c89e55e62a4bc5…`)
- `docs/06_VALIDATION.md` (SHA-256 `287b893f8576e7db23…`)
- `README.md` (SHA-256 `f5a9dfc444cf631466…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
