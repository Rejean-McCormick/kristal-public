# Validation — Kristal-Mythology

## Checks techniques exécutés

- `python tools/kristal.py check .`
- `python tools/kristal.py build-v9 .`
- vérification des blobs des deux manifests historiques ; comparaison des digests recomputés.

## Golden Commitments

- Logical Artifact : `sha256:c4d5103ac495cb420c14c254c61a764de6d8f7b079266e3db05fb899ac126c64`
- State Snapshot : `sha256:2e4f064f98758c38ecfde5e17a02554bf9ac590018f809e61d5cc59809d51aae`

Les deux engagements doivent rester identiques à ceux du paquet d'origine. Si une modification de `canon/` change ces digests, c'est une nouvelle version logique, pas une simple optimisation de stockage.

## Limite

La conformité structurelle au kit n'est ni la validation de la qualité scientifique du corpus ni un contrôle par les validateurs métier historiques (ces scripts ont été conservés).
