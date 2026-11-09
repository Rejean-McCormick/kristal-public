# Validation et reproduction

```bash
python tools/build_verified_v9.py
```

Cette commande exécute `check`, `build-v9` puis vérifie/retient le manifeste v9 historique.

**Logical Artifact Commitment immuable :** `sha256:44b853db43aa36038d65662d0233360463ee4833407145c20af6bf0abe434b33`

**State Commitment immuable :** `sha256:df7294a165392d3496c1a9aad2a97df768ecb44974d2c26c0050351f0a6ee2c8`

**Profil de matérialisation retenu :** `kristal.materialization/kristal-state-v6/1` ; 1 segment(s).

Pour reconstruire, vérifier à chaque build que les deux engagements sont identiques aux golden digests. Ne pas déclarer de nouvelle qualification full publisher sans tests de publication. Ne pas considérer la vérification SHA des blobs comme une preuve sémantique indépendante.
