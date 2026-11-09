# Validation — Kristal-Catho

## Checks techniques exécutés

- `python tools/kristal.py check .`
- `python tools/kristal.py build-v9 .`
- vérification du blob du manifest historique ; comparaison des digests recomputés.

## Golden Commitments

- Logical Artifact : `sha256:a08ca450ed75f8e13a1c2d8902949ab752a31886ccb3b3284fb5cbab910d279f`
- State Snapshot : `sha256:f65f61362b80ffbc5494559a48a33840a850d019c65e623b239861f21b73e4f5`

Les deux engagements doivent rester identiques à ceux du paquet d'origine. Si une modification de `canon/` change ces digests, c'est une nouvelle version logique, pas une simple optimisation de stockage.

## Limite

La conformité structurelle au kit n'est ni la validation de la qualité scientifique du corpus ni un contrôle par les validateurs métier historiques (ces scripts ont été conservés).



## Extension 2026-10-13 — contrôle additionnel

`python knowledge-base/tools/validate_people.py` contrôle la cardinalité de la liste vaticane (267 entrées / 265 personnes en raison de Benoît IX), les 38 docteurs, la résolution des sources et l'intégrité des catégories et numéros.

Exécuter ensuite `python tools/kristal.py check .`, `python tools/kristal.py build-v9 .` et, si la couche IA est construite, `python tools/kristal.py check-ai .`. Ces contrôles techniques ne confèrent aucune autorité ecclésiale au dépôt.
