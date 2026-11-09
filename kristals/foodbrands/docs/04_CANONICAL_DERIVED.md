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
