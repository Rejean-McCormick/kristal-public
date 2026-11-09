# Validation

Contrôles automatisés de cette migration :

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/verify_existing_materializations.py .
```

Golden logical commitment : `sha256:ab4fe707870ada575ec1fbdfa689f92725ecbf0c8ce50b7785340c73cc64d925`

Golden state commitment : `sha256:135acf22dfa600f1faa47b9b6de871539f615722310bf2f5db5cdb6ad62a3b8d`

Le rapport du kit ne certifie pas la vérité scientifique des assertions; les validators métier précédents et les rapports de qualification historiques restent des preuves indépendantes. Le champ `declared_lossless` des manifests historiques n'est pas une preuve de décompression ou de reconstruction exécutée par le kit 3.2.2.
