# Validation

Contrôles automatisés de cette migration :

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/verify_existing_materializations.py .
```

Golden logical commitment : `sha256:43320d2ff82c28ffd5cad99ccf9d182c52a049c535a7250c307ddbe4c29479d2`

Golden state commitment : `sha256:a21cf13ca028404caa603f832c6bc6b057d994b0872504f047881304b6c86360`

Le rapport du kit ne certifie pas la vérité scientifique des assertions; les validators métier précédents et les rapports de qualification historiques restent des preuves indépendantes. Le champ `declared_lossless` des manifests historiques n'est pas une preuve de décompression ou de reconstruction exécutée par le kit 3.2.2.
