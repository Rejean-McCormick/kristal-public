# Modèle natif — Kristal-Electronics

Le modèle déclaré par `.kristal/v9/domain-profile.json` est : **component / circuit / function / signal transformation graph**.

Axe canonique historique : `component → circuit → function → signal`.

## Distinctions à préserver

- physical component
- circuit topology
- obtained function
- observed signal

## Supports locaux du modèle

- `knowledge-base/corpus/electronic-pathways.json`
- `knowledge-base/corpus/navigation.json`
- `knowledge-base/corpus/boundaries.json`
- `knowledge-base/corpus/invariants.json`

L'unique artefact logique v9 importé possède le contrat `kristal.portable-epistemic-state/6.0` et porte le payload du portable state v6 original. La nouvelle structure n'aplatit pas les primitives du domaine.
