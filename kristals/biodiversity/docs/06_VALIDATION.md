# Validation — Kristal-Biodiversity

## Checks techniques exécutés

- `python tools/kristal.py check .`
- `python tools/kristal.py build-v9 .`
- vérification du blob du manifest historique ; comparaison des digests recomputés.

## Golden Commitments

- Logical Artifact : `sha256:67e45b65c045ae8a6d2217f6da8f3d320ac90f25a9bd925a8642bf3b02f6e9fe`
- State Snapshot : `sha256:bf0b09fc34f0bf980c4c4f31a8be4edcd093b5f5b6a8da2cbfc58fb17205277e`

Les deux engagements doivent rester identiques à ceux du paquet d'origine. Si une modification de `canon/` change ces digests, c'est une nouvelle version logique, pas une simple optimisation de stockage.

## Limite

La conformité structurelle au kit n'est ni la validation de la qualité scientifique du corpus ni un contrôle par les validateurs métier historiques (ces scripts ont été conservés).
