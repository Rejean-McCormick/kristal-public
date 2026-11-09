# Kristal-FoodScience v1.0.0

Corpus statique de science des aliments au format **Kristal v6**.

## Axe canonique

**composition → transformation → structure → propriétés → stabilité / sécurité**

Le Kristal décrit comment une matrice alimentaire et sa composition, soumises à un historique de procédé et de conservation, produisent une structure qui détermine des propriétés mesurables et des trajectoires de stabilité. L’innocuité est modélisée séparément par dangers, mesures de maîtrise, surveillance, validation et preuve.

## Contenu

- **1013 assertions**
- **382 référents**
- 20 familles de matrices alimentaires
- 34 constituants/fractions
- 46 transformations
- 26 structures
- 41 propriétés
- 30 mécanismes de stabilité/altération
- 21 catégories/exemples de dangers
- 25 mesures de maîtrise
- 30 méthodes analytiques
- 11 sources de référence

## Garde-fous sémantiques

1. **activité de l’eau ≠ teneur en eau**;
2. **pH ≠ acidité titrable**;
3. **stabilité ≠ sécurité**;
4. **altération ≠ présence d’un pathogène**;
5. **transformation ≠ résultat garanti** : temps, température, pression, géométrie, formulation et matrice comptent;
6. **durée de conservation ≠ durée de sécurité** sans base expérimentale/validation explicite;
7. une valeur de composition conserve l’identité de l’aliment, son état, l’échantillonnage et la méthode analytique;
8. aucun seuil réglementaire n’est traité comme universel.

## Validation

```bash
python knowledge-base/tools/validate.py
```

Le validateur vérifie les schémas, les sources, l’unicité des référents et plusieurs garde-fous de domaine.

## Kristal v9

Ce repo est migré vers **Kristal 9.0.0-draft.1 — Semantic State Architecture** sans supprimer les surfaces v6/v8 existantes.

- canon v9 : le state v6 canonique `knowledge-base/corpus/foodscience.kristal-state.json`;
- snapshot logique immuable : `.kristal/v9/state-snapshot.json`;
- matérialisation(s) : `.kristal/v9/materialization.*.json`;
- projection portable v6 : conservée sous `.kristal/v8/portable-state.kristal-state.json` et explicitement dérivée;
- indexes/read models v8 : restent dérivés et reconstruisibles;
- identité logique v9 : séparée des digests physiques des fichiers.

Voir `.kristal/v9/README.md` et `V9-MIGRATION.md`.
