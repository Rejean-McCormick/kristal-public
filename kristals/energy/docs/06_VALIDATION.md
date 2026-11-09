# Validation — Kristal-Energy

Exécuter :

```sh
python tools/kristal.py check .
python tools/build-with-materializations.py
python tools/build-with-materializations.py --verify-only
```

Ces tests contrôlent : format authoring 3.2.2, build v9, original Logical Commitment, original State Commitment, digest/size du blob v6, correspondance source/manifest et reconstruction exacte du payload à partir de la projection v6.

Golden Logical Commitment : `sha256:c33a343422d6af1ffc3693f7b54818ac1d455829374124880b8a0aecd1030961`.

Golden State Commitment : `sha256:48adc6a63f75df4dc315152c08c043f8a3a6353f0aacf64601e09821f7785ba8`.

Ces contrôles structurels et physiques n'attestent pas de la vérité externe des assertions ; les tests métiers historiques demeurent indépendants.
