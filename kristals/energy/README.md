# Kristal-Energy

**Version 1.0.0 — Kristal Standard 6.0**

Kristal-Energy est un corpus statique et traçable des **systèmes et flux énergétiques**. Son axe principal est :

`source → conversion → stockage → transport/distribution → consommation/usage → pertes`

Ce parcours est une vue de flux, pas une affirmation qu’un système réel contient toujours chaque étape. Le modèle distingue explicitement **énergie primaire**, **vecteurs/énergie secondaire**, **énergie finale** et **énergie utile**.

## Canonique

- `knowledge-base/corpus/energy.kristal-state.json` — état Kristal v6 canonique
- `knowledge-base/corpus/referents.json` — registre des concepts
- `knowledge-base/sources/source-catalog.json` — catalogue de sources
- `knowledge-base/corpus/energy-flow-graph.json` — graphe dérivé complet
- `knowledge-base/corpus/conversion-map.json` — projection des conversions
- `knowledge-base/corpus/storage-map.json` — projection du stockage
- `knowledge-base/tools/validate.py` — validation locale

## Principe clé

Une perte de système n’est pas une destruction d’énergie. Elle signifie qu’une fraction de l’énergie n’atteint pas la forme ou le service utile visé dans le périmètre étudié. Le corpus sépare donc conservation, rendement, pertes de conversion, transport, autodécharge, chaleur rejetée et dégradation de qualité énergétique.

## Frontière

Le Kristal décrit la structure physique et comptable des systèmes énergétiques. Il ne remplace pas Physique, Chimie, Economics, Climate, Materials ou un futur Kristal-Grid détaillé.

### Taille

- Référents : **124**
- Assertions : **210**
- Sources : **17**
