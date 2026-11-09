# Ecology — AI authoring improvement review

**State ref:** `urn:kristal:state:kristal-ecology`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Ecological interactions across scales.

**Scope:** Represent organisms, populations, communities and ecosystems through interaction networks and processes.

**Native model:** `scaled_ecological_interaction_process_network`. scaled ecological interaction/process network

**Non-equivalence to preserve:** Observed co-occurrence alone does not prove ecological dependence.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: Observed co-occurrence alone does not prove ecological dependence.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 18 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Multiplex / Organizational Model** (`ARK-09`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Environmental sciences and engineering; Biology**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 9 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 18 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `4bcea34e36b710e625…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `241be2e948b9f589e0…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `3b7c696f3e89d9a8fd…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `88498ed7b33854cfbd…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `0167cd97b36a80aea6…`)
- `docs/06_VALIDATION.md` (SHA-256 `0e6d45e6386286433b…`)
- `README.md` (SHA-256 `6c0cd45199fac9cfaf…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
