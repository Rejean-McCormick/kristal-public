# Validation — Kristal-Electronics

Exécuter :

```sh
python tools/kristal.py check .
python tools/build-with-materializations.py
python tools/build-with-materializations.py --verify-only
```

Ces tests contrôlent : format authoring 3.2.2, build v9, original Logical Commitment, original State Commitment, digest/size du blob v6, correspondance source/manifest et reconstruction exacte du payload à partir de la projection v6.

Golden Logical Commitment : `sha256:3c9782a40f55c151925a22d84d31b9fe22af461f2febac4ef7c72d73824c697e`.

Golden State Commitment : `sha256:a27f48934b79771b6f5dbd9a6c383b39e9587bb6b3f787bc5973660f11f4e059`.

Ces contrôles structurels et physiques n'attestent pas de la vérité externe des assertions ; les tests métiers historiques demeurent indépendants.
