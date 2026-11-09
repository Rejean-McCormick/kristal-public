# Validation — Kristal-NaturalHazards

## Checks techniques exécutés

- `python tools/kristal.py check .`
- `python tools/kristal.py build-v9 .`
- vérification des blobs des deux manifests historiques ; comparaison des digests recomputés.

## Golden Commitments

- Logical Artifact : `sha256:699299c299f7d820501ecc6c132ffefe81fa80cfb3b89b4747818e54cf2c971a`
- State Snapshot : `sha256:087cde277bcb6868e864c5f53cbe7108fd17046f56c4ef3491bc3c2776000d86`

Les deux engagements doivent rester identiques à ceux du paquet d'origine. Si une modification de `canon/` change ces digests, c'est une nouvelle version logique, pas une simple optimisation de stockage.

## Limite

La conformité structurelle au kit n'est ni la validation de la qualité scientifique du corpus ni un contrôle par les validateurs métier historiques (ces scripts ont été conservés).
