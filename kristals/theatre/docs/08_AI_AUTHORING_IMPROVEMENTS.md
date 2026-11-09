# Theatre — AI authoring improvement review

**State ref:** `urn:kristal:state:theatre`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Theatre works and performances.

**Scope:** Relate scripts, characters, scenes, staging, performances and interpretative records.

**Native model:** `theatrical_work_performance_graph`. Œuvre/texte → personnages et scènes → mise en scène → représentation, documentation et interprétation.

**Non-equivalence to preserve:** A script and a specific performance are separate artifacts.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: A script and a specific performance are separate artifacts.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 8 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.

## 3. Present classifications, not approvals

- Arketype: **Media and Creative Universes** (`ARK-13`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Performing arts**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 12 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 8 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `f5617291ae1527776c…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `34787d56a4c8710043…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `8b448dd0e89ccde654…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `e206818c46ae3ae2b7…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `146a55e1ee6a2eb4fa…`)
- `docs/06_VALIDATION.md` (SHA-256 `b3c17c9190f7763416…`)
- `README.md` (SHA-256 `1c04764733ec2e0ace…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
