# Validation

Contrôles automatisés de cette migration :

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/verify_existing_materializations.py .
```

Golden logical commitment : `sha256:df7409bd04f350d00eaa59624b860f44ec1b612bcc2831a8ae5048ce57110117`

Golden state commitment : `sha256:e5fbfb3b0d2ff5c27acfaaba9996831be66c8fbabe336625cfc1806105f2435d`

Le rapport du kit ne certifie pas la vérité scientifique des assertions; les validators métier précédents et les rapports de qualification historiques restent des preuves indépendantes. Le champ `declared_lossless` des manifests historiques n'est pas une preuve de décompression ou de reconstruction exécutée par le kit 3.2.2.
