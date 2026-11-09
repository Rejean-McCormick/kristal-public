# Validation et reproduction

```bash
python tools/build_verified_v9.py
```

Cette commande exécute `check`, `build-v9` puis vérifie/retient le manifeste v9 historique.

**Logical Artifact Commitment immuable :** `sha256:c811afc5845c6e4c8ba8243963f1eada576c21f95fdea3350d071b865fb43adc`

**State Commitment immuable :** `sha256:5318163afb08353c04e72112999d91e8b48d97e5f527235e932a603b85fd33c4`

**Profil de matérialisation retenu :** `recipes.materialization/domain-native-json-set/1` ; 17 segment(s).

Pour reconstruire, vérifier à chaque build que les deux engagements sont identiques aux golden digests. Ne pas déclarer de nouvelle qualification full publisher sans tests de publication. Ne pas considérer la vérification SHA des blobs comme une preuve sémantique indépendante.
