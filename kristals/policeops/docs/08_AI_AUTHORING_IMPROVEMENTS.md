# PoliceOps — AI authoring improvement review

**State ref:** `urn:kristal:state:policeops`  
**Workspace status:** `building`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Versioned police operations protocols.

**Scope:** Track source-bounded procedures, permissions, exceptions and operational reference assertions.

**Native model:** `structured_epistemic_state`. Document JSON natif PoliceOps v5 combinant assertions adressables, source_refs, provenance, statuts épistémiques, reader policies et extensions métier. La normalisation 3.2.2 ne réécrit pas ce payload.

**Non-equivalence to preserve:** A documented procedure does not authorize real-world enforcement.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: A documented procedure does not authorize real-world enforcement.
2. **Native Contract** [high]: Separate recorded observations, formal results, interpretations and hypotheses; require a source or proof artifact for any claim of mathematical or logical validity.
3. **Source Provenance** [normal]: Review the 29 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [normal]: PRF: retain Police Operations Protocols as **declared, unapproved**. Assess usage from actual user tasks and native evidence before replacing a generic PRF. | UNESCO: keep the recorded subject mapping as a **pending semantic review**, not a verified exact concept match. Do not promote keyword-based suggestions automatically. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.
5. **Build State** [high]: Workspace reports status=building. Do not promote to validated or released until its local Kit check, domain tests, v9 build and independent qualification evidence pass.
6. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Procedure / Protocol** (`ARK-04`), declared; not independently approved.
- Usage PRF: **Police Operations Protocols** (`PRF-16`), declared; not independently approved.
- UNESCO: **Politics and government; Legal systems**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 1 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 29 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `e1171dbe61b643dbec…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `421c45114cc416fa1a…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `db9552aa899f2eb02f…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `2b173ba85ae0463457…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `0c86f5e01169a0d64a…`)
- `docs/06_VALIDATION.md` (SHA-256 `238c3a4ab31fca1b23…`)
- `README.md` (SHA-256 `287b1ed5ec0a071f9d…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
