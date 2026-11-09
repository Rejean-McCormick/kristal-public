# Validation — Kristal-Education

Exécuter :

```sh
python tools/kristal.py check .
python tools/build-with-materializations.py
python tools/build-with-materializations.py --verify-only
```

Ces tests contrôlent : format authoring 3.2.2, build v9, original Logical Commitment, original State Commitment, digest/size du blob v6, correspondance source/manifest et reconstruction exacte du payload à partir de la projection v6.

Golden Logical Commitment : `sha256:d3a43d552efc9c2d4f810521e1ab95b6dbe0d71f25edcca3c04ff769c631111a`.

Golden State Commitment : `sha256:5fcde752fe96e4564e2ac316bd02a1655e5e87ce12f51a15d0c1cb355bbea3f3`.

Ces contrôles structurels et physiques n'attestent pas de la vérité externe des assertions ; les tests métiers historiques demeurent indépendants.
