# AI Context — Biology

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:biology`
- State Logical Commitment: `sha256:920e39ac5c26521b4f18362a911a5c8ba5a916620fce5f62a2aa0990398fa31c`
- Workspace profile: `layered`
- Native model: `multiscale_biological_organization_graph`
- Canonical artifacts: `9`
- Sources: `17`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et scope — Kristal-Biology

Ce workspace apporte une enveloppe **Local Kristal 3.2.2** au corpus historique doté d’un état v9 sans modification éditoriale ni refonte sémantique.

## Forme et sujet déjà établis

cellule → tissu → organisme → population, avec fonction, reproduction, hérédité et évolution comme processus transversaux.

Lire le `README.md` historique pour la description complète du corpus. `state_ref`: `urn:kristal:state:biology`.

## Portée de cette mise à jour

- Préserver les données sources et anciens fichiers v8/v9.
- Conserver le Logical Commitment et le State Commitment historiques.
- Ajouter un input canonique v9 recalculable, le catalogue de navigation des sources, les protocoles et le build.
- Ne pas prétendre à une qualification métier indépendante, ni à une publication v10.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Biology

## Possession logique

Ce Kristal possède les assertions statiques et identités de son corpus de référence dans le domaine `biology` et les règles d'interprétation associées.

Géométrie native déclarée : cellule → tissu → organisme → population, avec fonction, reproduction, hérédité et évolution comme processus transversaux.

## Ce qui n'est pas possédé ou garanti

Pas une encyclopédie taxonomique ni biomédicale ; biochimie, médecine, virologie spécialisée et écosystèmes restent distincts.

Les sources amont et leur autorité éditoriale ne sont pas contrôlées par cet état local ; la présence d'une assertion ne la transforme pas en vérité universelle.

## Documents historiques de frontière / architecture

- `knowledge-base/documentation/ARCHITECTURE.md`
- `knowledge-base/documentation/CONTENT_BOUNDARY.md`
- `knowledge-base/documentation/SCALE_MODEL.md`
- `knowledge-base/documentation/SEMANTIC_GUARDRAILS.md`

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-Biology

**Kind local** : `multiscale_biological_organization_graph`.

**Géométrie conservée** : cellule → tissu → organisme → population, avec fonction, reproduction, hérédité et évolution comme processus transversaux.

**Invariant essentiel** : hérédité ≠ héritabilité ; division cellulaire ≠ reproduction organismique ; sélection naturelle ≠ évolution ; fonction ≠ intention.

Le contrat engagé par le v9 historique reste `kristal.compat.v6-state-logical/1.0`. Ce contrat utilise le payload d'origine engagé dans v9 (corpus sémantique natif pour Catho ; `kristal_state` v6 pour les autres), avec les informations de provenance existantes. Cette migration ne convertit pas ce graphe en ontologie uniforme, en table ou en pipeline artificiel.

La vue authoring `canon/domain/legacy-v6-state.payload.json` est une photographie canonique du payload existant. Les fichiers du domaine dans `knowledge-base` restent inchangés. Le maintien en synchronisation future de ces deux sources exige une procédure éditoriale explicite.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique — Kristal-Biology

## Preuves et sources

La bibliographie / provenance historique est accessible dans `knowledge-base/sources/source-catalog.json`. Sa vue normalisée est `sources/source-catalog.json` (17 entrées). Les métadonnées complètes et politiques historiques demeurent dans le fichier d'origine ou dans le payload engagé.

## Interprétation

Une source, une assertion, un auteur et un engagement logique ont des fonctions distinctes : provenance ≠ autorité ≠ vérité. Un désaccord ne doit pas être résolu sans justifier l'autorité. `unknown` ≠ `false`.

Invariant disciplinaire : hérédité ≠ héritabilité ; division cellulaire ≠ reproduction organismique ; sélection naturelle ≠ évolution ; fonction ≠ intention.

Une réponse d'IA reste une proposition. Un index de requête ou une projection peut montrer une information sans devenir une source d'autorité.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé — Kristal-Biology

## Canon authoring 3.2.2

- `canon/state.index.json` décrit l'unique Logical Artifact hérité, dans son contrat exact.
- `canon/domain/legacy-v6-state.payload.json` est un input JSON canonique construit par copie logique du payload v9 antérieur et réengagé avec `compute-json-jcs`.
- `knowledge-base/sources/` conserve les sources métier natives non modifiées. Le corpus historique reste conservé comme référence et artefact de compatibilité, sans changement de sa signification ni de son autorité déclarée.

## Historique v9 préservé

Le manifest `.kristal/v9/materialization-manifest.json` est conservé, y compris le profil natif `native-blob/1` du Kristal Catho. Le blob est vérifié par son digest physique, mais le `build-v9` du Kit 3.2.2 reconstruit sa propre matérialisation `inline-json/1` et ne réutilise pas automatiquement ce manifest.

## Dérivé

`build/v9`, les caches v8, `state/`, `derived/`, `projections/materialized/`, `runtime/`, `release/` et toute couche `ai/` sont des sorties opératoires distinctes.

La factorisation v9 est **permise par le framework**, mais **n'est pas revendiquée** pour ce Kristal : aucun manifest factorisé n'était présent dans l'archive. La réduction des duplications futures doit être lossless et n'affecter aucun Logical Commitment.
