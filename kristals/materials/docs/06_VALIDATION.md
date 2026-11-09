# Validation — Kristal-Materials

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/register_legacy_materialization.py
```

**State Commitment attendu :** `sha256:731f64e995829bb680e62464fc584532f33080e7d2657370e4d668f2ff668c70`

**Logical Commitment attendu :** `sha256:9ccd9f97b177bdc65b273bbc6af03d1541549a5ce9eb2ca5661522a78157bb30`

Le validateur métier éventuellement présent sous `knowledge-base/tools/validate.py` vérifie d'autres invariants et doit être exécuté indépendamment du simple check structurel. Ne pas déduire de la validation v9 une vérité scientifique, juridique ou médicale.
