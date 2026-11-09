# Validation — Kristal-Ethics

Exécuter :

```sh
python tools/kristal.py check .
python tools/build-with-materializations.py
python tools/build-with-materializations.py --verify-only
```

Ces tests contrôlent : format authoring 3.2.2, build v9, original Logical Commitment, original State Commitment, digest/size du blob v6, correspondance source/manifest et reconstruction exacte du payload à partir de la projection v6.

Golden Logical Commitment : `sha256:1d927fbbbb988904dd8912eec243acbab52c47cb20e962fe4cdc76e837388f39`.

Golden State Commitment : `sha256:f6b76f1f18ff3d2220186fa4f869120b8aead562378c88f8226532adee166701`.

Ces contrôles structurels et physiques n'attestent pas de la vérité externe des assertions ; les tests métiers historiques demeurent indépendants.
