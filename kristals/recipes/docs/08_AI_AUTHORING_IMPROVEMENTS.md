# Recipes — AI authoring improvement review

**State ref:** `urn:kristal:state:recipes`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Structured culinary procedures.

**Scope:** Represent ingredients, transformation steps, variants, timing and explicit versioned recipes.

**Native model:** `procedural_transformation_graph_and_family_variants`. Programmes culinaires de transformation de matière, familles, variantes versionnées, sources et graphes procéduraux.

**Non-equivalence to preserve:** A recipe record is not a guarantee of food safety.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: A recipe record is not a guarantee of food safety.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 13 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Procedural Environment as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Procedure / Protocol** (`ARK-04`), declared; not independently approved.
- Usage PRF: **Procedural Environment** (`PRF-02`), declared; not independently approved.
- UNESCO: **Industry; Leisure**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 1 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 13 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `3ea4a539bc006bed1d…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `69659390e2a7bf06fa…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `1a7d814bc314d46f90…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `258a96b0f0bad3f052…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `b30240497d8135ecdf…`)
- `docs/06_VALIDATION.md` (SHA-256 `c1f3d240c0bf199cb1…`)
- `README.md` (SHA-256 `90c84f07b949fb803b…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
