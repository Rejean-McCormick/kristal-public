# Maritime — AI authoring improvement review

**State ref:** `urn:kristal:state:maritime`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Maritime navigation and operations model.

**Scope:** Connect vessels, marine environments, routes, cargo and operational contexts.

**Native model:** `sparse_multiplex_relational_graph`. Navire × environnement marin × navigation × opérations et cargaison

**Non-equivalence to preserve:** A documented navigation model does not authorize a voyage.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: A documented navigation model does not authorize a voyage.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 13 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Multiplex / Organizational Model** (`ARK-09`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Manufacturing and transport engineering; Geography and oceanography**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 13 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 13 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `0e438ffe3c1efbc596…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `e98dfb1f9aac2d5392…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `804a54de7de6b0c774…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `6d880fca59eec7ad77…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `39d49b3aaa09da310a…`)
- `docs/06_VALIDATION.md` (SHA-256 `134e75eaa37260bf54…`)
- `README.md` (SHA-256 `816c1413bd99e8ac12…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
