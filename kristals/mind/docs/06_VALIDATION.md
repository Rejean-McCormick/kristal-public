# Validation — Kristal-Mind

## Checks techniques exécutés

- `python tools/kristal.py check .`
- `python tools/kristal.py build-v9 .`
- vérification des blobs des deux manifests historiques ; comparaison des digests recomputés.

## Golden Commitments

- Logical Artifact : `sha256:f56c8988329eff5190dd0ac01c50c3c229825877febd675627a819d2e6be8d96`
- State Snapshot : `sha256:129263889ac0fb66334cb45240e30fc07f0905bd70ff3994638b2741a63a8b2a`

Les deux engagements doivent rester identiques à ceux du paquet d'origine. Si une modification de `canon/` change ces digests, c'est une nouvelle version logique, pas une simple optimisation de stockage.

## Limite

La conformité structurelle au kit n'est ni la validation de la qualité scientifique du corpus ni un contrôle par les validateurs métier historiques (ces scripts ont été conservés).
