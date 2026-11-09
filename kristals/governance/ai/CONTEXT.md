# AI Context — Governance

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:governance`
- State Logical Commitment: `sha256:0abc7effb122f143b2359fcaefb4721b15c35965bd3237e7404c9d7f44ca110c`
- Workspace profile: `layered`
- Native model: `mandate-institution-competence-decision-implementation-accountability-graph`
- Canonical artifacts: `14`
- Sources: `10`
- External pinned references: `0`
- Materialization manifests: `2`
- Workspace-local materialization blobs: `5`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et périmètre — Kristal-Governance

La présente migration **n'ajoute pas de faits métier**. Elle normalise l'enveloppe d'authoring v9 existante au format Local Kristal 3.2.2.

- Domaine existant : `governance`.
- Édition : `1.0.0`.
- Forme native existante : `mandate-institution-competence-decision-implementation-accountability-graph`.
- State ref : `urn:kristal:state:governance`.
- Documents métier source : `README.md` et `knowledge-base/documentation/`.

Les sources, le corpus et les snapshots originaux sont **conservés octet pour octet**.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Governance

Le Kristal possède le modèle logique et les ressources identifiées par son propre `resource-basis` v9; il ne devient pas l'autorité éditoriale de ses sources amont, des publications externes ou des systèmes runtime.

## Rôles canoniques déclarés

- `portable_epistemic_state`
- `identity_registry`
- `evidence_registry`
- `source_catalog`

## Garde-fous du domaine (extraits exacts du Logical Artifact v9)

- `mandate != unlimited_authority`
- `formal_authority != de_facto_power`
- `decision != implementation`
- `legality != legitimacy != effectiveness`

Chaque ressource originale conserve son identité. Une observation ne devient pas une vérité universelle du fait de son import.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-Governance

Type native déclaré par l'état sémantique v9 : **`mandate-institution-competence-decision-implementation-accountability-graph`**.

Les deux Logical Artifacts possédés sont :

- `urn:kristal:governance:resource-basis` — `kristal.repository-resource-set/1.0`
- `urn:kristal:governance:semantic-state` — `governance.semantic-state/9.0`

Le second dépend explicitement du premier. Les payloads originaux sont extraits sous `canon/domain/` et leurs commitments sont recalculés au build, sans réinventer un schéma universel.

Pour les détails des entités et relations, voir les documents métiers sous `knowledge-base/documentation/` et les ressources historiques.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Épistémologie et autorité — Kristal-Governance

- Autorité déclarée : `urn:kristal:authority:governance`.
- Provenance : `knowledge-base/sources/source-catalog.json` (10 entrées importées).
- Gouvernance sémantique : les distinctions du Logical Artifact sont contractuelles.
- Les registres de ressources, d'identité et les pièces de provenance restent distincts des artefacts dérivés.
- `unknown != false`; `provenance != authority`; `AI output != canon`.
- Les désaccords ne sont pas supprimés ou fusionnés silencieusement pendant la migration.

Aucune validation scientifique, médicale, juridique ou institutionnelle supplémentaire n'est impliquée par ce build.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé — Kristal-Governance

## Resources physiques canoniques historiques

- `knowledge-base/corpus/governance.kristal-state.json` — rôle `portable_epistemic_state`, ID `urn:kristal:governance:resource:portable_epistemic_state`
- `knowledge-base/corpus/referents.json` — rôle `identity_registry`, ID `urn:kristal:governance:resource:identity_registry`
- `knowledge-base/sources/evidence-registry.json` — rôle `evidence_registry`, ID `urn:kristal:governance:resource:evidence_registry`
- `knowledge-base/sources/source-catalog.json` — rôle `source_catalog`, ID `urn:kristal:governance:resource:source_catalog`

## Canon authoring 3.2.2

`canon/domain/resource-basis.payload.json` et `canon/domain/domain-state.payload.json` contiennent **seulement les payloads logiques préexistants**. `canon/state.index.json` fixe leurs contrats, dépendances, scopes et autorités.

## Matérialisations préservées

- `.kristal/v9/materializations/domain-state.materialization.json`
- `.kristal/v9/materializations/resource-basis.materialization.json`

Les manifestes historiques et leurs blobs restent en place; `tools/build_with_materializations.py` revalide leurs digests physiques et les enregistre en complément de la matérialisation inline du builder. Il ne faut jamais déclarer qu'une représentation est factorisée si elle ne l'est pas.

Les index `.kristal/v8`, caches, `build/` et projections non canoniques restent des dérivés; la migration ne réinterprète pas les anciens manifestes de contenu.
