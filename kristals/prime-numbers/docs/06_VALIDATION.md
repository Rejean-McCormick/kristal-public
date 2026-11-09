# Validation et reproduction

```bash
python tools/build_verified_v9.py
```

Cette commande exécute `check`, `build-v9` puis vérifie/retient le manifeste v9 historique.

**Logical Artifact Commitment immuable :** `sha256:dca6378056ac44faf4fd91b4bab1addf687e4e87491504f0657237c0d23c1a82`

**State Commitment immuable :** `sha256:ec0c647012acf3906009f33ce5d4cf86fc6bc2848be1b7d36d87aa511a688c91`

**Profil de matérialisation retenu :** `prime-numbers.materialization/kristall-v7-json-bundle/1` ; 12 segment(s).

Pour reconstruire, vérifier à chaque build que les deux engagements sont identiques aux golden digests. Ne pas déclarer de nouvelle qualification full publisher sans tests de publication. Ne pas considérer la vérification SHA des blobs comme une preuve sémantique indépendante.
