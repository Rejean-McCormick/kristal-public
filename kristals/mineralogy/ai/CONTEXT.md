# AI Context — Mineralogy

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:mineralogy:state`
- State Logical Commitment: `sha256:e44829573b505b85e817e5e5fb22b51294fc37365a7514a3e7c208e2d00f0692`
- Workspace profile: `layered`
- Native model: `composition_structure_property_occurrence_graph`
- Canonical artifacts: `12`
- Sources: `7`
- External pinned references: `0`
- Materialization manifests: `2`
- Workspace-local materialization blobs: `2`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et scope — Kristal-Mineralogy

Ce workspace apporte une enveloppe **Local Kristal 3.2.2** au corpus v6/v9 existant sans modification éditoriale ni refonte sémantique.

## Forme et sujet déjà établis

composition chimique + structure cristalline → identité minérale → propriétés → occurrences.

Lire le `README.md` historique pour la description complète du corpus. `state_ref`: `urn:kristal:mineralogy:state`.

## Portée de cette mise à jour

- Préserver les données sources et anciens fichiers v8/v9.
- Conserver le Logical Commitment et le State Commitment historiques.
- Ajouter un input canonique v9 recalculable, le catalogue de navigation des sources, les protocoles et le build.
- Ne pas prétendre à une qualification métier indépendante, ni à une publication v10.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Mineralogy

## Possession logique

Ce Kristal possède les assertions statiques et identités de son corpus de référence dans le domaine `mineralogy_composition_structure_properties_occurrence` et les règles d'interprétation associées.

Géométrie native déclarée : composition chimique + structure cristalline → identité minérale → propriétés → occurrences.

## Ce qui n'est pas possédé ou garanti

Ne pas assimiler ce graphe à une base exhaustive des analyses d’échantillons et occurrences réelles.

Les sources amont et leur autorité éditoriale ne sont pas contrôlées par cet état local ; la présence d'une assertion ne la transforme pas en vérité universelle.

## Documents historiques de frontière / architecture

- `knowledge-base/documentation/ARCHITECTURE.md`
- `knowledge-base/documentation/BOUNDARIES.md`
- `knowledge-base/documentation/COVERAGE.md`
- `knowledge-base/documentation/ONTOLOGY.md`
- `knowledge-base/documentation/SOURCES.md`
- `knowledge-base/documentation/VALIDATION.md`

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-Mineralogy

**Kind local** : `composition_structure_property_occurrence_graph`.

**Géométrie conservée** : composition chimique + structure cristalline → identité minérale → propriétés → occurrences.

**Invariant essentiel** : la composition et la structure ne doivent pas être confondues ; les contextes d’occurrence sont distincts de l’identité.

Le contrat engagé par le v9 historique reste `kristal_state.hash_target/6.0`. Ce contrat est un `kristal_state` v6 matérialisé en assertions atomiques avec informations de provenance. Cette migration ne convertit pas ce graphe en ontologie uniforme, en table ou en pipeline artificiel.

La vue authoring `canon/domain/legacy-v6-state.payload.json` est une photographie canonique du payload existant. Les fichiers du domaine dans `knowledge-base` restent inchangés. Le maintien en synchronisation future de ces deux sources exige une procédure éditoriale explicite.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique — Kristal-Mineralogy

## Preuves et sources

La bibliographie / provenance historique est accessible dans `knowledge-base/sources/source_catalog.json`. Sa vue normalisée est `sources/source-catalog.json` (7 entrées). Les métadonnées complètes et politiques historiques demeurent dans le fichier d'origine ou dans le payload engagé.

## Interprétation

Une source, une assertion, un auteur et un engagement logique ont des fonctions distinctes : provenance ≠ autorité ≠ vérité. Un désaccord ne doit pas être résolu sans justifier l'autorité. `unknown` ≠ `false`.

Invariant disciplinaire : la composition et la structure ne doivent pas être confondues ; les contextes d’occurrence sont distincts de l’identité.

Une réponse d'IA reste une proposition. Un index de requête ou une projection peut montrer une information sans devenir une source d'autorité.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé — Kristal-Mineralogy

## Canon authoring 3.2.2

- `canon/state.index.json` décrit l'unique Logical Artifact hérité.
- `canon/domain/legacy-v6-state.payload.json` est un input JSON canonique construit par copie logique du payload v9 antérieur et réengagé avec `compute-json-jcs`.
- `knowledge-base/sources/` conserve les sources métier natives non modifiées. Le corpus v6 historique reste un artefact de compatibilité connu ; sa qualité de canon historique n'est pas révoquée.

## Historique v9 préservé

Les manifests `.kristal/v9/materializations/inline-json.materialization.json` et `.kristal/v9/materializations/portable-v6.materialization.json` sont conservés. Les blobs sont vérifiés par leurs digests physiques, mais le `build-v9` du Kit 3.2.2 reconstruit sa propre matérialisation `inline-json/1` et ne réutilise pas automatiquement ces deux manifests.

## Dérivé

`build/v9`, les caches v8, `state/`, `derived/`, `projections/materialized/`, `runtime/`, `release/` et toute couche `ai/` sont des sorties opératoires distinctes.

La factorisation v9 est **permise par le framework**, mais **n'est pas revendiquée** pour ce Kristal : aucun manifest factorisé n'était présent dans l'archive. La réduction des duplications futures doit être lossless et n'affecter aucun Logical Commitment.
