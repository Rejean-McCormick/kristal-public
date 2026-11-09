# Validation et reproduction

```bash
python tools/build_verified_v9.py
```

Cette commande exécute `check`, `build-v9` puis vérifie/retient le manifeste v9 historique.

**Logical Artifact Commitment immuable :** `sha256:2526cda3ac5aca0d04c91ff3da5d5750a4134020bea0007e5e434d452fe9be4c`

**State Commitment immuable :** `sha256:600fdb78e64094f610b57faadbb1dec28706562d70a4b839f57af9d99c097ae9`

**Profil de matérialisation retenu :** `kristal.materialization/kristal-state-v6/1` ; 1 segment(s).

Pour reconstruire, vérifier à chaque build que les deux engagements sont identiques aux golden digests. Ne pas déclarer de nouvelle qualification full publisher sans tests de publication. Ne pas considérer la vérification SHA des blobs comme une preuve sémantique indépendante.
