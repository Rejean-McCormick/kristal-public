# Modèle natif — Kristal-Energy

Le modèle déclaré par `.kristal/v9/domain-profile.json` est : **directed energy-flow and transformation graph**.

Axe canonique historique : `source → conversion → storage → transport → consumption → loss`.

## Distinctions à préserver

- source
- conversion
- storage
- transport
- consumption
- loss

## Supports locaux du modèle

- `knowledge-base/corpus/energy-flow-graph.json`
- `knowledge-base/corpus/conversion-map.json`
- `knowledge-base/corpus/storage-map.json`

L'unique artefact logique v9 importé possède le contrat `kristal.portable-epistemic-state/6.0` et porte le payload du portable state v6 original. La nouvelle structure n'aplatit pas les primitives du domaine.
