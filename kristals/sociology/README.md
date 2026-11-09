# Kristal-Sociology

**Version 1.0.0 — Kristal Standard 6.0**

Kristal-Sociology est un corpus statique et traçable des **structures et interactions sociales**. Son noyau couvre :

`individus ↔ interactions ↔ groupes ↔ rôles ↔ institutions ↔ normes ↔ réseaux`

Ce parcours n’est pas une chaîne causale. Le corpus utilise un **graphe multi-échelle** : micro (acteurs, interactions, rôles), méso (groupes, organisations, réseaux) et macro (institutions, normes, stratification).

## Canonique

- `knowledge-base/corpus/sociology.kristal-state.json` — état Kristal v6 canonique
- `knowledge-base/corpus/referents.json` — registre des concepts
- `knowledge-base/sources/source-catalog.json` — sources traçables
- `knowledge-base/corpus/social-structure-graph.json` — projection relationnelle dérivée
- `knowledge-base/corpus/network-projection.json` — projection réseau dérivée
- `knowledge-base/corpus/coverage-report.json` — couverture, frontières et quality gates
- `knowledge-base/tools/validate.py` — validation locale

## Frontière

Ce Kristal décrit les formes sociales générales. Il ne cherche pas à remplacer un Kristal dédié au droit, à l’économie, à la politique, à la psychologie clinique, à l’anthropologie ou à la démographie. Les domaines voisins sont reliables par référents externes futurs.

## Principe épistémique

Les assertions sont atomiques et sourcées. Les concepts fortement théoriques (isomorphisme institutionnel, capital social, trous structuraux) portent une dépendance théorique explicite. Une association observée dans un réseau n’est jamais encodée comme preuve automatique d’influence causale.
