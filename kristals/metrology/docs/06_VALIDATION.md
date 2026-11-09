# Validation — Kristal-Metrology

## Checks techniques exécutés

- `python tools/kristal.py check .`
- `python tools/kristal.py build-v9 .`
- vérification des blobs des deux manifests historiques ; comparaison des digests recomputés.

## Golden Commitments

- Logical Artifact : `sha256:cb57424e0a40b6a38c2eb63e6c3412e3512e7e9a46d2a48b68ef7dd4346f1d00`
- State Snapshot : `sha256:0b4ff16e80db2afd62877bcaaaec6a6ba5ba56b728a760589255844d269bcd46`

Les deux engagements doivent rester identiques à ceux du paquet d'origine. Si une modification de `canon/` change ces digests, c'est une nouvelle version logique, pas une simple optimisation de stockage.

## Limite

La conformité structurelle au kit n'est ni la validation de la qualité scientifique du corpus ni un contrôle par les validateurs métier historiques (ces scripts ont été conservés).
