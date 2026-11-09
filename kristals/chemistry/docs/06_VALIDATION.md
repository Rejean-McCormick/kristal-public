# Validation — Kristal-Chemistry

## Checks techniques exécutés

- `python tools/kristal.py check .`
- `python tools/kristal.py build-v9 .`
- vérification du blob du manifest historique ; comparaison des digests recomputés.

## Golden Commitments

- Logical Artifact : `sha256:6f2d8bc02c54ad9dc24d7733cdd1d879c9171ee6a02e829364ae8dbecda0cc7a`
- State Snapshot : `sha256:b224a3e8d4855d8160388abebd676e4c747bcd5c197264f13245d61f4f950efc`

Les deux engagements doivent rester identiques à ceux du paquet d'origine. Si une modification de `canon/` change ces digests, c'est une nouvelle version logique, pas une simple optimisation de stockage.

## Limite

La conformité structurelle au kit n'est ni la validation de la qualité scientifique du corpus ni un contrôle par les validateurs métier historiques (ces scripts ont été conservés).
