# Validation

Contrôles automatisés de cette migration :

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/verify_existing_materializations.py .
```

Golden logical commitment : `sha256:3208e10d634125338ad7d2d9c4ad30bf2f5430da9ee406a94b042ee5bc9aa9f4`

Golden state commitment : `sha256:5c48d1c99a43a648c0361c9f6828877b5280653af91d764cec523d998ad745d5`

Le rapport du kit ne certifie pas la vérité scientifique des assertions; les validators métier précédents et les rapports de qualification historiques restent des preuves indépendantes. Le champ `declared_lossless` des manifests historiques n'est pas une preuve de décompression ou de reconstruction exécutée par le kit 3.2.2.
