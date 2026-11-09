# Forestry — AI authoring improvement review

**State ref:** `urn:kristal:state:forestry`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Forest stands and interventions timeline.

**Scope:** Represent stand states, growth, disturbance, interventions and follow-up over time.

**Native model:** `forest_stand_temporal_transition_model`. Peuplements forestiers, états dans le temps, croissance, perturbations, interventions et suivi.

**Non-equivalence to preserve:** A modeled forest trajectory is not an observed management outcome.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: A modeled forest trajectory is not an observed management outcome.
2. **Native Contract** [high]: Test the declared native shape against its source payloads; preserve typed identities, collections, applicability and evidence rather than converting to a generic untyped table.
3. **Source Provenance** [normal]: Review the 9 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [high]: PRF: RETAIN_DECLARED. Earlier alternative PRF-04 is an **unapproved hypothesis**. The corpus models forest stands and temporal transitions, but the source does not demonstrate an operational monitoring dashboard or observed state tracking required to promote System-State Tracking. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Simulation / Transitions** (`ARK-14`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Agriculture; Natural resources**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 13 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 9 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `3558c3ad77334d4bd7…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `94c6cbf0701ba897da…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `b8fc5f12cfe54ffadc…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `2071e89238e69b8ee0…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `1f7a6fe30465bf215e…`)
- `docs/06_VALIDATION.md` (SHA-256 `e92b30c3af7cb6938b…`)
- `README.md` (SHA-256 `3dec8d402ef76be85b…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
