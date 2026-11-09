# Validation — Kristal-Evolution

Exécuter :

```sh
python tools/kristal.py check .
python tools/build-with-materializations.py
python tools/build-with-materializations.py --verify-only
```

Ces tests contrôlent : format authoring 3.2.2, build v9, original Logical Commitment, original State Commitment, digest/size du blob v6, correspondance source/manifest et reconstruction exacte du payload à partir de la projection v6.

Golden Logical Commitment : `sha256:fbe9e733cdc1267f82dcb0e8ccd19ac7a0c0066be8d8fd30acac31e2a33d18c9`.

Golden State Commitment : `sha256:18fb7ec7f383198a0c42378f62201e5e0463ac9d69a15e61e2302f070eeca48f`.

Ces contrôles structurels et physiques n'attestent pas de la vérité externe des assertions ; les tests métiers historiques demeurent indépendants.
