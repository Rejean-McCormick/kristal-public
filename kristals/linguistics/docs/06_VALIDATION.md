# Validation — Kristal-Linguistics

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/register_legacy_materialization.py
```

**State Commitment attendu :** `sha256:97209736a40d7c2a6d7d7c6a4c5ed517c0496540e12b59fc03c3910639acad98`

**Logical Commitment attendu :** `sha256:d12d763a681e3303b102738ef77c2542999f30613be95f79d0b09b771e3e1a3d`

Le validateur métier éventuellement présent sous `knowledge-base/tools/validate.py` vérifie d'autres invariants et doit être exécuté indépendamment du simple check structurel. Ne pas déduire de la validation v9 une vérité scientifique, juridique ou médicale.
