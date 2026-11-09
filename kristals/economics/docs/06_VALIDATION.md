# Validation — Kristal-Economics

Exécuter :

```sh
python tools/kristal.py check .
python tools/build-with-materializations.py
python tools/build-with-materializations.py --verify-only
```

Ces tests contrôlent : format authoring 3.2.2, build v9, original Logical Commitment, original State Commitment, digest/size du blob v6, correspondance source/manifest et reconstruction exacte du payload à partir de la projection v6.

Golden Logical Commitment : `sha256:ca651851f7f599429e08c226ee7ad1bb9da7e0edbee6df86560279ea4ff056ac`.

Golden State Commitment : `sha256:4617e0a585472ff81895e2385e905071a26db94d3b1a854d6305c455da578091`.

Ces contrôles structurels et physiques n'attestent pas de la vérité externe des assertions ; les tests métiers historiques demeurent indépendants.
