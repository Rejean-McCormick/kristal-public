# Validation — Kristal-Maritime

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/register_legacy_materialization.py
```

**State Commitment attendu :** `sha256:07466f198752008f47110ccd1f6a4eedda072743972264265f041ecbd748b270`

**Logical Commitment attendu :** `sha256:345eebae81ee5dfcf3a2771f9e5d2d244933b4598d67634fed72953f66e76136`

Le validateur métier éventuellement présent sous `knowledge-base/tools/validate.py` vérifie d'autres invariants et doit être exécuté indépendamment du simple check structurel. Ne pas déduire de la validation v9 une vérité scientifique, juridique ou médicale.
