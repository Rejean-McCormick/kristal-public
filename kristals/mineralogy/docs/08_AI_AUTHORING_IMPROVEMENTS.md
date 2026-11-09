# Mineralogy — AI authoring improvement review

**State ref:** `urn:kristal:mineralogy:state`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Mineral classification and structure.

**Scope:** Connect chemical composition, crystal structures, mineral identities, properties and occurrences.

**Native model:** `composition_structure_property_occurrence_graph`. composition chimique + structure cristalline → identité minérale → propriétés → occurrences

**Non-equivalence to preserve:** A measured property alone does not define a mineral species.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: A measured property alone does not define a mineral species.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 7 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Nature Taxonomy as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: evaluate alternative ARK-15 only as a question; A historical AI alternative suggested Hybrid Composition; source-centered mineral identity and crystallography may support retaining ARK-17.

## 3. Present classifications, not approvals

- Arketype: **Taxonomy / Natural Classification** (`ARK-17`), declared; not independently approved.
- Usage PRF: **Nature Taxonomy** (`PRF-03`), declared; not independently approved.
- UNESCO: **Earth sciences; Chemical sciences**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 12 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 7 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `b24a620fc0d7f39737…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `da0837f89920803d32…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `4df597efa63e4d59c0…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `559f97eb33fef8b06c…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `fa87ba4b3b107f2e5e…`)
- `docs/06_VALIDATION.md` (SHA-256 `946fa864d71d18a799…`)
- `README.md` (SHA-256 `0563d5826d7a63c401…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
