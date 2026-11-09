# Migration vers Local Kristal 3.2.2

## Stratégie

Migration non destructive : ajout de l’enveloppe `kristal.local-workspace/3.2.0` autour du corpus PoliceOps existant.

## Non-modifié

- corpus natif v5;
- `state_id` et content hash natifs;
- anciens artefacts `.kristal/v8` et `.kristal/v9`;
- Source Store snapshot et outils métier.

## Ajouté

- `kristal.workspace.json`;
- `canon/state.index.json`;
- `sources/source-catalog.json`;
- documentation normative `docs/00` à `docs/07`;
- `AGENTS.md`;
- `tools/kristal.py` du kit 3.2.2;
- nouveaux dossiers lifecycle/build prévus par le kit.

## Compatibilité attendue

Le Logical Commitment natif et le State Commitment reconstruits doivent rester identiques aux valeurs du build v9 legacy. Toute divergence est un échec de migration et doit être investiguée avant livraison.

## Commitment natif préservé

Le test initial avec `compute-json-jcs` du Local Kit 3.2.2 a produit un commitment différent, car il enveloppe le JSON brut alors que la migration PoliceOps v9 historique applique la `hash_target_policy` native avant commitment. La configuration finale utilise donc `precomputed` avec le commitment déjà qualifié `sha256:5cf1bea721c665905139b5aedcaeaed4ffe570786e6d64bd868c251ffaaebd18`. Le State Commitment attendu reste `sha256:46b7848a7c82b0a98f735fe993dcfab545d50f47ce44f1c8bc5ab2875f9f3ca1`.
