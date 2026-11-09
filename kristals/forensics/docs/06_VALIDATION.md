# Validation

Contrôles automatisés de cette migration :

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/verify_existing_materializations.py .
```

Golden logical commitment : `sha256:120b8b06602c3f76db903ee455d51fc8311b795c7b7a77f4220d2936d32e10a8`

Golden state commitment : `sha256:2d5d2d582e8b80fcb401058bd88652c708400c74b6c885b4544ac837810ea6da`

Le rapport du kit ne certifie pas la vérité scientifique des assertions; les validators métier précédents et les rapports de qualification historiques restent des preuves indépendantes. Le champ `declared_lossless` des manifests historiques n'est pas une preuve de décompression ou de reconstruction exécutée par le kit 3.2.2.
