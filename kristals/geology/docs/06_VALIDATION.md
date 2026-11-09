# Validation

Contrôles automatisés de cette migration :

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/verify_existing_materializations.py .
```

Golden logical commitment : `sha256:b298c9c0f2fed7c16d7ca075d6ffc76a233fb072af2b4a7fbd4db163a8c9c23f`

Golden state commitment : `sha256:c3e33f539b6d8d0eb1f35ae2312f2ae14873159f030d3e712bc047cc1301643e`

Le rapport du kit ne certifie pas la vérité scientifique des assertions; les validators métier précédents et les rapports de qualification historiques restent des preuves indépendantes. Le champ `declared_lossless` des manifests historiques n'est pas une preuve de décompression ou de reconstruction exécutée par le kit 3.2.2.
