# AI Context — kOA Ecosystem

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:koa-ecosystem:state`
- State Logical Commitment: `sha256:77e97e70d2d5aeb28faa7cecb43bd8c9a17855a42d1bdf6fe73e9e0b126735f1`
- Workspace profile: `open`
- Native model: `semantic_graph`
- Canonical artifacts: `1`
- Sources: `142`
- External pinned references: `0`
- Materialization manifests: `2`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intent and scope

This Kristal maps the **kOA Digital Ecosystem** as a durable semantic graph of components, capabilities, operating functions, contracts, artifacts, workflows, authorities, lifecycles, repositories and evidence.

The current domain content version is `0.6.3`. The authoritative portable domain state is `kristal_state/6.0`; the Local Kristal envelope targets `kristal.state/9.0` while retaining the existing v6 state and its already-established v9 Logical Commitment.

The normalization to Local Kit 3.2.2 is structural and additive. It does not rewrite domain assertions or silently promote evidence.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Semantic boundary

## Owned here

This Kristal owns the curated **cross-system ecosystem map** and the local architectural assertions that describe how kOA components, capabilities, functions, contracts, artifacts, workflows, lifecycles, repositories and evidence relate inside that map. It also owns the editorial selection/qualification rules used to compile that map.

The canonical subject is `koa:digital-ecosystem` — **kOA Digital Ecosystem**.

## Explicitly not owned here

- Internal implementation truth of owner repositories beyond assertions explicitly imported into this Kristal.
- Authority of independent supporting ecosystems or external tools merely connected to kOA.
- Runtime deployment or activation merely because a composition, repository or local checkout exists.
- Financial, pricing, revenue, funding and other commercial claims excluded by `knowledge-base/documentation/SOURCE_SELECTION.md`.

## Boundary invariants

The existing project documentation makes these distinctions normative:

```text
repository != authority
hosting != ownership
scenario != deployment
projection != canon
support != membership
```

A source can establish claims only within its documented authority scope.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Native model

The native model is a **typed semantic graph** represented in the canonical `kristal_state/6.0` file. It is compiled from curated editorial catalogs under `knowledge-base/sources/`.

The main domain topology includes relations such as:

```text
Component -> Capability -> Need
Component -> OperatingFunction
Utility -> WorkflowPattern -> Capability
ProblemFamily -> WorkflowPattern
Scenario -> WorkflowPattern
Scenario -> Component
```

Around this graph are contracts, artifacts, lifecycles, invariants, domains, repositories and external references. Assertions carry source/evidence references and can also carry valuations, notes and status.

At normalization time the native validators report **7,929 assertions**, **2,523 relations**, **718 referents** and **117 components**. These counts describe the preserved snapshot; they are not schema limits.

The Local Kit must not flatten this model into a simpler generic structure. The existing v6 canonical file remains the domain-native payload, registered in `canon/state.index.json` by its pre-existing v9 Logical Commitment.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Epistemic model and authority

Provenance and authority remain separate. The source registry and canonical assertions retain source IDs, evidence references, assertion status, record role and other qualifiers.

Key rules already established by the project:

- A repository is not automatically an application, member or authority.
- An owner repository README/contract is strong evidence for its own declared purpose, version and implementation boundary, not for the whole ecosystem.
- Local presence does not prove activation or deployment.
- Scenario compositions can remain `runtime UNVERIFIED`.
- Missing or unresolved information must not be fabricated.
- Supporting ecosystems can contribute capabilities without becoming kOA members.
- AI/model output does not become proof or canon without explicit review/promotion.

The 3.2.2 `sources/source-catalog.json` preserves all 142 current source identities and their authority notes from `koa.source-registry.v4`. The original project source registry remains the richer project-specific record.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonical and derived surfaces

## Canonical domain artifact

`knowledge-base/corpus/koa-ecosystem.kristal-state.json` is the registered canonical domain state. Its existing v9 Logical Artifact is:

- artifact: `urn:kristal:koa-ecosystem:artifact:canonical-state`
- contract: `koa-ecosystem.canonical-knowledge-state/1.0`
- commitment: `sha256:8d5195171697739485ada83e69b8fae83fe95cda155d5181a8d61dff4cc40a74`

The file remains at its legacy path so the existing project builder and validations keep working without a semantic rewrite. `canon/state.index.json` is the Local Kit 3.2.2 registry for that artifact.

## Authoring/build inputs

`knowledge-base/sources/` contains editorial catalogs and the project-specific source registry used by the native builder. They are not silently promoted to additional v9 State Snapshot members.

## Derived/rebuildable surfaces

- `knowledge-base/corpus/index.json` — query/index surface.
- `.kristal/v8/` — legacy read/query models.
- `views/` — generated navigational views and matrices.
- `build/v9/` — Local Kit 3.2.2 build candidate.
- `.kristal/v9/` — retained legacy v9 compatibility/migration envelope.
- `runtime/`, `derived/`, `projections/materialized/`, `state/` — reconstructible surfaces when used.

Generated surfaces must never be edited as a shortcut for changing canonical knowledge.
