# Validation — Kristal-Logic

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/register_legacy_materialization.py
```

**State Commitment attendu :** `sha256:42f614e25d5d2f6ba82bf4b16c59e2423da55eed012861cdc7c1bf7a2d2cc996`

**Logical Commitment attendu :** `sha256:3a529cfa53da08d6ec933fc1cee96a790517201eac285a7282d74b8dd1e619bd`

Le validateur métier éventuellement présent sous `knowledge-base/tools/validate.py` vérifie d'autres invariants et doit être exécuté indépendamment du simple check structurel. Ne pas déduire de la validation v9 une vérité scientifique, juridique ou médicale.
