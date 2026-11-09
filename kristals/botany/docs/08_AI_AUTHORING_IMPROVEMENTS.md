# Botany — AI authoring improvement review

**State ref:** `urn:kristal:state:botany`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Plant structures and taxonomy.

**Scope:** Organize plant organs, tissues, functions, development, reproduction, classification and environmental responses.

**Native model:** `land_plant_architecture_function_graph`. architecture des Embryophyta : organes, tissus, fonctions, croissance, reproduction, taxonomie et réponses à l’environnement

**Non-equivalence to preserve:** A plant classification must keep its evidence and taxonomic scope.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: A plant classification must keep its evidence and taxonomic scope.
2. **Native Contract** [high]: Test the identity and rank boundaries: a class, an observed instance and a taxonomic assertion must not be conflated; document disputed or time-sensitive classifications.
3. **Source Provenance** [normal]: Review the 21 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Nature Taxonomy as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Taxonomy / Natural Classification** (`ARK-17`), declared; not independently approved.
- Usage PRF: **Nature Taxonomy** (`PRF-03`), declared; not independently approved.
- UNESCO: **Biology**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 1 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 21 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `463083e9f99fb2aea3…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `fbe7852b9081c2f2fe…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `c488e0952e57cb6571…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `fad5907947e8d8a0c7…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `05e650441c360703b9…`)
- `docs/06_VALIDATION.md` (SHA-256 `99183560595e561a1c…`)
- `README.md` (SHA-256 `5500d6c05fa645a75b…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
