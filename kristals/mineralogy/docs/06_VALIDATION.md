# Validation — Kristal-Mineralogy

## Checks techniques exécutés

- `python tools/kristal.py check .`
- `python tools/kristal.py build-v9 .`
- vérification des blobs des deux manifests historiques ; comparaison des digests recomputés.

## Golden Commitments

- Logical Artifact : `sha256:03a65382e20c60add87c87ecb5bcfcf0884a8edcd8e68432d5b97ebb429f71ef`
- State Snapshot : `sha256:8bd65fa600e8b272a22ea20189f99ac560c9193619b2f1c5ad2895ad26b6246b`

Les deux engagements doivent rester identiques à ceux du paquet d'origine. Si une modification de `canon/` change ces digests, c'est une nouvelle version logique, pas une simple optimisation de stockage.

## Limite

La conformité structurelle au kit n'est ni la validation de la qualité scientifique du corpus ni un contrôle par les validateurs métier historiques (ces scripts ont été conservés).
