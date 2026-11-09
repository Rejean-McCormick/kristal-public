# Validation — Kristal-Music

## Checks techniques exécutés

- `python tools/kristal.py check .`
- `python tools/kristal.py build-v9 .`
- vérification des blobs des deux manifests historiques ; comparaison des digests recomputés.

## Golden Commitments

- Logical Artifact : `sha256:929ae7595b75c0fe8f9fbc0c35e857e9a5a46d5773f1ec3a19e625777b42d4ac`
- State Snapshot : `sha256:7f672714a71916d15be92d5dcd00d3206c6448c0b4666848c4e37545d39dfc63`

Les deux engagements doivent rester identiques à ceux du paquet d'origine. Si une modification de `canon/` change ces digests, c'est une nouvelle version logique, pas une simple optimisation de stockage.

## Limite

La conformité structurelle au kit n'est ni la validation de la qualité scientifique du corpus ni un contrôle par les validateurs métier historiques (ces scripts ont été conservés).
