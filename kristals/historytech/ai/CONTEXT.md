# AI Context — HistoryTech

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:historytech`
- State Logical Commitment: `sha256:091b2c41a9621a7b73fdd556ae313f077058145110a590536362c2ab2939ec15`
- Workspace profile: `layered`
- Native model: `technology-manifestation-occurrence-sociotechnical-lineage-graph`
- Canonical artifacts: `13`
- Sources: `37`
- External pinned references: `0`
- Materialization manifests: `2`
- Workspace-local materialization blobs: `4`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et périmètre — Kristal-HistoryTech

La présente migration **n'ajoute pas de faits métier**. Elle normalise l'enveloppe d'authoring v9 existante au format Local Kristal 3.2.2.

- Domaine existant : `historytech`.
- Édition : `0.10.2`.
- Forme native existante : `technology-manifestation-occurrence-sociotechnical-lineage-graph`.
- State ref : `urn:kristal:state:historytech`.
- Documents métier source : `README.md` et `knowledge-base/documentation/`.

Les sources, le corpus et les snapshots originaux sont **conservés octet pour octet**.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-HistoryTech

Le Kristal possède le modèle logique et les ressources identifiées par son propre `resource-basis` v9; il ne devient pas l'autorité éditoriale de ses sources amont, des publications externes ou des systèmes runtime.

## Rôles canoniques déclarés

- `structured_epistemic_state`
- `source_authority_registry`
- `editorial_semantic_policy`

## Garde-fous du domaine (extraits exacts du Logical Artifact v9)

- `technology != manifestation != occurrence`
- `certainty_level != sociotechnical_state`
- `earliest_known_attestation is derived`
- `source_authority != automatic_validation`

Chaque ressource originale conserve son identité. Une observation ne devient pas une vérité universelle du fait de son import.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-HistoryTech

Type native déclaré par l'état sémantique v9 : **`technology-manifestation-occurrence-sociotechnical-lineage-graph`**.

Les deux Logical Artifacts possédés sont :

- `urn:kristal:historytech:resource-basis` — `kristal.repository-resource-set/1.0`
- `urn:kristal:historytech:semantic-state` — `historytech.semantic-state/9.0`

Le second dépend explicitement du premier. Les payloads originaux sont extraits sous `canon/domain/` et leurs commitments sont recalculés au build, sans réinventer un schéma universel.

Pour les détails des entités et relations, voir les documents métiers sous `knowledge-base/documentation/` et les ressources historiques.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Épistémologie et autorité — Kristal-HistoryTech

- Autorité déclarée : `urn:kristal:authority:historytech`.
- Provenance : `knowledge-base/sources/source_hunting_catalog.json` (37 entrées importées).
- Gouvernance sémantique : les distinctions du Logical Artifact sont contractuelles.
- Les registres de ressources, d'identité et les pièces de provenance restent distincts des artefacts dérivés.
- `unknown != false`; `provenance != authority`; `AI output != canon`.
- Les désaccords ne sont pas supprimés ou fusionnés silencieusement pendant la migration.

Aucune validation scientifique, médicale, juridique ou institutionnelle supplémentaire n'est impliquée par ce build.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé — Kristal-HistoryTech

## Resources physiques canoniques historiques

- `knowledge-base/corpus/historytech.structured-epistemic-state.json` — rôle `structured_epistemic_state`, ID `urn:kristal:historytech:resource:structured_epistemic_state`
- `knowledge-base/sources/source_authority_registry.json` — rôle `source_authority_registry`, ID `urn:kristal:historytech:resource:source_authority_registry`
- `knowledge-base/sources/historytech_design_principles_v1.json` — rôle `editorial_semantic_policy`, ID `urn:kristal:historytech:resource:editorial_semantic_policy`

## Canon authoring 3.2.2

`canon/domain/resource-basis.payload.json` et `canon/domain/domain-state.payload.json` contiennent **seulement les payloads logiques préexistants**. `canon/state.index.json` fixe leurs contrats, dépendances, scopes et autorités.

## Matérialisations préservées

- `.kristal/v9/materializations/domain-state.materialization.json`
- `.kristal/v9/materializations/resource-basis.materialization.json`

Les manifestes historiques et leurs blobs restent en place; `tools/build_with_materializations.py` revalide leurs digests physiques et les enregistre en complément de la matérialisation inline du builder. Il ne faut jamais déclarer qu'une représentation est factorisée si elle ne l'est pas.

Les index `.kristal/v8`, caches, `build/` et projections non canoniques restent des dérivés; la migration ne réinterprète pas les anciens manifestes de contenu.
