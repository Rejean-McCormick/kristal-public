# AI Context — Geology

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:geology`
- State Logical Commitment: `sha256:c6182de3ca806c4086ce055fed58b5ac29d9c40761eeebebcc505a73ac4e3d28`
- Workspace profile: `layered`
- Native model: `stratigraphic_process_event_temporal_graph`
- Canonical artifacts: `14`
- Sources: `18`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intentions et scope — Kristal-Geology

Le sujet est : **Matière, processus, structure, enregistrement stratigraphique et événement géologique.**

Cette opération ajoute l'enveloppe Local Kristal 3.2.2 au v9 existant, sans changer le contrat logique ni la vérité métier. Le v9 historique est décrit dans `V9_MIGRATION.md` et `.kristal/v9/migration-report.json`. La décision du canon préexistante est **`v6-canonical-state-bridge`**, depuis **`knowledge-base/corpus/geology.kristal-state.json`**.

Les ressources v6/v8 sont conservées sans renommage ni réécriture.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique

## Possède

Matière, processus, structure, enregistrement stratigraphique et événement géologique.

## Distinction non négociable

Processus ≠ événement; temps géologique ≠ unité rocheuse; discordance ≠ couche déposée.

## Ne possède pas

La propriété des contenus, versions et interprétations futures de sources externes; ni les publications/activations en réseau. Les autres Kristals fédérés ne fusionnent pas leurs identités automatiquement avec ce modèle.

La définition éditoriale source, lorsqu'elle existe, est sous `knowledge-base/documentation/` et dans le README historique.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif

- **Kind** : `stratigraphic_process_event_temporal_graph`
- **Description** : Matière, processus, structure, enregistrement stratigraphique et événement géologique.
- **Axes et coordonnées** : Matière, processus, structure, stratigraphie, temps et événements.
- **Invariant** : Processus ≠ événement; temps géologique ≠ unité rocheuse; discordance ≠ couche déposée.

## Canal canonique de migration

Le Logical Artifact `urn:kristal:geology:canonical` possède le contrat `kristal.v6-state-reference/1.0`. Son payload authoring se trouve dans `canon/domain/geology.logical-payload.json` et est recalculé sans commitment `precomputed`.

Les modèles métier historiques sont dans `knowledge-base/` : leur forme native demeure autoritaire pour l'interprétation ; la seule enveloppe 3.2.2 ne redéfinit pas les sémantiques.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique

Les sources documentaires / preuves et les assertions sont des plans différents. Processus ≠ événement; temps géologique ≠ unité rocheuse; discordance ≠ couche déposée.

- Source ≠ assertion validée ; provenance ≠ autorité.
- Inconnu ≠ faux ; une divergence doit être conservée avec sa provenance.
- Les sorties d'IA sont des propositions, jamais des faits admis automatiquement.
- Les politiques et limites spécifiques au domaine, lorsqu'elles existent, se trouvent dans `knowledge-base/documentation` et/ou `knowledge-base/sources`.

Nombre de références sourcées cataloguées dans l'enveloppe : **18**. Ce nombre représente les enregistrements explicitement trouvés, pas une certification de complétude ni un classement d'autorité.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé

## Canon

- Entrée du build 3.2.2 : `canon/domain/geology.logical-payload.json` (payload logique identique au snapshot historique).
- Source métier historique : `knowledge-base/corpus/geology.kristal-state.json`.
- Legacy State v9 : `.kristal/v9/state-snapshot.json`.

La stratégie `v6-canonical-state-bridge` doit rester explicite : les bridges v6 référencent la source historique et ne représentent **pas** une nouvelle factorisation ou refonte du graphe métier.

## Dérivés / représentations

- `build/v9` est un build reconstruit (fallback `inline-json/1` du kit).
- `.kristal/v9/materialization.*.json` : profils physiques antérieurs préservés, inventoriés dans `materializations/existing-v9-registry.json`.
- `.kristal/v8` : read models / projection portable antérieurs.

Les engagements logiques sont indépendants de l'encodage, compression et segmentation physiques.
