# AI Context — Climate

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:climate`
- State Logical Commitment: `sha256:9fb8bc3743ad960ea2ef0c9f0a2ab709d4692b660f7397bd91623876966b5cb3`
- Workspace profile: `layered`
- Native model: `coupled_climate_distribution_feedback_graph`
- Canonical artifacts: `13`
- Sources: `12`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et scope — Kristal-Climate

Ce workspace apporte une enveloppe **Local Kristal 3.2.2** au corpus historique doté d’un état v9 sans modification éditoriale ni refonte sémantique.

## Forme et sujet déjà établis

forçages → réponse → rétroactions → distributions → variabilité → tendances, comme navigation et non causalité linéaire obligatoire.

Lire le `README.md` historique pour la description complète du corpus. `state_ref`: `urn:kristal:state:climate`.

## Portée de cette mise à jour

- Préserver les données sources et anciens fichiers v8/v9.
- Conserver le Logical Commitment et le State Commitment historiques.
- Ajouter un input canonique v9 recalculable, le catalogue de navigation des sources, les protocoles et le build.
- Ne pas prétendre à une qualification métier indépendante, ni à une publication v10.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Climate

## Possession logique

Ce Kristal possède les assertions statiques et identités de son corpus de référence dans le domaine `climate` et les règles d'interprétation associées.

Géométrie native déclarée : forçages → réponse → rétroactions → distributions → variabilité → tendances, comme navigation et non causalité linéaire obligatoire.

## Ce qui n'est pas possédé ou garanti

Prévision météorologique opérationnelle, bulletin courant, impacts, politique climatique et attribution d’événement particulier exclus.

Les sources amont et leur autorité éditoriale ne sont pas contrôlées par cet état local ; la présence d'une assertion ne la transforme pas en vérité universelle.

## Documents historiques de frontière / architecture

- `knowledge-base/documentation/ARCHITECTURE.md`
- `knowledge-base/documentation/CLIMATE_MODEL.md`
- `knowledge-base/documentation/CONTENT_BOUNDARY.md`
- `knowledge-base/documentation/SEMANTIC_GUARDRAILS.md`

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-Climate

**Kind local** : `coupled_climate_distribution_feedback_graph`.

**Géométrie conservée** : forçages → réponse → rétroactions → distributions → variabilité → tendances, comme navigation et non causalité linéaire obligatoire.

**Invariant essentiel** : climat ≠ météo ; anomalie ≠ erreur ; forçage ≠ rétroaction ; tendance ≠ attribution ; rétroaction positive ≠ emballement nécessaire.

Le contrat engagé par le v9 historique reste `kristal.compat.v6-state-logical/1.0`. Ce contrat utilise le payload d'origine engagé dans v9 (corpus sémantique natif pour Catho ; `kristal_state` v6 pour les autres), avec les informations de provenance existantes. Cette migration ne convertit pas ce graphe en ontologie uniforme, en table ou en pipeline artificiel.

La vue authoring `canon/domain/legacy-v6-state.payload.json` est une photographie canonique du payload existant. Les fichiers du domaine dans `knowledge-base` restent inchangés. Le maintien en synchronisation future de ces deux sources exige une procédure éditoriale explicite.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique — Kristal-Climate

## Preuves et sources

La bibliographie / provenance historique est accessible dans `knowledge-base/sources/source-catalog.json`. Sa vue normalisée est `sources/source-catalog.json` (12 entrées). Les métadonnées complètes et politiques historiques demeurent dans le fichier d'origine ou dans le payload engagé.

## Interprétation

Une source, une assertion, un auteur et un engagement logique ont des fonctions distinctes : provenance ≠ autorité ≠ vérité. Un désaccord ne doit pas être résolu sans justifier l'autorité. `unknown` ≠ `false`.

Invariant disciplinaire : climat ≠ météo ; anomalie ≠ erreur ; forçage ≠ rétroaction ; tendance ≠ attribution ; rétroaction positive ≠ emballement nécessaire.

Une réponse d'IA reste une proposition. Un index de requête ou une projection peut montrer une information sans devenir une source d'autorité.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé — Kristal-Climate

## Canon authoring 3.2.2

- `canon/state.index.json` décrit l'unique Logical Artifact hérité, dans son contrat exact.
- `canon/domain/legacy-v6-state.payload.json` est un input JSON canonique construit par copie logique du payload v9 antérieur et réengagé avec `compute-json-jcs`.
- `knowledge-base/sources/` conserve les sources métier natives non modifiées. Le corpus historique reste conservé comme référence et artefact de compatibilité, sans changement de sa signification ni de son autorité déclarée.

## Historique v9 préservé

Le manifest `.kristal/v9/materialization-manifest.json` est conservé, y compris le profil natif `native-blob/1` du Kristal Catho. Le blob est vérifié par son digest physique, mais le `build-v9` du Kit 3.2.2 reconstruit sa propre matérialisation `inline-json/1` et ne réutilise pas automatiquement ce manifest.

## Dérivé

`build/v9`, les caches v8, `state/`, `derived/`, `projections/materialized/`, `runtime/`, `release/` et toute couche `ai/` sont des sorties opératoires distinctes.

La factorisation v9 est **permise par le framework**, mais **n'est pas revendiquée** pour ce Kristal : aucun manifest factorisé n'était présent dans l'archive. La réduction des duplications futures doit être lossless et n'affecter aucun Logical Commitment.
