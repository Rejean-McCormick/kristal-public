# Validation — Kristal-Nutrition

## Checks techniques exécutés

- `python tools/kristal.py check .`
- `python tools/kristal.py build-v9 .`
- vérification des blobs des deux manifests historiques ; comparaison des digests recomputés.

## Golden Commitments

- Logical Artifact : `sha256:895dee9f7a1c370f928246f12ed27bba74733fba53c7b0071c0246000950dab9`
- State Snapshot : `sha256:17c0bfa713edd10b2eaabe6a63a389dec9c6226c9a55df1c7154d7d63c30902a`

Les deux engagements doivent rester identiques à ceux du paquet d'origine. Si une modification de `canon/` change ces digests, c'est une nouvelle version logique, pas une simple optimisation de stockage.

## Limite

La conformité structurelle au kit n'est ni la validation de la qualité scientifique du corpus ni un contrôle par les validateurs métier historiques (ces scripts ont été conservés).
