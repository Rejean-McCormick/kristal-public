# AI Context — VaticanOps

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:vaticanops`
- State Logical Commitment: `sha256:0af3674eef560da6d3e91f56d12feca3b0dc0b56447b13ec1c314dc8dc7a4575`
- Workspace profile: `procedural`
- Native model: `procedure_graph_conditionnelle`
- Canonical artifacts: `22`
- Sources: `6`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intent and scope

VaticanOps represents **8 curated public-procedure summaries** mapped to the provided six Vatican publications. It supports navigation and audit, not legal advice, institutional authority or task execution. This is a deliberately partial corpus; more article-level review is needed for completeness.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Semantic boundary

- **Owns:** editor-defined procedure and step identifiers VO-PXX, source-linked transition descriptions, project labels, statuses.
- **External authority:** each publication originates from the referenced Vatican URL and its own rules and validity; the project does not own or interpret that authority conclusively.
- **Does not own:** people, cases, discipline records, papal authority, civil/Vatican State laws or confidential documents.
- **Never equate:** Holy See, Roman Curia, Latin Church and Vatican City State.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Native model — ARK-04

`canon/domain/vaticanops.procedures.json`: each procedure has an entry description, conditional nodes and guarded edges, role labels, scope, caveats, evidence references, and editor/authority metadata. Some branches have no executable resolution and should remain descriptive. A `kind=outcome` node is not a recorded event. Graph edges do not grant permission.

Other logical artifacts: `canon/epistemic/vaticanops.passage-evidence.json` (digest-bound text anchors) and `canon/domain/vaticanops.taxonomy.json` (controlled scope vocabulary). `derived/source-units.json` indexes available source divisions, not a normative graph.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Epistemics

All nodes: `source_mapped_unreviewed`; all procedures: `source_mapped_editorial_draft`; legal applicability: `not_legally_reviewed`. An identified article proves attribution to a captured version, not authoritative interpretation or current force of law. No promotion to reviewed without an independent record of review.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonical and derived

The three files registered in `canon/state.index.json` are the sole editorial logical content commitments in this initial version. `sources/DocVatican` stores externally obtained physical files, `sources/source-inventory.json` documents their hashes; these are not promoted as canonical normative claims. `derived/`, `ai/`, `build/` and `.kristal/v9/` are build/read artifacts.
