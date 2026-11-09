# Validation — Kristal-Epistemology

Exécuter :

```sh
python tools/kristal.py check .
python tools/build-with-materializations.py
python tools/build-with-materializations.py --verify-only
```

Ces tests contrôlent : format authoring 3.2.2, build v9, original Logical Commitment, original State Commitment, digest/size du blob v6, correspondance source/manifest et reconstruction exacte du payload à partir de la projection v6.

Golden Logical Commitment : `sha256:96b7fd65e506a18eaa5aa37e013e50b5ed2ba6e954d919e0a4259d5674d44654`.

Golden State Commitment : `sha256:0862a292f1cbe928a6ae9e86f8579dfe3e886af2b7a6b09d959d7ada0565afd5`.

Ces contrôles structurels et physiques n'attestent pas de la vérité externe des assertions ; les tests métiers historiques demeurent indépendants.
