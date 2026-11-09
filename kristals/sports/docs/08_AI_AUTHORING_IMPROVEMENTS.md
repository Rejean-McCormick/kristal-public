# Sports — AI authoring improvement review

**State ref:** `urn:kristal:state:sports`  
**Workspace status:** `building`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Sport competition and event model.

**Scope:** Connect rules, participants, actions, results, matches and tournament structures.

**Native model:** `typed_sport_rules_competition_graph`. règle → participant → action → événement → résultat → compétition. Cet axe est un ordre de lecture, pas une chronologie ; action ≠ événement arbitré ≠ résultat agrégé.

**Non-equivalence to preserve:** An event record and a competition rule have different authority.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: An event record and a competition rule have different authority.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 11 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Build State** [high]: Workspace reports status=building. Do not promote to validated or released until its local Kit check, domain tests, v9 build and independent qualification evidence pass.

## 3. Present classifications, not approvals

- Arketype: **Event Ledger / Chronology** (`ARK-11`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Leisure**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 12 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 11 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `b40ab09b50bb14276d…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `4d67dea7d9df91e84e…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `c88469155e456a1d01…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `52d0b1dddeaf40cb03…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `a7829eda9bb5d5b45e…`)
- `docs/06_VALIDATION.md` (SHA-256 `95343189fa70e942b1…`)
- `README.md` (SHA-256 `f840ac4749f9db881d…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
