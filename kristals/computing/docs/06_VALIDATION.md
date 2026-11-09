# Validation — Kristal-Computing

## Checks techniques exécutés

- `python tools/kristal.py check .`
- `python tools/kristal.py build-v9 .`
- vérification du blob du manifest historique ; comparaison des digests recomputés.

## Golden Commitments

- Logical Artifact : `sha256:fa5181f99901d83b87467a7be6c4005c04f5715bbdd8d3646a4789d9f302eba7`
- State Snapshot : `sha256:f746d0bc2a85c30cf4d2c8006583a88487bcbd9cce3ab8bd3df6fe8c5086c128`

Les deux engagements doivent rester identiques à ceux du paquet d'origine. Si une modification de `canon/` change ces digests, c'est une nouvelle version logique, pas une simple optimisation de stockage.

## Limite

La conformité structurelle au kit n'est ni la validation de la qualité scientifique du corpus ni un contrôle par les validateurs métier historiques (ces scripts ont été conservés).
