# Kristal-Games v1.0.0

Corpus statique et validé décrivant les jeux comme systèmes d’états, règles, actions, transitions, objectifs et résultats.

Navigation canonique : **état → règles → actions possibles → transition → objectif → résultat**.

Le modèle est volontairement non linéaire : information, stratégie, hasard, dynamique, apprentissage et expérience traversent le pipeline.

- Référents : 199
- Assertions atomiques : 397
- Sources : 18
- Kristal Standard : 6.0
- State ID : `sha256:f5035ca81d97faf07d2a1be27da601429b5bea9a81b4775c2e6f468ba84ea104`

## Kristal v9

Ce repo est migré vers **Kristal 9.0.0-draft.1 — Semantic State Architecture** sans supprimer les surfaces v6/v8 existantes.

- canon v9 : le state v6 canonique `knowledge-base/corpus/games.kristal-state.json`;
- snapshot logique immuable : `.kristal/v9/state-snapshot.json`;
- matérialisation(s) : `.kristal/v9/materialization.*.json`;
- projection portable v6 : conservée sous `.kristal/v8/portable-state.kristal-state.json` et explicitement dérivée;
- indexes/read models v8 : restent dérivés et reconstruisibles;
- identité logique v9 : séparée des digests physiques des fichiers.

Voir `.kristal/v9/README.md` et `V9-MIGRATION.md`.
