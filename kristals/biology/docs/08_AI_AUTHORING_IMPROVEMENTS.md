# Biology — AI authoring improvement review

**State ref:** `urn:kristal:state:biology`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Multi-scale biological knowledge model.

**Scope:** Relate cells, tissues, organisms and populations through function, reproduction, inheritance and evolution.

**Native model:** `multiscale_biological_organization_graph`. cellule → tissu → organisme → population, avec fonction, reproduction, hérédité et évolution comme processus transversaux

**Non-equivalence to preserve:** Shared biological terminology does not prove identical mechanisms across scales.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: Shared biological terminology does not prove identical mechanisms across scales.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 17 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [high]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: KEEP_DECLARED_REJECT_AUTO_PROMOTION. Earlier scan candidate "Population" is not adopted. Biological populations are not equivalent to a social-science Population microthesaurus; retain Biology. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Multiplex / Organizational Model** (`ARK-09`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Biology**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 9 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 17 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `2d3c8af236eada3dc1…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `5ec037bafede2c0d34…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `2ad569625c0e8acfaa…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `47a5fa7d69a3564961…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `dd70b07a6f86c9984a…`)
- `docs/06_VALIDATION.md` (SHA-256 `0c3637839b57235814…`)
- `README.md` (SHA-256 `70f5baa29885bdb091…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
