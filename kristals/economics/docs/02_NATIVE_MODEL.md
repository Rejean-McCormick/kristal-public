# Modèle natif — Kristal-Economics

Le modèle déclaré par `.kristal/v9/domain-profile.json` est : **allocation-under-constraints relation/model graph**.

Axe canonique historique : `agents + constraints → choices/incentives → production/transactions → allocation`.

## Distinctions à préserver

- descriptive relation
- model rule
- model scope
- market as one allocation mechanism

## Supports locaux du modèle

- `knowledge-base/corpus/allocation-graph.json`
- `knowledge-base/corpus/transaction-network.json`
- `knowledge-base/corpus/production-graph.json`
- `knowledge-base/corpus/market-structure-matrix.json`
- `knowledge-base/corpus/model-scope-report.json`

L'unique artefact logique v9 importé possède le contrat `kristal.portable-epistemic-state/6.0` et porte le payload du portable state v6 original. La nouvelle structure n'aplatit pas les primitives du domaine.
