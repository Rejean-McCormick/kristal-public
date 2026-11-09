# AI Context — SolarSystem

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:solar-system`
- State Logical Commitment: `sha256:436bd792f347185c3e21da9ef3d11400f7e32b113c6eff2b49b32fe3096f1d9b`
- Workspace profile: `layered`
- Native model: `solar_system_reference_relational_graph`
- Canonical artifacts: `12`
- Sources: `24`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et portée — Kristal-SolarSystem

## Intention d’origine (README)

# Kristal SolarSystem v1.0.0

Corpus statique et validable sur les corps du Système solaire, leurs orbites, compositions, surfaces et interactions.

- Assertions atomiques : 228
- Axes de couverture : 28
- Référents : 256
- Sources externes : 24
- Langue éditoriale : français
- Schéma : Kristal v6

Le corpus privilégie les propriétés stables. Les positions et éléments orbitaux de haute précision restent explicitement dépendants d’une époque et d’un référentiel; JPL Horizons est la source externe prescrite pour ces données dynamiques.

## Portée de la migration

Ajouter le workspace 3.2.2 sans refonte métier, changement de forme native ni modification des commitments existants. Statut du workspace : `validated`.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-SolarSystem

Le modèle décrit : **corps → orbite → composition → surface → interactions**.

## Invariant

Les positions/éléments orbitaux de haute précision dépendent d’une époque et d’un référentiel, distincts des propriétés stables.

## Ownership

La vérité propre du Kristal est la connaissance locale engagée et qualifiée par les sources existantes. Le Kristal ne possède pas les sources externes ou leur politique de publication.

## Identité

State ref : `urn:kristal:state:solar-system`. Authority ref : `urn:kristal:authority:solar-system`.

Le v9 historique possède un `canonical.logical-artifact.json` et un champ `state.scope` ; ils sont conservés.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-SolarSystem

Forme native identifiée : `solar_system_reference_relational_graph`.

Axes métier : **corps → orbite → composition → surface → interactions**.

Les positions/éléments orbitaux de haute précision dépendent d’une époque et d’un référentiel, distincts des propriétés stables.

Contrat historique conservé : `kristal_state/6.0`.

Référence d’origine : `knowledge-base/documentation/ARCHITECTURE.md`.

Les assertions, données de contexte, et registres métier restent dans `knowledge-base/` ; aucun graphe n’a été aplati ou remplacé.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique — Kristal-SolarSystem

Les assertions d’origine restent engagées, sans adjudication nouvelle. Catalogue d’origine : `knowledge-base/sources/source_catalog.json`.

**Une référence n’est pas automatiquement une autorité universelle.** Les divergences, qualifications, incertitudes et inconnus explicitement représentés doivent rester distincts.

Une IA future ne peut que proposer des évolutions à valider.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique, dérivé, matérialisation — Kristal-SolarSystem

## Adaptateur 3.2.2

`canon/domain/legacy-v6-state.payload.json` est le payload logique exact du v9 historique. `canon/state.index.json` l’engage sous le contrat existant via `compute-json-jcs`.

## Emplacements historiques conservés

- `knowledge-base/` : sources et fichiers historiques de vérité v6 selon l’autorité indiquée par le README original, autres vues reconstruites.
- `.kristal/v8/` : index et projections antérieurs.
- `.kristal/v9/` : artefact et manifestes v9 originaux.

La matérialisation historique `kristal.materialization/native-blob/1` est préservée sans substitution ; le builder 3.2.2 produit également `inline-json/1`. La compression/factorisation n’est **pas** annoncée si inexistante.
