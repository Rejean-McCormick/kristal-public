# Validation et reproduction

```bash
python tools/build_verified_v9.py
```

Cette commande exécute `check`, `build-v9` puis vérifie/retient le manifeste v9 historique.

**Logical Artifact Commitment immuable :** `sha256:a86abf8d2847f9b0563609bc99b9d09c6850843a8907cabdfcb94e23c3302910`

**State Commitment immuable :** `sha256:31e7ed7434833bbd4a15aeb6371dd4571b822f5f607dae6c468733de92ac4d8b`

**Profil de matérialisation retenu :** `kristal.materialization/kristal-state-v6/1` ; 1 segment(s).

Pour reconstruire, vérifier à chaque build que les deux engagements sont identiques aux golden digests. Ne pas déclarer de nouvelle qualification full publisher sans tests de publication. Ne pas considérer la vérification SHA des blobs comme une preuve sémantique indépendante.
