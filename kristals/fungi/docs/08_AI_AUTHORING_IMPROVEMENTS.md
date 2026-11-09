# Fungi — AI authoring improvement review

**State ref:** `urn:kristal:state:fungi`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Fungal taxonomy and life cycles.

**Scope:** Organize fungal structures, mycelia, networks, interactions and reproductive cycles.

**Native model:** `fungal_network_and_lifecycle_graph`. Organisation fongique, mycélium, réseaux, interactions écologiques et cycles de vie.

**Non-equivalence to preserve:** Species classification and ecological function are distinct questions.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: Species classification and ecological function are distinct questions.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 10 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Nature Taxonomy as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.

## 3. Present classifications, not approvals

- Arketype: **Taxonomy / Natural Classification** (`ARK-17`), declared; not independently approved.
- Usage PRF: **Nature Taxonomy** (`PRF-03`), declared; not independently approved.
- UNESCO: **Biology**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 12 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 10 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `091ebfaa9a328b38d9…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `299f9abb0d633a5c3d…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `35712baf3089f8f9d3…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `fecfe21cc8ee60e2ab…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `7bd53c569a76a24bc8…`)
- `docs/06_VALIDATION.md` (SHA-256 `aa13a67c817e3e8255…`)
- `README.md` (SHA-256 `ac51c3e646aeda48cf…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
