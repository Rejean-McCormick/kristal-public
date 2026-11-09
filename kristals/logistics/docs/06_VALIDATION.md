# Validation — Kristal-Logistics

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/register_legacy_materialization.py
```

**State Commitment attendu :** `sha256:9807bbe4c0afdc5c4d986897a1cadf077e16641a90a9f79316da049e2e089237`

**Logical Commitment attendu :** `sha256:fa58abcba64d359003dd7ce928a3d5622244aeb9b6b37de81ab4d3ef6b1b9b60`

Le validateur métier éventuellement présent sous `knowledge-base/tools/validate.py` vérifie d'autres invariants et doit être exécuté indépendamment du simple check structurel. Ne pas déduire de la validation v9 une vérité scientifique, juridique ou médicale.
