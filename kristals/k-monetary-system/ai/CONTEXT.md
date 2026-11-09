# AI Context — K Monetary System — Socio-Monetary Transition Model

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:k-monetary-system`
- State Logical Commitment: `sha256:53cdf568c0a7fee24d2993968b09a25fd522cdafc6dc96877864023fb1982c9b`
- Workspace profile: `executable`
- Native model: `hybrid_executable_multiplex_statechart_causal_ledger`
- Canonical artifacts: `36`
- Sources: `41`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# 00 — Intent and scope

## Intent

Crystallize the K monetary thought experiment as a testable system rather than a narrative claim. The Kristal must preserve monetary, payment, distributional, governance, debt-transition and real-resource distinctions while allowing conditional simulation.

## Scope

Owned here: K_M/K_C design, monetary constitution, transition statechart, causal/distributional models, policy-operation contracts, payment settlement semantics, debt-transition scenario semantics, simulation specification and epistemic memory.

Not owned here: Smart Vote/EkoH internals, sovereign law, empirical macroeconomic datasets, external central-bank authority, or the truth of the scenario.

## Success criterion

A researcher should be able to change assumptions or policy parameters and inspect the consequences without any simulation output being silently promoted to fact or policy authority.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# 01 — Semantic boundary

The subject is **one monetary system under transition**, not a collection of separate topic Kristals.

The Kristal owns the semantics of K_M, K_C, the transition states, causal/distributional relations, monetary/payment/social-dividend/debt operations, and the epistemic status of claims about them.

It references Konnaxion Smart Vote as an **external governance authority interface**. It does not copy Smart Vote's scoring ontology or claim authority over its implementation.

A future split into another Kristal is justified only by a genuine authority/lifecycle/permission boundary (for example an independently governed production payment network), not merely because a subsystem is complex.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# 02 — Native model

Shape probes identify a hybrid form:

- **Multiplex:** monetary, payment, credit, distribution, fiscal, governance, productive-capacity and epistemic layers connect many of the same actors.
- **Statechart:** adoption can progress, stagnate or fail through explicit regime states.
- **Causal model:** signed mechanisms and feedback loops must remain distinguishable from empirical proof.
- **Executable:** monetary, payment, social-dividend and simulation contracts have operational semantics.
- **Polychronical ledger:** policy/adoption/stress events must remain append-only.
- **Research memory:** hypotheses, counterarguments, evidence obligations and validation state must survive failed tests.

No single graph or flat assertion list can preserve all of these distinctions losslessly.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# 03 — Epistemic model

The Kristal uses explicit regimes:

```text
DESIGN ASSUMPTION
SCENARIO ASSUMPTION
REFERENCE MODEL / ACCOUNTING IDENTITY
HYPOTHESIS
EXTERNAL SYSTEM REFERENCE
EVIDENCE OBLIGATION
POLICY DECISION
ACTION / ACTIVATION
SIMULATION OUTPUT
OBSERVED OUTCOME
COUNTERARGUMENT
UNKNOWN
```

Key rule:

```text
SIMULATION OUTPUT != FORECAST != POLICY DECISION != OBSERVED FACT
```

The extreme-adoption scenario is intentionally allowed as an assumption for stress-testing. Its presence in canon records the modeled condition, not its probability.

Smart Vote decisions are decision records. They do not prove causal hypotheses true.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# 04 — Canonical versus derived

## Canonical

`canon/domain/` owns the system, constitution, statechart, causal/distribution model and append-only event schema.

`canon/operations/` owns executable policy/settlement/simulation contracts.

`canon/epistemic/` owns assumptions, hypotheses, counterarguments, evidence obligations and validation state.

## Derived

Simulation runs, charts, dashboards, rankings, forecast summaries, Monte-Carlo distributions, query indexes, embeddings and UI projections are derived.

A simulation run may be appended to the event ledger as a historical record, but its numeric output remains a model result unless independently validated and explicitly promoted.
