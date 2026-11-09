# Canonique et dérivé — Kristal-Internet

## Resources physiques canoniques historiques

- `knowledge-base/sources/semantic_model.json` — rôle `semantic_model`, ID `urn:kristal:internet:resource:semantic_model`
- `knowledge-base/sources/identifiers.json` — rôle `identifier_model`, ID `urn:kristal:internet:resource:identifier_model`
- `knowledge-base/sources/layers.json` — rôle `layer_model`, ID `urn:kristal:internet:resource:layer_model`
- `knowledge-base/sources/addressing.json` — rôle `addressing_model`, ID `urn:kristal:internet:resource:addressing_model`
- `knowledge-base/sources/protocols.json` — rôle `protocol_model`, ID `urn:kristal:internet:resource:protocol_model`
- `knowledge-base/sources/services.json` — rôle `service_model`, ID `urn:kristal:internet:resource:service_model`
- `knowledge-base/sources/routing.json` — rôle `routing_model`, ID `urn:kristal:internet:resource:routing_model`
- `knowledge-base/sources/security.json` — rôle `security_model`, ID `urn:kristal:internet:resource:security_model`
- `knowledge-base/sources/failures.json` — rôle `failure_model`, ID `urn:kristal:internet:resource:failure_model`
- `knowledge-base/sources/relations.json` — rôle `relation_model`, ID `urn:kristal:internet:resource:relation_model`
- `knowledge-base/sources/invariants.json` — rôle `semantic_invariants`, ID `urn:kristal:internet:resource:semantic_invariants`
- `knowledge-base/sources/source_catalog.json` — rôle `source_catalog`, ID `urn:kristal:internet:resource:source_catalog`

## Canon authoring 3.2.2

`canon/domain/resource-basis.payload.json` et `canon/domain/domain-state.payload.json` contiennent **seulement les payloads logiques préexistants**. `canon/state.index.json` fixe leurs contrats, dépendances, scopes et autorités.

## Matérialisations préservées

- `.kristal/v9/materializations/domain-state.materialization.json`
- `.kristal/v9/materializations/resource-basis.materialization.json`

Les manifestes historiques et leurs blobs restent en place; `tools/build_with_materializations.py` revalide leurs digests physiques et les enregistre en complément de la matérialisation inline du builder. Il ne faut jamais déclarer qu'une représentation est factorisée si elle ne l'est pas.

Les index `.kristal/v8`, caches, `build/` et projections non canoniques restent des dérivés; la migration ne réinterprète pas les anciens manifestes de contenu.
