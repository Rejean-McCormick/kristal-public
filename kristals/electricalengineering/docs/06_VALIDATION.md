# Validation — Kristal-ElectricalEngineering

Exécuter :

```sh
python tools/kristal.py check .
python tools/build-with-materializations.py
python tools/build-with-materializations.py --verify-only
```

Ces tests contrôlent : format authoring 3.2.2, build v9, original Logical Commitment, original State Commitment, digest/size du blob v6, correspondance source/manifest et reconstruction exacte du payload à partir de la projection v6.

Golden Logical Commitment : `sha256:1637a2b8a3d258f9dc2bf7878c5915e59dd437288e41c21288148ee7bb23eccf`.

Golden State Commitment : `sha256:ba2ca177fa9738f7634eda20f1ba346d9cd1621c9e67908da60588763c3686bb`.

Ces contrôles structurels et physiques n'attestent pas de la vérité externe des assertions ; les tests métiers historiques demeurent indépendants.
