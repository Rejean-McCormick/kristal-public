# Canonique et dérivé

## Logical Artifacts canoniques 3.2.2

`canon/state.index.json` enregistre deux Logical Artifacts v9 déjà présents dans la migration additive antérieure :

- `urn:kristal:pi-theory:resource-basis` ;
- `urn:kristal:pi-theory:semantic-state`.

Leurs représentations sont copiées octet pour octet sous `canon/logical/` et leurs Logical Commitments sont déclarés `precomputed`. Cette décision permet de conserver exactement le State Logical Commitment v9 existant sans prétendre recalculer un contrat différent à partir du payload v6.

## Ressources historiques liées

Le resource-basis engage les ressources historiques existantes : état v6, registre de référents, catalogue/politique de sources, historique des versions et registre d'empreintes externes. Elles restent à leurs emplacements d'origine et ne sont pas réécrites par la normalisation.

## Dérivés

Sont notamment dérivés/reconstructibles : `.kristal/v8/`, l'ancienne couche de compatibilité `.kristal/v9/`, `views/ai-contexts/`, `build/`, ainsi que les rapports/index listés dans `kristal.workspace.json` et `canon/state.index.json`.

`BUILD != PUBLISH != ACTIVATE`. Aucun artefact dérivé ne devient canon par simple existence.
