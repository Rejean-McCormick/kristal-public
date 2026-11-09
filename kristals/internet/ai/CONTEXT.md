# AI Context — Internet

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:internet`
- State Logical Commitment: `sha256:4dc021e3ffeb97a69e8edfbd87be18766852d73bf4d44fdd128a72e51e4f38f0`
- Workspace profile: `layered`
- Native model: `protocol-addressing-routing-service-dependency-model`
- Canonical artifacts: `10`
- Sources: `51`
- External pinned references: `0`
- Materialization manifests: `2`
- Workspace-local materialization blobs: `13`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et périmètre — Kristal-Internet

La présente migration **n'ajoute pas de faits métier**. Elle normalise l'enveloppe d'authoring v9 existante au format Local Kristal 3.2.2.

- Domaine existant : `internet`.
- Édition : `1.0.0`.
- Forme native existante : `protocol-addressing-routing-service-dependency-model`.
- State ref : `urn:kristal:state:internet`.
- Documents métier source : `README.md` et `knowledge-base/documentation/`.

Les sources, le corpus et les snapshots originaux sont **conservés octet pour octet**.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Internet

Le Kristal possède le modèle logique et les ressources identifiées par son propre `resource-basis` v9; il ne devient pas l'autorité éditoriale de ses sources amont, des publications externes ou des systèmes runtime.

## Rôles canoniques déclarés

- `semantic_model`
- `identifier_model`
- `layer_model`
- `addressing_model`
- `protocol_model`
- `service_model`
- `routing_model`
- `security_model`
- `failure_model`
- `relation_model`
- `semantic_invariants`
- `source_catalog`

## Garde-fous du domaine (extraits exacts du Logical Artifact v9)

- `source_models are authoring_canon`
- `portable_v6_state is derived_projection`
- `valid_address != reachable_endpoint`
- `BGP_announcement != authorization_proof`

Chaque ressource originale conserve son identité. Une observation ne devient pas une vérité universelle du fait de son import.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-Internet

Type native déclaré par l'état sémantique v9 : **`protocol-addressing-routing-service-dependency-model`**.

Les deux Logical Artifacts possédés sont :

- `urn:kristal:internet:resource-basis` — `kristal.repository-resource-set/1.0`
- `urn:kristal:internet:semantic-state` — `internet.semantic-state/9.0`

Le second dépend explicitement du premier. Les payloads originaux sont extraits sous `canon/domain/` et leurs commitments sont recalculés au build, sans réinventer un schéma universel.

Pour les détails des entités et relations, voir les documents métiers sous `knowledge-base/documentation/` et les ressources historiques.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Épistémologie et autorité — Kristal-Internet

- Autorité déclarée : `urn:kristal:authority:internet`.
- Provenance : `knowledge-base/sources/source_catalog.json` (51 entrées importées).
- Gouvernance sémantique : les distinctions du Logical Artifact sont contractuelles.
- Les registres de ressources, d'identité et les pièces de provenance restent distincts des artefacts dérivés.
- `unknown != false`; `provenance != authority`; `AI output != canon`.
- Les désaccords ne sont pas supprimés ou fusionnés silencieusement pendant la migration.

Aucune validation scientifique, médicale, juridique ou institutionnelle supplémentaire n'est impliquée par ce build.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

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
