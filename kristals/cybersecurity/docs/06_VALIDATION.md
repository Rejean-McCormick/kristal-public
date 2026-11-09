# Validation — Kristal-Cybersecurity

## Commandes

```shell
python tools/kristal.py check .
python tools/kristal.py build-v9 .
```

## Golden commitments

Logical Artifact : `sha256:d688b56bbeaffe68c6b4e755fcf3d0c9b758f49d63c2df548bc97a1da9cc7e52`

State v9 : `sha256:ce349a4ad4d44b2f71f5d91294ae3f55e1a3a677941c3ec6cb57560a2e60292d`

La validation conserve aussi le manifest de matérialisation historique et vérifie octets, taille et SHA-256 des blobs sous `knowledge-base/corpus/`.

**Limite :** cette validation ne remplace pas les tests de vérité du domaine, ni la qualification externe, ni la publication.
