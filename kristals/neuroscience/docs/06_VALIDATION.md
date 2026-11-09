# Validation — Kristal-Neuroscience

## Checks techniques exécutés

- `python tools/kristal.py check .`
- `python tools/kristal.py build-v9 .`
- vérification des blobs des deux manifests historiques ; comparaison des digests recomputés.

## Golden Commitments

- Logical Artifact : `sha256:8d62f538149a75b73b41ba509625b80069b63d0d599c31c613099f5e1cb4434f`
- State Snapshot : `sha256:9e8f98b13e7056936825d84163fd08cbd433a89b9f8f3dfbbdb36ebe47c646c7`

Les deux engagements doivent rester identiques à ceux du paquet d'origine. Si une modification de `canon/` change ces digests, c'est une nouvelle version logique, pas une simple optimisation de stockage.

## Limite

La conformité structurelle au kit n'est ni la validation de la qualité scientifique du corpus ni un contrôle par les validateurs métier historiques (ces scripts ont été conservés).
