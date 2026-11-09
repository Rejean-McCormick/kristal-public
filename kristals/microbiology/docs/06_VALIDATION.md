# Validation — Kristal-Microbiology

## Checks techniques exécutés

- `python tools/kristal.py check .`
- `python tools/kristal.py build-v9 .`
- vérification des blobs des deux manifests historiques ; comparaison des digests recomputés.

## Golden Commitments

- Logical Artifact : `sha256:f20afb5def1469338979b4d645e8889f6e610c52e863a56468fcdf8d9daa4647`
- State Snapshot : `sha256:d909d47473a4873570ff9309670987f4ba888bff6d1f9eba317186517a31e236`

Les deux engagements doivent rester identiques à ceux du paquet d'origine. Si une modification de `canon/` change ces digests, c'est une nouvelle version logique, pas une simple optimisation de stockage.

## Limite

La conformité structurelle au kit n'est ni la validation de la qualité scientifique du corpus ni un contrôle par les validateurs métier historiques (ces scripts ont été conservés).
