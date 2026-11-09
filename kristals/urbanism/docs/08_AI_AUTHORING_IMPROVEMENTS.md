# Urbanism — AI authoring improvement review

**State ref:** `urn:kristal:state:kristal-urbanism`  
**Workspace status:** `building`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Urban planning and land-use model.

**Scope:** Describe parcels, neighborhoods, urban form, density, land use, infrastructure and mobility.

**Native model:** `multiscale_spatial_urban_graph`. Parcelle, quartier, ville, réseau, forme urbaine, densité, usage et mobilité.

**Non-equivalence to preserve:** Planning intentions are not existing urban conditions.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: Planning intentions are not existing urban conditions.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 10 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Build State** [high]: Workspace reports status=building. Do not promote to validated or released until its local Kit check, domain tests, v9 build and independent qualification evidence pass.
6. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Multiplex / Organizational Model** (`ARK-09`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Human settlements and land use**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 9 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 10 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `77aba7c7cd56195b6c…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `22ae874b3600f87c45…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `29c55e1329ff53fb00…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `2ad4c241326c67b1af…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `028142e564620fcd29…`)
- `docs/06_VALIDATION.md` (SHA-256 `f0c85c57dcb552226d…`)
- `README.md` (SHA-256 `9eba513f3ac03a930f…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
