# AI Context — HomeCare

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:homecare`
- State Logical Commitment: `sha256:de24b8d9ac4f924f4b6ea71b635cfe324a9875fa78680eab3c7ac6237f799895`
- Workspace profile: `layered`
- Native model: `property-functional-diagnostic-temporal-graph`
- Canonical artifacts: `2`
- Sources: `0`
- External pinned references: `0`
- Materialization manifests: `2`
- Workspace-local materialization blobs: `3`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et périmètre — Kristal-HomeCare

La présente migration **n'ajoute pas de faits métier**. Elle normalise l'enveloppe d'authoring v9 existante au format Local Kristal 3.2.2.

- Domaine existant : `homecare`.
- Édition : `2.0.0`.
- Forme native existante : `property-functional-diagnostic-temporal-graph`.
- State ref : `urn:kristal:state:homecare`.
- Documents métier source : `README.md` et `knowledge-base/documentation/`.

Les sources, le corpus et les snapshots originaux sont **conservés octet pour octet**.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-HomeCare

Le Kristal possède le modèle logique et les ressources identifiées par son propre `resource-basis` v9; il ne devient pas l'autorité éditoriale de ses sources amont, des publications externes ou des systèmes runtime.

## Rôles canoniques déclarés

- `structured_epistemic_state`
- `identity_registry`

## Garde-fous du domaine (extraits exacts du Logical Artifact v9)

- `generic_type != installed_instance`
- `derived_current_state != canonical_event_ledger`
- `asset_identity survives progressive_refinement`

Chaque ressource originale conserve son identité. Une observation ne devient pas une vérité universelle du fait de son import.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-HomeCare

Type native déclaré par l'état sémantique v9 : **`property-functional-diagnostic-temporal-graph`**.

Les deux Logical Artifacts possédés sont :

- `urn:kristal:homecare:resource-basis` — `kristal.repository-resource-set/1.0`
- `urn:kristal:homecare:semantic-state` — `homecare.semantic-state/9.0`

Le second dépend explicitement du premier. Les payloads originaux sont extraits sous `canon/domain/` et leurs commitments sont recalculés au build, sans réinventer un schéma universel.

Pour les détails des entités et relations, voir les documents métiers sous `knowledge-base/documentation/` et les ressources historiques.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Épistémologie et autorité — Kristal-HomeCare

- Autorité déclarée : `urn:kristal:authority:homecare`.
- Provenance : Aucun catalogue source générique repéré : inventaire conservé dans les fichiers historiques; catalogue 3.2.2 vide et explicite..
- Gouvernance sémantique : les distinctions du Logical Artifact sont contractuelles.
- Les registres de ressources, d'identité et les pièces de provenance restent distincts des artefacts dérivés.
- `unknown != false`; `provenance != authority`; `AI output != canon`.
- Les désaccords ne sont pas supprimés ou fusionnés silencieusement pendant la migration.

Aucune validation scientifique, médicale, juridique ou institutionnelle supplémentaire n'est impliquée par ce build.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé — Kristal-HomeCare

## Resources physiques canoniques historiques

- `knowledge-base/corpus/homecare.structured-epistemic-state.json` — rôle `structured_epistemic_state`, ID `urn:kristal:homecare:resource:structured_epistemic_state`
- `knowledge-base/corpus/referents.json` — rôle `identity_registry`, ID `urn:kristal:homecare:resource:identity_registry`

## Canon authoring 3.2.2

`canon/domain/resource-basis.payload.json` et `canon/domain/domain-state.payload.json` contiennent **seulement les payloads logiques préexistants**. `canon/state.index.json` fixe leurs contrats, dépendances, scopes et autorités.

## Matérialisations préservées

- `.kristal/v9/materializations/domain-state.materialization.json`
- `.kristal/v9/materializations/resource-basis.materialization.json`

Les manifestes historiques et leurs blobs restent en place; `tools/build_with_materializations.py` revalide leurs digests physiques et les enregistre en complément de la matérialisation inline du builder. Il ne faut jamais déclarer qu'une représentation est factorisée si elle ne l'est pas.

Les index `.kristal/v8`, caches, `build/` et projections non canoniques restent des dérivés; la migration ne réinterprète pas les anciens manifestes de contenu.
