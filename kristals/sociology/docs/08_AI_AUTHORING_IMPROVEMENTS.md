# Sociology — AI authoring improvement review

**State ref:** `urn:kristal:state:sociology`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Sociological roles and institutions.

**Scope:** Relate individuals, interactions, groups, roles, social norms, institutions and networks.

**Native model:** `multiscale_social_network_graph`. individus ↔ interactions ↔ groupes ↔ rôles ↔ institutions ↔ normes ↔ réseaux. Le parcours micro/méso/macro est une navigation multi-échelle, et non une chaîne causale.

**Non-equivalence to preserve:** A social model must preserve context and avoid universalizing groups.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: A social model must preserve context and avoid universalizing groups.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 18 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Contextual Social Organizations as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Multiplex / Organizational Model** (`ARK-09`), declared; not independently approved.
- Usage PRF: **Contextual Social Organizations** (`PRF-09`), declared; not independently approved.
- UNESCO: **Social sciences; Social systems**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 9 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 18 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `7051f4cd7d7c7af2f3…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `d2f384059659e1dd05…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `8dbfcbeb8edc1451e6…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `47955a711522e0cf2b…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `bcc68631374277b60f…`)
- `docs/06_VALIDATION.md` (SHA-256 `ebeac2fa07afa8ff8d…`)
- `README.md` (SHA-256 `6444f467ad2250481d…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
