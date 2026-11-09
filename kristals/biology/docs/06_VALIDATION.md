# Validation — Kristal-Biology

## Checks techniques exécutés

- `python tools/kristal.py check .`
- `python tools/kristal.py build-v9 .`
- vérification du blob du manifest historique ; comparaison des digests recomputés.

## Golden Commitments

- Logical Artifact : `sha256:856062596bbbcff48e3d2d11d5e38d6ec338b14c9fbd0745c0b536eddf5615aa`
- State Snapshot : `sha256:03fbb4a6a29ee3f842974cb59b27deb68f106a6f6f566c3c93f44338c71872a5`

Les deux engagements doivent rester identiques à ceux du paquet d'origine. Si une modification de `canon/` change ces digests, c'est une nouvelle version logique, pas une simple optimisation de stockage.

## Limite

La conformité structurelle au kit n'est ni la validation de la qualité scientifique du corpus ni un contrôle par les validateurs métier historiques (ces scripts ont été conservés).
