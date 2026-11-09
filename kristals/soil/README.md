# Kristal-Soil v1.0.0

Corpus statique de référence pour la pédologie, centré sur le **profil vertical + les processus**.

Axe principal : **horizon → texture → chimie → biologie → eau → fertilité**, avec `process`, `measurement context` et `classification system` comme dimensions transversales.

## Contenu

- 847 assertions Kristal v6
- 274 référents
- 10 horizons/couches maîtres USDA représentés
- 12 classes texturales USDA
- 20 propriétés/concepts chimiques
- 15 entités/indicateurs biologiques
- 16 concepts hydriques
- 14 concepts de fertilité
- 30 processus pédologiques
- 18 méthodes d’observation/mesure
- 11 sources externes référencées

## Principe de lecture

Une valeur pédologique ne doit jamais être détachée de sa **profondeur/horizon, méthode, date, unité et conditions pertinentes**. Un horizon génétique, un horizon diagnostique et une couche d’échantillonnage sont trois objets distincts.

`fertility_state` est volontairement multivarié : le Kristal n’assimile pas fertilité, santé du sol et rendement.

## Validation

```bash
python knowledge-base/tools/validate.py
```

## Frontières

La v1.0.0 n’embarque ni la totalité des clés USDA/WRB, ni des recommandations d’engrais, ni des seuils réglementaires locaux. Ces couches doivent être versionnées séparément.
