# Validation — Kristal-Ocean

## Checks techniques exécutés

- `python tools/kristal.py check .`
- `python tools/kristal.py build-v9 .`
- vérification des blobs des deux manifests historiques ; comparaison des digests recomputés.

## Golden Commitments

- Logical Artifact : `sha256:37047f7bffc021ec765e472c77b2c003317de719f5b005108d5db30710e19810`
- State Snapshot : `sha256:0295970e7464bfc348117b5b6620e7bac14daf591f8e1f1164d8e1aadc8b6cf4`

Les deux engagements doivent rester identiques à ceux du paquet d'origine. Si une modification de `canon/` change ces digests, c'est une nouvelle version logique, pas une simple optimisation de stockage.

## Limite

La conformité structurelle au kit n'est ni la validation de la qualité scientifique du corpus ni un contrôle par les validateurs métier historiques (ces scripts ont été conservés).
