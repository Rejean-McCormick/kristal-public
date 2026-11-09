# Astronomy — AI authoring improvement review

**State ref:** `urn:kristal:astronomy:state`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Astronomical object reference.

**Scope:** Relate celestial object types to mass, distance, motion, radiation, formation and evolution.

**Native model:** `measurement_contextualized_object_graph`. Type → masse → distance → mouvement → rayonnement → formation → évolution → observation

**Non-equivalence to preserve:** An inferred property is not a direct observation.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: An inferred property is not a direct observation.
2. **Native Contract** [high]: Audit the unit, method, time, locale/reference frame and applicability attached to every value; do not merge contextual observations into universal facts.
3. **Source Provenance** [normal]: Review the 14 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.

## 3. Present classifications, not approvals

- Arketype: **Semantic Reference** (`ARK-01`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Space sciences**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 13 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 14 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `a6e1728adb40bbc020…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `3cf7b5aa0bcaddcaf5…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `d7590030692f3ea54a…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `970d38a1a4773200ac…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `762607b69a256acf36…`)
- `docs/06_VALIDATION.md` (SHA-256 `1aae62857b1969bd93…`)
- `README.md` (SHA-256 `bfe89391b422e080a2…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
