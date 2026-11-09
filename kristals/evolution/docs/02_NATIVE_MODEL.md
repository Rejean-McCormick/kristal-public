# Modèle natif — Kristal-Evolution

Le modèle déclaré par `.kristal/v9/domain-profile.json` est : **evolutionary process and lineage graph**.

Axe canonique historique : `variation → transmission/descent → differential/stochastic sorting → population change → lineages → divergence`.

## Distinctions à préserver

- natural selection ≠ all evolution
- mutation
- genetic drift
- gene flow
- lineage/divergence

## Supports locaux du modèle

- `knowledge-base/corpus/evolutionary-process-model.json`
- `knowledge-base/corpus/selection-model.json`
- `knowledge-base/corpus/lineage-model.json`
- `knowledge-base/corpus/divergence-model.json`

L'unique artefact logique v9 importé possède le contrat `kristal.portable-epistemic-state/6.0` et porte le payload du portable state v6 original. La nouvelle structure n'aplatit pas les primitives du domaine.
