# Infrastructure — AI authoring improvement review

**State ref:** `urn:kristal:state:infrastructure`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Infrastructure dependencies and service state.

**Scope:** Map infrastructure topology, capacity, service, dependencies, failure modes and resilience.

**Native model:** `physical-service-network-resilience-graph`. Native model declared by the historical v9 domain-state logical artifact; not replaced with a universal schema.

**Non-equivalence to preserve:** Designed redundancy is not proof of current availability.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: Designed redundancy is not proof of current availability.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 9 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [high]: PRF: RETAIN_DECLARED. Earlier alternative PRF-04 is an **unapproved hypothesis**. The native resilience graph models service dependencies; physical integrity and service availability are explicitly distinct. No evidence of deployed, live multi-system monitoring was verified. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Multiplex / Organizational Model** (`ARK-09`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Equipment and facilities; Civil, military, and mining engineering**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 14 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 9 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `bb81182ca88482f04c…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `d2f40118cb2b325136…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `e3d7dec5c098b1ccf8…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `8a38da094308ee9df0…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `13ed993aeb0cdf939b…`)
- `docs/06_VALIDATION.md` (SHA-256 `4783a85ab88a7c3077…`)
- `README.md` (SHA-256 `da50667384cc63aec3…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
