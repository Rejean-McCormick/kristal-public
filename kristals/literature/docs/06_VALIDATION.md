# Validation — Kristal-Literature

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/register_legacy_materialization.py
```

**State Commitment attendu :** `sha256:0d091c687a8e6ba8089969ed5e4f54fbf7a8e63a3cd20dea14adb679b2df6f64`

**Logical Commitment attendu :** `sha256:abac8acfce10eb331f02d070fe42e76daa23ffbb4549dd17414f41dac6113a5c`

Le validateur métier éventuellement présent sous `knowledge-base/tools/validate.py` vérifie d'autres invariants et doit être exécuté indépendamment du simple check structurel. Ne pas déduire de la validation v9 une vérité scientifique, juridique ou médicale.
