# Finance — AI authoring improvement review

**State ref:** `urn:kristal:state:finance`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Financial rights and valuation model.

**Scope:** Connect dated assets, liabilities, claims, cash flows, risk, returns and valuation.

**Native model:** `financial_claim_temporal_relation_graph`. Actifs et passifs, droits/obligations, flux datés, risque, rendement, mesure et valorisation.

**Non-equivalence to preserve:** Valuation assumptions must not be presented as actual prices or advice.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: Valuation assumptions must not be presented as actual prices or advice.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 11 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Semantic Reference** (`ARK-01`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Finance and trade**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 13 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 11 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `9b7e8d904ee017d214…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `9a7766928c649407dd…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `2fcd2f14c72a10ba13…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `87262db5cfe3c65cc4…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `16fd56d943a794047a…`)
- `docs/06_VALIDATION.md` (SHA-256 `788a9285a0e5a1a3fa…`)
- `README.md` (SHA-256 `3ceb5f385cdebb73fd…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
