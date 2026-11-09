# FoodKristal — paquet consolidé

Le paquet a été réorganisé avec des noms stables, explicites et sans numéro de version dans les dossiers.

```text
FoodKristal/
├── source-manager/          # application Python et CLI
├── knowledge-base/sources/source-catalog/          # providers, sources de référence et règles d’acquisition
├── knowledge-base/documentation/           # politiques, mapping provider et schéma
├── knowledge-base/examples/                # exemples de manifeste et de source_refs
└── external-source-library/ # acquisitions locales; vide au départ
```

L’archive imbriquée d’origine et les caches Python ne sont pas conservés. Les futurs snapshots sont organisés dans des dossiers explicites et sans copies de publication redondantes.

## Kristal v9

Ce repo est migré vers **Kristal 9.0.0-draft.1 — Semantic State Architecture** sans supprimer les surfaces v6/v8 existantes.

- canon v9 : le source catalog natif (`providers`, `reference-sources`, `acquisition-overrides`);
- snapshot logique immuable : `.kristal/v9/state-snapshot.json`;
- matérialisation(s) : `.kristal/v9/materialization.*.json`;
- projection portable v6 : conservée sous `.kristal/v8/portable-state.kristal-state.json` et explicitement dérivée;
- indexes/read models v8 : restent dérivés et reconstruisibles;
- identité logique v9 : séparée des digests physiques des fichiers.

Voir `.kristal/v9/README.md` et `V9-MIGRATION.md`.
