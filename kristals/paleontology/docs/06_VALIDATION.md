# Validation et reproduction

```bash
python tools/build_verified_v9.py
```

Cette commande exécute `check`, `build-v9` puis vérifie/retient le manifeste v9 historique.

**Logical Artifact Commitment immuable :** `sha256:356f98bff62f3bc5f4c4255acb6965f275c968f1be6427bbf81361c8e31b27fa`

**State Commitment immuable :** `sha256:6871a42c8db0e88d3fd60491f33b6d764e0195b3cde5fd688e1c8facee74f18a`

**Profil de matérialisation retenu :** `kristal.materialization/kristal-state-v6/1` ; 1 segment(s).

Pour reconstruire, vérifier à chaque build que les deux engagements sont identiques aux golden digests. Ne pas déclarer de nouvelle qualification full publisher sans tests de publication. Ne pas considérer la vérification SHA des blobs comme une preuve sémantique indépendante.
