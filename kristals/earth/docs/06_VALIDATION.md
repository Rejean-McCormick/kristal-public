# Validation — Kristal-Earth

## Commandes

```shell
python tools/kristal.py check .
python tools/kristal.py build-v9 .
```

## Golden commitments

Logical Artifact : `sha256:30a5e8367084a74eba695862edc7af75fb199c78c671c1339eb5d6fa4358820a`

State v9 : `sha256:447ec078994fc446a3f1ad5fb918ba9d7762e549fe98c3812e060f1d6727e5f1`

La validation conserve aussi le manifest de matérialisation historique et vérifie octets, taille et SHA-256 des blobs sous `knowledge-base/corpus/`.

**Limite :** cette validation ne remplace pas les tests de vérité du domaine, ni la qualification externe, ni la publication.
