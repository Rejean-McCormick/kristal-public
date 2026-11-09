# Validation — Kristal-Climate

## Checks techniques exécutés

- `python tools/kristal.py check .`
- `python tools/kristal.py build-v9 .`
- vérification du blob du manifest historique ; comparaison des digests recomputés.

## Golden Commitments

- Logical Artifact : `sha256:01455cd05d5c562f107a16fead9076808e9058e624c7c80f5cd317b4334670c3`
- State Snapshot : `sha256:d9687696176c96578f9fd57ce474671ffb1eeb04372d1645aeb7ad7bf41b0842`

Les deux engagements doivent rester identiques à ceux du paquet d'origine. Si une modification de `canon/` change ces digests, c'est une nouvelle version logique, pas une simple optimisation de stockage.

## Limite

La conformité structurelle au kit n'est ni la validation de la qualité scientifique du corpus ni un contrôle par les validateurs métier historiques (ces scripts ont été conservés).
