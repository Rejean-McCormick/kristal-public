# Paleontology — AI authoring improvement review

**State ref:** `urn:kristal:state:paleontology`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Fossils and deep-time inference model.

**Scope:** Connect fossil observations to strata, age estimates, ancient organisms and reconstructed lineages.

**Native model:** `provenance_bearing_evidence_inference_graph`. Chaîne d’inférences fossiles, organismes, strates, âges, environnements et lignées avec séparation observation et inférence.

**Non-equivalence to preserve:** A fossil observation and reconstruction of life history are different evidence levels.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: A fossil observation and reconstruction of life history are different evidence levels.
2. **Native Contract** [high]: Exercise typed edges and multi-axis navigation: preserve relation direction, scope and authority; do not collapse a multiplex graph into a single mandatory hierarchy.
3. **Source Provenance** [normal]: Review the 14 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [high]: PRF: REJECT_ALTERNATIVE. Earlier alternative PRF-03 is an **unapproved hypothesis**. The native model is a provenance-bearing fossil evidence-to-inference graph; it should not be recast as primarily a natural taxonomic catalog. | UNESCO: REJECT_UNSUPPORTED_SUGGESTION. Earlier scan candidate "Teaching and training" is not adopted. Paleontology centers on fossils, strata, ages and inferred ancient life; education is not the primary subject. | ARK: retain existing declared native archetype pending structured evidence and human acceptance.

## 3. Present classifications, not approvals

- Arketype: **Research Memory** (`ARK-06`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Earth sciences; Biology**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 12 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 14 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `66f20d330a34991f27…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `f3127f340be9344df4…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `e411989260ab790ffb…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `bdc18aeabb56e22173…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `d606f7cd5966c1ef4d…`)
- `docs/06_VALIDATION.md` (SHA-256 `00c4b6a035ce61be1c…`)
- `README.md` (SHA-256 `c6ec606b57f3c59c46…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
