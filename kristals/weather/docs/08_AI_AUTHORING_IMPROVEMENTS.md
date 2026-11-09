# Weather — AI authoring improvement review

**State ref:** `urn:kristal:state:kristal-weather`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Weather observation and forecast model.

**Scope:** Connect atmospheric observations, current states, analyses, forecasts, hazards and uncertainty.

**Native model:** `dynamic_atmospheric_state_graph`. État atmosphérique, forçages, structures, observation, analyse, prévision et risques.

**Non-equivalence to preserve:** Observed weather and forecast weather must remain distinct.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: Observed weather and forecast weather must remain distinct.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 23 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [high]: PRF: EXPLORE_SECONDARY_NOT_PRIMARY. Earlier alternative PRF-04 is an **unapproved hypothesis**. Weather includes time-indexed observations, analyses and forecasts, but no evidence was established of operational station-state tracking meeting the PRF-04 template; observation and forecast are separate. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Multiplex / Organizational Model** (`ARK-09`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Meteorology**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 1 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 23 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `676ad195e9cb68d9ec…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `fd092ac2646f7dd0a3…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `a0dd34c6c4e2464504…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `2ad4c241326c67b1af…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `881f8eb3063ebee67a…`)
- `docs/06_VALIDATION.md` (SHA-256 `c134bf876d01c6c5b3…`)
- `README.md` (SHA-256 `70fd81ec5aee4a7136…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
