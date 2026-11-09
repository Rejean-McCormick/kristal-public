# Validation — Kristal-ControlSystems

## Checks techniques exécutés

- `python tools/kristal.py check .`
- `python tools/kristal.py build-v9 .`
- vérification du blob du manifest historique ; comparaison des digests recomputés.

## Golden Commitments

- Logical Artifact : `sha256:aa77aae7091888cfbd81c1fe3e0820fc26a01569b65e533153de6da90687e1c1`
- State Snapshot : `sha256:bbed949bcdefddcf6b9ceba55a2d6588ed3015fe9d9078c5614bee2a4d9287f7`

Les deux engagements doivent rester identiques à ceux du paquet d'origine. Si une modification de `canon/` change ces digests, c'est une nouvelle version logique, pas une simple optimisation de stockage.

## Limite

La conformité structurelle au kit n'est ni la validation de la qualité scientifique du corpus ni un contrôle par les validateurs métier historiques (ces scripts ont été conservés).
