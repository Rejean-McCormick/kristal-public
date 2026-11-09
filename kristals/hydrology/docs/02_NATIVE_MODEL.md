# Modèle natif — Kristal-Hydrology

Type native déclaré par l'état sémantique v9 : **`coupled-stock-flow-graph`**.

Les deux Logical Artifacts possédés sont :

- `urn:kristal:hydrology:resource-basis` — `kristal.repository-resource-set/1.0`
- `urn:kristal:hydrology:semantic-state` — `hydrology.semantic-state/9.0`

Le second dépend explicitement du premier. Les payloads originaux sont extraits sous `canon/domain/` et leurs commitments sont recalculés au build, sans réinventer un schéma universel.

Pour les détails des entités et relations, voir les documents métiers sous `knowledge-base/documentation/` et les ressources historiques.
