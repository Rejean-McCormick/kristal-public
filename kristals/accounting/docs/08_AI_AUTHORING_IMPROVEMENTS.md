# Accounting — AI authoring improvement review

**State ref:** `urn:kristal:accounting:state`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Economic accounting ledger.

**Scope:** Connect economic events, recognition and measurement to dated entries, accounts, periods and financial statements.

**Native model:** `accounting_event_ledger_graph`. Événement économique → reconnaissance/mesure → écriture → compte/livre → période → état financier

**Non-equivalence to preserve:** An accounting entry is not itself the underlying economic event.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: An accounting entry is not itself the underlying economic event.
2. **Native Contract** [high]: Test event ordering and provenance: distinguish event time, recording time, interpretation and any inferred causality; preserve conflicting source accounts.
3. **Source Provenance** [normal]: Review the 10 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: evaluate alternative ARK-11 only as a question; Accounting is event- and period-oriented; examine whether Event Ledger / Chronology is more than a supporting structure.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Semantic Reference** (`ARK-01`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Finance and trade**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 2 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 10 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `5b6a89885972deb56b…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `f1cbcaa3515eeafe15…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `85492b998b46349e19…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `2b71bf35c16f813b64…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `0d98b0eaee2cb91ce6…`)
- `docs/06_VALIDATION.md` (SHA-256 `64eab09c3037c6fb6a…`)
- `README.md` (SHA-256 `fd9cca8579841c8b1d…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
