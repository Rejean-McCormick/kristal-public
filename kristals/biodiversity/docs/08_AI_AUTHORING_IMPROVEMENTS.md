# Biodiversity — AI authoring improvement review

**State ref:** `urn:kristal:state:biodiversity`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Biodiversity observation and taxonomy.

**Scope:** Connect taxon concepts with spatial, temporal and evidence contexts for occurrence and diversity assessments.

**Native model:** `taxon_space_time_evidence_observation_graph`. taxon concept × spatial support × temporal support × evidence/provenance → occurrence, abondance, diversité, évaluation de menace

**Non-equivalence to preserve:** An occurrence report is not a complete biodiversity inventory.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: An occurrence report is not a complete biodiversity inventory.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 12 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Nature Taxonomy as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.

## 3. Present classifications, not approvals

- Arketype: **Taxonomy / Natural Classification** (`ARK-17`), declared; not independently approved.
- Usage PRF: **Nature Taxonomy** (`PRF-03`), declared; not independently approved.
- UNESCO: **Biology; Environmental sciences and engineering**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 12 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 12 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `e8d4f3e242d74e7913…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `740ca0e4eacbf185a0…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `1ef59dbb0e9c34df02…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `45ec31bf1dbb1b3a7c…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `2c037b1a4cad4101f5…`)
- `docs/06_VALIDATION.md` (SHA-256 `7a37ec2cd85b5ad317…`)
- `README.md` (SHA-256 `8c37a51759e4abcdac…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
