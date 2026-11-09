# Validation — Kristal-CivilEngineering

## Checks techniques exécutés

- `python tools/kristal.py check .`
- `python tools/kristal.py build-v9 .`
- vérification du blob du manifest historique ; comparaison des digests recomputés.

## Golden Commitments

- Logical Artifact : `sha256:bcbe7f3eb4011b4fd8cda2af25ef843e1d436fedef54501ba4f9ea61f30d6ca6`
- State Snapshot : `sha256:c7c8ae8ab00abd528514c04908214521cd907319bf08a5b7fd4b04618df64434`

Les deux engagements doivent rester identiques à ceux du paquet d'origine. Si une modification de `canon/` change ces digests, c'est une nouvelle version logique, pas une simple optimisation de stockage.

## Limite

La conformité structurelle au kit n'est ni la validation de la qualité scientifique du corpus ni un contrôle par les validateurs métier historiques (ces scripts ont été conservés).
