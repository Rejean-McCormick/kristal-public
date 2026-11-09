# Validation du domaine et lifecycle v10

## Invariants structurels

- 142 IDs Q&A uniques ;
- toutes les routes Q&A résolvent vers des IDs existants ;
- toutes les références de preuve packagées existent ;
- le miroir legacy du state reste byte-identique au canon 3.2.2 ;
- `READ MODEL != CANONICAL STATE` ;
- `MODEL OUTPUT != AUTHORITY`.

## Invariants épistémiques

- 120 scénarios historiques + 36 archétypes V2 ne deviennent jamais 156 validations indépendantes ;
- scénario récurrent ≠ validation marché ;
- documenté ≠ implémenté ≠ testé ≠ qualifié ≠ déployé ≠ commercialisé ;
- modularité/séparation ≠ preuve de confinement ;
- E2E reste non vérifié sans artefact reproductible attaché.

## Tests de reconstruction

1. `python knowledge-base/tools/validate.py`
2. `python tools/kristal.py check .`
3. `python tools/kristal.py build-v9 .`
4. comparer le commitment du nouveau `build/v9/state-snapshot.json` au commitment v9 historique attendu.

## Logical Commitments

Le Logical Artifact canonique conserve `sha256:7b93562350b278aa9a126d28b0c3712e17847cac88620b97c9f6d31c36fcbe71`. Le State Snapshot attendu conserve `sha256:97bf4babbe6111bd71cc2f4687c1320da4466f91aca3da2dcd37d9c8a83a224e`.

## Critères de publication

Le package reste `building` même si les validations structurelles passent : une publication doit être une décision explicite, précédée d'une qualification du commit exact. Les limites épistémiques ouvertes ne doivent pas être masquées par un PASS structurel.
