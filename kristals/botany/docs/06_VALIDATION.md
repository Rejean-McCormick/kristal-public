# Validation — Kristal-Botany

## Checks techniques exécutés

- `python tools/kristal.py check .`
- `python tools/kristal.py build-v9 .`
- vérification du blob du manifest historique ; comparaison des digests recomputés.

## Golden Commitments

- Logical Artifact : `sha256:6d5b5efdabc072fe3685fa326c459d5f2aec09aa3f63beca55f89e222d9dec3d`
- State Snapshot : `sha256:1e333720f36104ab8f7b1e375ea336f384ed4f19664f602f8f3dc183992757e2`

Les deux engagements doivent rester identiques à ceux du paquet d'origine. Si une modification de `canon/` change ces digests, c'est une nouvelle version logique, pas une simple optimisation de stockage.

## Limite

La conformité structurelle au kit n'est ni la validation de la qualité scientifique du corpus ni un contrôle par les validateurs métier historiques (ces scripts ont été conservés).
