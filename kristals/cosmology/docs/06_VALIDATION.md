# Validation — Kristal-Cosmology

## Commandes

```shell
python tools/kristal.py check .
python tools/kristal.py build-v9 .
```

## Golden commitments

Logical Artifact : `sha256:65dd5fa88ccdaa2b14175ebf9ed308364e289e72c28eadefe37392fa6aca505c`

State v9 : `sha256:0cdcb703f5d0bda2ccdb9ab39ffd58bf7fd3824b4570071ae2d707d556621b44`

La validation conserve aussi le manifest de matérialisation historique et vérifie octets, taille et SHA-256 des blobs sous `knowledge-base/corpus/`.

**Limite :** cette validation ne remplace pas les tests de vérité du domaine, ni la qualification externe, ni la publication.
