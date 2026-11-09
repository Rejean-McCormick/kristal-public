# Kristal-Mind

**Version 1.0.0 — Kristal Standard 6.0**

Kristal-Mind est un corpus statique et traçable des fonctions cognitives fondamentales. Sa navigation principale suit :

`perception → représentation → mémoire → décision → action`

Cette flèche est une **colonne vertébrale de navigation**, pas une affirmation de sérialité stricte. Le corpus encode explicitement les boucles de rétroaction et les fonctions transversales (attention, contrôle exécutif, métacognition, apprentissage).

## Canonique

- `knowledge-base/corpus/mind.kristal-state.json` — état Kristal v6 canonique
- `knowledge-base/corpus/referents.json` — registre de référents
- `knowledge-base/sources/source-catalog.json` — bibliographie traçable
- `knowledge-base/corpus/process-graph.json` — projection de graphe dérivée
- `knowledge-base/corpus/state-process-map.json` — projection états ↔ processus
- `knowledge-base/corpus/coverage-report.json` — couverture et frontières
- `knowledge-base/tools/validate.py` — validation structurelle et sémantique locale

## Frontière

Le Kristal décrit les **fonctions cognitives**, leurs états et leurs relations. Il ne constitue ni un manuel de psychiatrie, ni une ontologie neuroanatomique, ni une théorie de la conscience. Les localisations cérébrales détaillées sont volontairement laissées à `Kristal-HumanBody` / un futur Kristal de neurosciences.

## Principe épistémique

Les assertions sont sourcées. Les constructions dépendantes d’un modèle (p. ex. seuil décisionnel) ou conditionnelles (p. ex. reconsolidation) reçoivent une valuation `theory_dependence` et/ou une note explicite. La validation du paquet vérifie la structure, les références et la couverture; elle ne transforme pas la littérature scientifique en autorité absolue.
