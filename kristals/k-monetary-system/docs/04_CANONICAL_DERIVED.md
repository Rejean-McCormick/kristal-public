# 04 — Canonical versus derived

## Canonical

`canon/domain/` owns the system, constitution, statechart, causal/distribution model and append-only event schema.

`canon/operations/` owns executable policy/settlement/simulation contracts.

`canon/epistemic/` owns assumptions, hypotheses, counterarguments, evidence obligations and validation state.

## Derived

Simulation runs, charts, dashboards, rankings, forecast summaries, Monte-Carlo distributions, query indexes, embeddings and UI projections are derived.

A simulation run may be appended to the event ledger as a historical record, but its numeric output remains a model result unless independently validated and explicitly promoted.
