# Validation

Contrôles automatisés de cette migration :

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/verify_existing_materializations.py .
```

Golden logical commitment : `sha256:10caa2abb9503ce5d47b30ed2022a5dea280642d092e93b5bc1d52d3786f05d9`

Golden state commitment : `sha256:89dca6fbac6c23f463d65d97b8d190d4d6703ec73972ec611d06a3eee9eb546e`

Le rapport du kit ne certifie pas la vérité scientifique des assertions; les validators métier précédents et les rapports de qualification historiques restent des preuves indépendantes. Le champ `declared_lossless` des manifests historiques n'est pas une preuve de décompression ou de reconstruction exécutée par le kit 3.2.2.
