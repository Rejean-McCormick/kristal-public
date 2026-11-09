# Validation — Kristal-Disasters

## Commandes

```shell
python tools/kristal.py check .
python tools/kristal.py build-v9 .
```

## Golden commitments

Logical Artifact : `sha256:fd6935f1b061b49e68714e65c9453c6f7556acf89ad2e120c85deb816563985e`

State v9 : `sha256:7c1509e20058b35b6d59def5419ea5eda3b028b4b5d219e5f266abae7a300182`

La validation conserve aussi le manifest de matérialisation historique et vérifie octets, taille et SHA-256 des blobs sous `knowledge-base/corpus/`.

**Limite :** cette validation ne remplace pas les tests de vérité du domaine, ni la qualification externe, ni la publication.
