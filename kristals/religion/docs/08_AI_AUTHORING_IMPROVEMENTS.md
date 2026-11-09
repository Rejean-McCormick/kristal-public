# Religion — AI authoring improvement review

**State ref:** `urn:kristal:state:religion`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Comparative religion and practices.

**Scope:** Preserve traditions, beliefs, texts, transmission, practice, institutions and communities.

**Native model:** `comparative_multilayer_tradition_practice_graph`. Modèle comparatif tradition/croyance/texte/transmission/pratique/institution/communauté non linéaire.

**Non-equivalence to preserve:** Beliefs must be attributed without declaring one tradition authoritative.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: Beliefs must be attributed without declaring one tradition authoritative.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 18 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Traditions and Mythology Collection as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Layered Interpretations** (`ARK-12`), declared; not independently approved.
- Usage PRF: **Traditions and Mythology Collection** (`PRF-08`), declared; not independently approved.
- UNESCO: **Religion**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 13 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 18 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `ece8b6cad8f3f9d803…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `68b9ccad5359dad656…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `746991c34c3e326a0d…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `9ff37f0ebba39c0ede…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `d606f7cd5966c1ef4d…`)
- `docs/06_VALIDATION.md` (SHA-256 `7e1eec162d35e58bd2…`)
- `README.md` (SHA-256 `65a3a09c5ca3350d67…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
