# AI Context — Soil

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:soil`
- State Logical Commitment: `sha256:9b39862e9f40aec5991c0f7d12237fd83e23673a3793c3e1cee04b31fbfaea72`
- Workspace profile: `layered`
- Native model: `vertical_soil_profile_process_graph`
- Canonical artifacts: `1`
- Sources: `11`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et portée — Kristal-Soil

## Intention d’origine (README)

# Kristal-Soil v1.0.0

Corpus statique de référence pour la pédologie, centré sur le **profil vertical + les processus**.

Axe principal : **horizon → texture → chimie → biologie → eau → fertilité**, avec `process`, `measurement context` et `classification system` comme dimensions transversales.

## Portée de la migration

Ajouter le workspace 3.2.2 sans refonte métier, changement de forme native ni modification des commitments existants. Statut du workspace : `validated`.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Soil

Le modèle décrit : **horizon → texture → chimie → biologie → eau → fertilité**.

## Invariant

Une mesure conserve profondeur/horizon, méthode, date, unité et conditions ; horizon génétique ≠ horizon diagnostique ≠ couche d’échantillonnage.

## Ownership

La vérité propre du Kristal est la connaissance locale engagée et qualifiée par les sources existantes. Le Kristal ne possède pas les sources externes ou leur politique de publication.

## Identité

State ref : `urn:kristal:state:soil`. Authority ref : `urn:kristal:authority:soil`.

Le v9 historique possède un `canonical.logical-artifact.json` et un champ `state.scope` ; ils sont conservés.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-Soil

Forme native identifiée : `vertical_soil_profile_process_graph`.

Axes métier : **horizon → texture → chimie → biologie → eau → fertilité**.

Une mesure conserve profondeur/horizon, méthode, date, unité et conditions ; horizon génétique ≠ horizon diagnostique ≠ couche d’échantillonnage.

Contrat historique conservé : `kristal_state/6.0`.

Référence d’origine : `knowledge-base/documentation/ARCHITECTURE.md`.

Les assertions, données de contexte, et registres métier restent dans `knowledge-base/` ; aucun graphe n’a été aplati ou remplacé.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique — Kristal-Soil

Les assertions d’origine restent engagées, sans adjudication nouvelle. Catalogue d’origine : `external-source-library/source-store.json`.

**Une référence n’est pas automatiquement une autorité universelle.** Les divergences, qualifications, incertitudes et inconnus explicitement représentés doivent rester distincts.

Une IA future ne peut que proposer des évolutions à valider.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique, dérivé, matérialisation — Kristal-Soil

## Adaptateur 3.2.2

`canon/domain/legacy-v6-state.payload.json` est le payload logique exact du v9 historique. `canon/state.index.json` l’engage sous le contrat existant via `compute-json-jcs`.

## Emplacements historiques conservés

- `knowledge-base/` : sources et fichiers historiques de vérité v6 selon l’autorité indiquée par le README original, autres vues reconstruites.
- `.kristal/v8/` : index et projections antérieurs.
- `.kristal/v9/` : artefact et manifestes v9 originaux.

La matérialisation historique `kristal.materialization/native-blob/1` est préservée sans substitution ; le builder 3.2.2 produit également `inline-json/1`. La compression/factorisation n’est **pas** annoncée si inexistante.
