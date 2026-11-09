# Validation — Kristal-Manufacturing

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/register_legacy_materialization.py
```

**State Commitment attendu :** `sha256:ab83dfd868d40f90d057cacf5b1955dcee90a11a915a867525eb53cbeada269f`

**Logical Commitment attendu :** `sha256:9736e272363ea19412a592436dfa09106620aa43ed7c2f66f56f9135325513fc`

Le validateur métier éventuellement présent sous `knowledge-base/tools/validate.py` vérifie d'autres invariants et doit être exécuté indépendamment du simple check structurel. Ne pas déduire de la validation v9 une vérité scientifique, juridique ou médicale.
