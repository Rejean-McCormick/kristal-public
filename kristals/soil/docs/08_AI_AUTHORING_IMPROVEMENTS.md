# Soil — AI authoring improvement review

**State ref:** `urn:kristal:state:soil`  
**Workspace status:** `validated`  
**Review:** AI draft, **not accepted** · 2026-11-05  
**Authoring Kit boundary:** local `kristal.local-workspace/3.2.0`; no canonical write, ID allocation, publication or approval.

## 1. Source-grounded semantic orientation

**Purpose:** Soil horizons and properties model.

**Scope:** Connect horizons, texture, chemistry, biology, water, fertility and contextual measurements.

**Native model:** `vertical_soil_profile_process_graph`. horizon → texture → chimie → biologie → eau → fertilité. Une mesure conserve profondeur/horizon, méthode, date, unité et conditions ; horizon génétique ≠ horizon diagnostique ≠ couche d’échantillonnage.

**Non-equivalence to preserve:** A soil observation without depth and method is incomplete.

## 2. Concrete authoring improvements to review

1. **Semantic Boundary** [high]: Check and document an explicit counterexample for this boundary: A soil observation without depth and method is incomplete.
2. **Native Contract** [high]: Audit the unit, method, time, locale/reference frame and applicability attached to every value; do not merge contextual observations into universal facts.
3. **Source Provenance** [normal]: Review the 11 local normalized source-catalog entries against asserted provenance; keep every external authority external.
4. **Classification** [high]: PRF: REJECT_ALTERNATIVE. Earlier alternative PRF-03 is an **unapproved hypothesis**. The primary object is a context-bound vertical soil profile and processes, with measurements by depth and method. Soil classifications are one dimension, not proof that taxonomic catalog usage is primary. | UNESCO: KEEP_DECLARED_WITH_SECONDARY_SCOPE_REVIEW. Earlier scan candidate "Biology" is not adopted. Soil biology is part of the model, but pedology and agriculture remain central; any Biology tag needs source-specific justification. | ARK: evaluate alternative ARK-09 only as a question; The primary vertical profile and interacting processes may be more multiplex than taxonomic; preserve declared ARK-17 until human content review.
5. **Read Model** [normal]: Portable AI index not observed. Before enabling any read model, use the installed Kit build/check-ai workflow; do not author a stand-alone AI manifest or infer canon from the review dossier.

## 3. Present classifications, not approvals

- Arketype: **Taxonomy / Natural Classification** (`ARK-17`), declared; not independently approved.
- Usage PRF: **Multi-Purpose Semantic Reference** (`PRF-20`), declared; not independently approved.
- UNESCO: **Earth sciences; Agriculture**, declared, semantic review pending.

## 4. Evidence and reviewer acceptance conditions

- 1 registered canonical artifact path(s) exist in the supplied snapshot. No canonical payload is modified by this review.
- 11 normalized catalog source record(s); a zero count calls for historical-source inspection, not fabricated evidence.
- AI read index currently not present; this review is not a replacement for a generated portable AI read layer.
- Kit command `build-discovery` not available in the bundled local tools; do not copy newer Kit executables into this workspace silently.

**Before accepting an actual canonical change:** identify the authority and source claim, preserve existing KQ/KP/KA/KS and state identities, update through the Kit authoring workflow, run project-specific domain validation plus the appropriate Kit `check` / build sequence, compare logical commitments and obtain independent qualification. Do not publish or activate without a separate authorization.

## 5. Source anchors in this snapshot

- `docs/00_INTENT_AND_SCOPE.md` (SHA-256 `be88ec71ebaedbeca3…`)
- `docs/01_SEMANTIC_BOUNDARY.md` (SHA-256 `1571561f39c9cd9ca7…`)
- `docs/02_NATIVE_MODEL.md` (SHA-256 `bf560ea0f6908c39c2…`)
- `docs/03_EPISTEMIC_MODEL.md` (SHA-256 `18a96093857e3e2ebe…`)
- `docs/04_CANONICAL_DERIVED.md` (SHA-256 `0fdc9dcb5e704980d2…`)
- `docs/06_VALIDATION.md` (SHA-256 `71978d0b4943e540ac…`)
- `README.md` (SHA-256 `8f21418fb74d5b4de1…`)

**Machine-readable review:** `derived/authoring-review/AI_EDITORIAL_DOSSIER.json`. Input SHA-256 anchors are embedded there. If a source changes, re-review its conclusions.
