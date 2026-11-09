# Validation

La conformité de ce workspace doit être évaluée à plusieurs niveaux.

## Domaine

Depuis `knowledge-base/` :

```bash
python tools/validate.py
python -m unittest discover -s tests -v
```

Le validateur métier couvre notamment le schéma v6, la résolution des sources, le ledger mécanique, l'unicité des IDs et les manifestes. Ces contrôles ne certifient pas la vérité des interprétations ontologiques.

## Local Kristal 3.2.2

```bash
python <authoring-kit>/tools/kristal.py check .
python <authoring-kit>/tools/kristal.py build-v9 .
```

La normalisation impose en plus deux invariants :

1. les fichiers préexistants du snapshot doivent rester inchangés octet pour octet ;
2. le `build/v9/state-snapshot.json` doit retrouver le même State Logical Commitment que `.kristal/v9/state-snapshot.json`.

Ces validations sont structurelles et de cohérence ; elles ne remplacent pas une qualification indépendante du contenu scientifique/philosophique.
