# Validation

Contrôles automatisés de cette migration :

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/verify_existing_materializations.py .
```

Golden logical commitment : `sha256:c5805bcf289232108defb6f9f0aa9c1b6fb25e5813b7b47a1683454dc8d67604`

Golden state commitment : `sha256:c75091e8470883c1f3fc35253e1224096caf97f439eb3fa32aaf69ea1d80d9b7`

Le rapport du kit ne certifie pas la vérité scientifique des assertions; les validators métier précédents et les rapports de qualification historiques restent des preuves indépendantes. Le champ `declared_lossless` des manifests historiques n'est pas une preuve de décompression ou de reconstruction exécutée par le kit 3.2.2.
