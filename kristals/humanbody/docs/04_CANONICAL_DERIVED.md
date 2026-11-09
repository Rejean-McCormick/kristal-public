# Canonique et dérivé — Kristal-HumanBody

## Resources physiques canoniques historiques

- `knowledge-base/corpus/humanbody.structured-epistemic-state.json` — rôle `structured_epistemic_state`, ID `urn:kristal:humanbody:resource:structured_epistemic_state`
- `knowledge-base/corpus/referents.json` — rôle `identity_registry`, ID `urn:kristal:humanbody:resource:identity_registry`
- `knowledge-base/integration/source-resolution-contract.json` — rôle `source_resolution_contract`, ID `urn:kristal:humanbody:resource:source_resolution_contract`

## Canon authoring 3.2.2

`canon/domain/resource-basis.payload.json` et `canon/domain/domain-state.payload.json` contiennent **seulement les payloads logiques préexistants**. `canon/state.index.json` fixe leurs contrats, dépendances, scopes et autorités.

## Matérialisations préservées

- `.kristal/v9/materializations/domain-state.materialization.json`
- `.kristal/v9/materializations/resource-basis.materialization.json`

Les manifestes historiques et leurs blobs restent en place; `tools/build_with_materializations.py` revalide leurs digests physiques et les enregistre en complément de la matérialisation inline du builder. Il ne faut jamais déclarer qu'une représentation est factorisée si elle ne l'est pas.

Les index `.kristal/v8`, caches, `build/` et projections non canoniques restent des dérivés; la migration ne réinterprète pas les anciens manifestes de contenu.
