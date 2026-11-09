# AI Context — Recipes

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:recipes`
- State Logical Commitment: `sha256:5318163afb08353c04e72112999d91e8b48d97e5f527235e932a603b85fd33c4`
- Workspace profile: `layered`
- Native model: `procedural_transformation_graph_and_family_variants`
- Canonical artifacts: `1`
- Sources: `13`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et périmètre — Kristal-Recipes

Ce dépôt conserve son domaine et sa sémantique historique. L'enveloppe Local Kristal 3.2.2 est ajoutée sans modifier les fichiers préexistants.

**Forme :** Programmes culinaires de transformation de matière, familles, variantes versionnées, sources et graphes procéduraux.

**State v9 :** `urn:kristal:state:recipes` ; **scope initial :** `{"domain": "culture", "subdomain": "recipes", "language": "fr", "environment": "knowledge-base"}`.

Le contrat natif v9 déjà présent est `recipes.domain-native-canonical-payload/1.0`, caractérisé ici comme noyau natif v7/domain-specific. Aucun reclassement du canon historique n'est imposé.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique

## Ownership positif

Modèle canonique des familles, variantes, ingrédients, mécanismes, transitions et sources culinaires.

## Ne possède pas

Assimilation d’une famille à sa variante ou d’une source externe à une recette vérifiée. Le dépôt ne possède pas automatiquement ses sources externes et ne publie ni n'active de State v9 à l'occasion de cette normalisation.

## State et références

`urn:kristal:state:recipes` ; membres : 1 ; références externes pinées : 0. L’absence de références pinées n’implique pas absence de sources bibliographiques dans le catalogue.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif

`native_model.kind = procedural_transformation_graph_and_family_variants` (qualification descriptive de la forme existante, non conversion).

Programmes culinaires de transformation de matière, familles, variantes versionnées, sources et graphes procéduraux.

**Orientation principale :** RecipeFamily → RecipeVariant → transformations/états → résultats.

**Invariants :** RecipeFamily != RecipeVariant != RecipeSourceInstance ; préserver étapes, états et provenance.

L'engagement v9 existant porte sur le payload logique à `canon/domain/v9-logical-payload.json`. Les relations et structures déjà déclarées dans le corpus historique demeurent la référence détaillée. Le seul changement de layout ne crée pas de nouveaux prédicats ni de nouveaux IDs.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Épistémologie et autorité

Le catalogue d’origine `knowledge-base/sources/source_catalog.json` est conservé, avec une concordance sous `sources/source-catalog.json`. Les notices y sont copiées dans `legacy_record` pour conserver les classes d'évidence/autorité explicites du corpus.

La provenance d'une source n'implique pas vérité automatique ou autorité d'édition. Une divergence ne doit pas être effacée silencieusement ; `unknown != false`. Les sorties d’IA éventuelles restent des propositions et non des faits canoniques.

**Règle métier :** RecipeFamily != RecipeVariant != RecipeSourceInstance ; préserver étapes, états et provenance.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé

## Canon local 3.2.2

`canon/domain/v9-logical-payload.json` est une extraction à l’identique des données `payload` du Logical Artifact v9 préexistant, engagée en `compute-json-jcs` via `canon/state.index.json`.

Les fichiers sources historiques et leurs règles sémantiques ne sont ni supprimés ni modifiés. `build/v9`, `.kristal/v8`, les caches/index et les projections `knowledge-base/corpus` ne doivent pas devenir une nouvelle autorité par le fait d'être matérialisés.

## Matérialisations v9

La matérialisation historique `recipes.materialization/domain-native-json-set/1` est conservée sous `.kristal/v9/materialization.json`, avec 17 segment(s) identifié(s) par SHA-256. Le builder officiel 3.2.2 génère aussi sa représentation `inline-json/1`. Le workflow `tools/build_verified_v9.py` réenregistre ensuite le manifeste historique sous `build/v9/materializations/` **après validation des blobs et de leur lien au Logical Commitment**.

Le succès de la vérification physique n’équivaut pas à une preuve indépendante de toute la procédure de reconstruction lossless.
