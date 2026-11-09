# Kristal-Nutrition v1.0.0

Corpus statique de référence décrivant la chaîne **aliment → nutriment → digestion/absorption → métabolisme → besoin → effet physiologique**.

## Périmètre

Le Kristal représente la grammaire fondamentale de la nutrition humaine. Il distingue la composition d’un aliment de ce qui est ingéré, absorbé, métabolisé et finalement relié à une fonction physiologique. Il modélise aussi les principaux types de valeurs de référence nutritionnelle sans figer dans le noyau des tableaux numériques dépendants d’une édition ou d’une population.

## État

- Kristal v6
- 213 référents
- 647 assertions atomiques
- 9 sources de référence/catalogue
- assertions déterministes, corpus statique, manifeste SHA-256

## Fichiers principaux

- `knowledge-base/corpus/nutrition.kristal-state.json`
- `knowledge-base/corpus/nutrition.referent-registry.json`
- `knowledge-base/corpus/nutrition-chain-model.json`
- `knowledge-base/corpus/food-composition-model.json`
- `knowledge-base/corpus/absorption-model.json`
- `knowledge-base/corpus/requirement-model.json`
- `knowledge-base/corpus/physiological-effect-model.json`

## Invariants critiques

- aliment ≠ nutriment
- composition ≠ quantité consommée
- apport ingéré ≠ quantité absorbée
- absorption ≠ biodisponibilité systémique ≠ statut
- statut ≠ effet physiologique
- besoin individuel ≠ valeur de référence de population
- UL ≠ cible recommandée
- apport inadéquat ≠ diagnostic de carence
- essentiel ≠ bénéfique sans limite
- fonction physiologique ≠ bénéfice clinique démontré à toute dose

## Frontières

Hors périmètre : prescription nutritionnelle individualisée, traitement des maladies, toxicologie alimentaire exhaustive, tables numériques DRI versionnées, base complète de composition alimentaire, pharmacologie, cuisine et biochimie exhaustive.
