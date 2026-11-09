# Validation — Kristal-MechanicalEngineering

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/register_legacy_materialization.py
```

**State Commitment attendu :** `sha256:cf0959ebd2173a8f1dbd949420fec251c245675457aab35a803407577da3c3d0`

**Logical Commitment attendu :** `sha256:a5a7481dac8c29013e4c92de10f14b2330bc7e1f282d320770c538870159dea2`

Le validateur métier éventuellement présent sous `knowledge-base/tools/validate.py` vérifie d'autres invariants et doit être exécuté indépendamment du simple check structurel. Ne pas déduire de la validation v9 une vérité scientifique, juridique ou médicale.
