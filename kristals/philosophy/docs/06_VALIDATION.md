# Validation et reproduction

```bash
python tools/build_verified_v9.py
```

Cette commande exécute `check`, `build-v9` puis vérifie/retient le manifeste v9 historique.

**Logical Artifact Commitment immuable :** `sha256:2fb055999fa4828ebbe3223999a37f4c72aa37b6b6a72a3e19afb964d5d3a3c3`

**State Commitment immuable :** `sha256:ad85891fa46b7492f2e037963ec53c81f607e6cf4d5fe72441eb349bb6910111`

**Profil de matérialisation retenu :** `kristal.materialization/kristal-state-v6/1` ; 1 segment(s).

Pour reconstruire, vérifier à chaque build que les deux engagements sont identiques aux golden digests. Ne pas déclarer de nouvelle qualification full publisher sans tests de publication. Ne pas considérer la vérification SHA des blobs comme une preuve sémantique indépendante.
