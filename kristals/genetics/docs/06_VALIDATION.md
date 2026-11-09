# Validation

Contrôles automatisés de cette migration :

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/verify_existing_materializations.py .
```

Golden logical commitment : `sha256:c116269ca3c320d52354250e16933c824066b991e9c245bf3aec46918749a672`

Golden state commitment : `sha256:b2209e90f1e85d1dd809e8c93b6e7f1ebcb328f11d583dd5db7854db3e693e09`

Le rapport du kit ne certifie pas la vérité scientifique des assertions; les validators métier précédents et les rapports de qualification historiques restent des preuves indépendantes. Le champ `declared_lossless` des manifests historiques n'est pas une preuve de décompression ou de reconstruction exécutée par le kit 3.2.2.
