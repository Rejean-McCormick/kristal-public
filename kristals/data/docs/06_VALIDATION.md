# Validation — Kristal-Data

## Commandes

```shell
python tools/kristal.py check .
python tools/kristal.py build-v9 .
```

## Golden commitments

Logical Artifact : `sha256:b1b9ec135aba541937d1f168b36a6f2034c9e98cf94ffdaeb45ac2a147477b72`

State v9 : `sha256:23d13957637969863189939ddfed65515da7587c890da028c1a74f8fb3836469`

La validation conserve aussi le manifest de matérialisation historique et vérifie octets, taille et SHA-256 des blobs sous `knowledge-base/corpus/`.

**Limite :** cette validation ne remplace pas les tests de vérité du domaine, ni la qualification externe, ni la publication.
