# Validation — Kristal-Media

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/register_legacy_materialization.py
```

**State Commitment attendu :** `sha256:16f1f50ac6a2a57e2a6a8130a0e5b9503a28d9bf52b78f6058c095876d21e56d`

**Logical Commitment attendu :** `sha256:411fab276ae7a476c27ed7788a69eee17a0a5bf8dc131c132e219a51338d15a2`

Le validateur métier éventuellement présent sous `knowledge-base/tools/validate.py` vérifie d'autres invariants et doit être exécuté indépendamment du simple check structurel. Ne pas déduire de la validation v9 une vérité scientifique, juridique ou médicale.
