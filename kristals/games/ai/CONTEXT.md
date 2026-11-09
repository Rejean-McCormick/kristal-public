# AI Context — Games

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:games`
- State Logical Commitment: `sha256:89dca6fbac6c23f463d65d97b8d190d4d6703ec73972ec611d06a3eee9eb546e`
- Workspace profile: `layered`
- Native model: `state_rule_action_transition_graph`
- Canonical artifacts: `1`
- Sources: `18`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intentions et scope — Kristal-Games

Le sujet est : **Jeux comme systèmes : règles, états, actions, transitions, objectifs et résultats.**

Cette opération ajoute l'enveloppe Local Kristal 3.2.2 au v9 existant, sans changer le contrat logique ni la vérité métier. Le v9 historique est décrit dans `V9_MIGRATION.md` et `.kristal/v9/migration-report.json`. La décision du canon préexistante est **`v6-canonical-state-bridge`**, depuis **`knowledge-base/corpus/games.kristal-state.json`**.

Les ressources v6/v8 sont conservées sans renommage ni réécriture.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique

## Possède

Jeux comme systèmes : règles, états, actions, transitions, objectifs et résultats.

## Distinction non négociable

Règle, état, action, transition, objectif et résultat ne sont pas des synonymes.

## Ne possède pas

La propriété des contenus, versions et interprétations futures de sources externes; ni les publications/activations en réseau. Les autres Kristals fédérés ne fusionnent pas leurs identités automatiquement avec ce modèle.

La définition éditoriale source, lorsqu'elle existe, est sous `knowledge-base/documentation/` et dans le README historique.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif

- **Kind** : `state_rule_action_transition_graph`
- **Description** : Jeux comme systèmes : règles, états, actions, transitions, objectifs et résultats.
- **Axes et coordonnées** : État, règle, action, transition, objectif, résultat.
- **Invariant** : Règle, état, action, transition, objectif et résultat ne sont pas des synonymes.

## Canal canonique de migration

Le Logical Artifact `urn:kristal:games:canonical` possède le contrat `kristal.v6-state-reference/1.0`. Son payload authoring se trouve dans `canon/domain/games.logical-payload.json` et est recalculé sans commitment `precomputed`.

Les modèles métier historiques sont dans `knowledge-base/` : leur forme native demeure autoritaire pour l'interprétation ; la seule enveloppe 3.2.2 ne redéfinit pas les sémantiques.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique

Les sources documentaires / preuves et les assertions sont des plans différents. Règle, état, action, transition, objectif et résultat ne sont pas des synonymes.

- Source ≠ assertion validée ; provenance ≠ autorité.
- Inconnu ≠ faux ; une divergence doit être conservée avec sa provenance.
- Les sorties d'IA sont des propositions, jamais des faits admis automatiquement.
- Les politiques et limites spécifiques au domaine, lorsqu'elles existent, se trouvent dans `knowledge-base/documentation` et/ou `knowledge-base/sources`.

Nombre de références sourcées cataloguées dans l'enveloppe : **18**. Ce nombre représente les enregistrements explicitement trouvés, pas une certification de complétude ni un classement d'autorité.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé

## Canon

- Entrée du build 3.2.2 : `canon/domain/games.logical-payload.json` (payload logique identique au snapshot historique).
- Source métier historique : `knowledge-base/corpus/games.kristal-state.json`.
- Legacy State v9 : `.kristal/v9/state-snapshot.json`.

La stratégie `v6-canonical-state-bridge` doit rester explicite : les bridges v6 référencent la source historique et ne représentent **pas** une nouvelle factorisation ou refonte du graphe métier.

## Dérivés / représentations

- `build/v9` est un build reconstruit (fallback `inline-json/1` du kit).
- `.kristal/v9/materialization.*.json` : profils physiques antérieurs préservés, inventoriés dans `materializations/existing-v9-registry.json`.
- `.kristal/v8` : read models / projection portable antérieurs.

Les engagements logiques sont indépendants de l'encodage, compression et segmentation physiques.
