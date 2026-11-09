# Validation — Kristal-Ecology

Exécuter :

```sh
python tools/kristal.py check .
python tools/build-with-materializations.py
python tools/build-with-materializations.py --verify-only
```

Ces tests contrôlent : format authoring 3.2.2, build v9, original Logical Commitment, original State Commitment, digest/size du blob v6, correspondance source/manifest et reconstruction exacte du payload à partir de la projection v6.

Golden Logical Commitment : `sha256:bc4ec7bab591bede37737e51c0d76b540a520b75d675521c8a12d027224aa562`.

Golden State Commitment : `sha256:12094d7f1712a39a4d004989be90bddfe7c10851f67a369be4a7fb376544e594`.

Ces contrôles structurels et physiques n'attestent pas de la vérité externe des assertions ; les tests métiers historiques demeurent indépendants.
