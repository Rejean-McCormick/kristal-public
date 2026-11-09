# Validation — Kristal-EngineeringConstraints

Exécuter :

```sh
python tools/kristal.py check .
python tools/build-with-materializations.py
python tools/build-with-materializations.py --verify-only
```

Ces tests contrôlent : format authoring 3.2.2, build v9, original Logical Commitment, original State Commitment, digest/size du blob v6, correspondance source/manifest et reconstruction exacte du payload à partir de la projection v6.

Golden Logical Commitment : `sha256:a15a0db16777cbb02daa88ffe885d922c81a6a3fb3227c8dcf0f3d366d286e20`.

Golden State Commitment : `sha256:b41eb1c05e14b0007c42d98e224d37a514c1ecf64edf7584597e2e324f6a2d68`.

Ces contrôles structurels et physiques n'attestent pas de la vérité externe des assertions ; les tests métiers historiques demeurent indépendants.
