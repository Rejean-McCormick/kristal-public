# Validation

Contrôles automatisés de cette migration :

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/verify_existing_materializations.py .
```

Golden logical commitment : `sha256:66dba9e991c40e51d496419704460cd8f429bcaf4d8b3884a92f2116a1dc1362`

Golden state commitment : `sha256:7da8f26afa158ed22cc3f0c13b1c6bd55fb4c38e30bc98d09fab947ee4ab6ba3`

Le rapport du kit ne certifie pas la vérité scientifique des assertions; les validators métier précédents et les rapports de qualification historiques restent des preuves indépendantes. Le champ `declared_lossless` des manifests historiques n'est pas une preuve de décompression ou de reconstruction exécutée par le kit 3.2.2.
