# Validation — Kristal-Design

## Commandes

```shell
python tools/kristal.py check .
python tools/kristal.py build-v9 .
```

## Golden commitments

Logical Artifact : `sha256:e8f9110ce5d57820983ea0950cf1373cd90e3f6ffa6f26b6c82c1dc56f7c51ae`

State v9 : `sha256:45b1c8fa68e71451468b9bb2e30350d1570e0fcf81849f92a76218c6c3e5e8a2`

La validation conserve aussi le manifest de matérialisation historique et vérifie octets, taille et SHA-256 des blobs sous `knowledge-base/corpus/`.

**Limite :** cette validation ne remplace pas les tests de vérité du domaine, ni la qualification externe, ni la publication.
