# Validation — Kristal-Medicine

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/register_legacy_materialization.py
```

**State Commitment attendu :** `sha256:2d442d8c6e34d0fb69214d73741e4fb13935b105083c24c8cfad8fb51ce63bb5`

**Logical Commitment attendu :** `sha256:7335494b06a5862c777d3b9a08b62cde0c816c1217af43d42390b5ed002788c6`

Le validateur métier éventuellement présent sous `knowledge-base/tools/validate.py` vérifie d'autres invariants et doit être exécuté indépendamment du simple check structurel. Ne pas déduire de la validation v9 une vérité scientifique, juridique ou médicale.
