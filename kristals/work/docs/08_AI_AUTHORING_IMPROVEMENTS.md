# Work — AI authoring improvement review

**State ref:** `urn:kristal:state:kristal-work`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Work activities and competences model.

**Scope:** Relate activities, skills, roles, occupations, work environments and outcomes.

**Native model:** `many_to_many_work_activity_skill_graph`. activité ↔ compétence ↔ rôle ↔ métier ↔ environnement → résultat. Rôle ≠ métier, activité ≠ compétence, poste ≠ occupation ; classification datée et rapports plusieurs-à-plusieurs.

**Non-equivalence to preserve:** A role label is not proof of individual competence.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: A role label is not proof of individual competence.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [high]: The normalized source catalog currently has zero entries. Inspect the historical corpus/sources before proposing any import, never invent source records.
4. **Classification** [high]: PRF: retain Multi-Purpose Semantic Reference as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: REJECT_UNSUPPORTED_SUGGESTION. Earlier scan candidate "Information technology (software)" is not adopted. Work activities, skills, roles and employment conditions are not primarily software engineering. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Multiplex / Organizational Model** (`ARK-09`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Labour; Personnel management**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 9 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 0 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `64edde9422d5e14901…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `d7f533aa47b8992be2…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `fa4a0b5f4175e46577…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `9dd5aba1536c78983d…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `8434223aa9125d7d72…`)
- `docs/06_VALIDATION.md` (SHA-256 `33515e7d83e1765cc2…`)
- `README.md` (SHA-256 `6beed7333b60f92aad…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
