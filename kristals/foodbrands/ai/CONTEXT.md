# AI Context — FoodBrands

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:foodbrands`
- State Logical Commitment: `sha256:e41df7d28e730954db8ecea433571c99d77c09db3f7ebc0aee4b8480833b1eb9`
- Workspace profile: `layered`
- Native model: `controlled_source_catalog`
- Canonical artifacts: `6`
- Sources: `12`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intentions et scope — Kristal-FoodBrands

Le sujet est : **Registre contrôlé des fournisseurs, sources de référence et règles explicites d’acquisition.**

Cette opération ajoute l'enveloppe Local Kristal 3.2.2 au v9 existant, sans changer le contrat logique ni la vérité métier. Le v9 historique est décrit dans `V9_MIGRATION.md` et `.kristal/v9/migration-report.json`. La décision du canon préexistante est **`native-source-catalog`**, depuis **`knowledge-base/sources/source-catalog/reference-sources.json`**.

Les ressources v6/v8 sont conservées sans renommage ni réécriture.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique

## Possède

Registre contrôlé des fournisseurs, sources de référence et règles explicites d’acquisition.

## Distinction non négociable

Un fournisseur ou une source ne devient pas une vérité nutritionnelle par son inscription au catalogue.

## Ne possède pas

La propriété des contenus, versions et interprétations futures de sources externes; ni les publications/activations en réseau. Les autres Kristals fédérés ne fusionnent pas leurs identités automatiquement avec ce modèle.

La définition éditoriale source, lorsqu'elle existe, est sous `knowledge-base/documentation/` et dans le README historique.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif

- **Kind** : `controlled_source_catalog`
- **Description** : Registre contrôlé des fournisseurs, sources de référence et règles explicites d’acquisition.
- **Axes et coordonnées** : Fournisseurs, références et règles d’acquisition (trois membres distincts).
- **Invariant** : Un fournisseur ou une source ne devient pas une vérité nutritionnelle par son inscription au catalogue.

## Canal canonique de migration

Le Logical Artifact `urn:kristal:foodbrands:canonical` possède le contrat `foodbrands.source-catalog/1.0`. Son payload authoring se trouve dans `canon/domain/foodbrands.logical-payload.json` et est recalculé sans commitment `precomputed`.

Les modèles métier historiques sont dans `knowledge-base/` : leur forme native demeure autoritaire pour l'interprétation ; la seule enveloppe 3.2.2 ne redéfinit pas les sémantiques.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique

Les sources documentaires / preuves et les assertions sont des plans différents. Un fournisseur ou une source ne devient pas une vérité nutritionnelle par son inscription au catalogue.

- Source ≠ assertion validée ; provenance ≠ autorité.
- Inconnu ≠ faux ; une divergence doit être conservée avec sa provenance.
- Les sorties d'IA sont des propositions, jamais des faits admis automatiquement.
- Les politiques et limites spécifiques au domaine, lorsqu'elles existent, se trouvent dans `knowledge-base/documentation` et/ou `knowledge-base/sources`.

Nombre de références sourcées cataloguées dans l'enveloppe : **12**. Ce nombre représente les enregistrements explicitement trouvés, pas une certification de complétude ni un classement d'autorité.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé

## Canon

- Entrée du build 3.2.2 : `canon/domain/foodbrands.logical-payload.json` (payload logique identique au snapshot historique).
- Source métier historique : `knowledge-base/sources/source-catalog/reference-sources.json`.
- Legacy State v9 : `.kristal/v9/state-snapshot.json`.

La stratégie `native-source-catalog` doit rester explicite : les bridges v6 référencent la source historique et ne représentent **pas** une nouvelle factorisation ou refonte du graphe métier.

## Dérivés / représentations

- `build/v9` est un build reconstruit (fallback `inline-json/1` du kit).
- `.kristal/v9/materialization.*.json` : profils physiques antérieurs préservés, inventoriés dans `materializations/existing-v9-registry.json`.
- `.kristal/v8` : read models / projection portable antérieurs.

Les engagements logiques sont indépendants de l'encodage, compression et segmentation physiques.
