# Validation — Kristal-Demography

## Commandes

```shell
python tools/kristal.py check .
python tools/kristal.py build-v9 .
```

## Golden commitments

Logical Artifact : `sha256:616614071991211a55ec681af9036a3970b023b108cba1f8c1189e52c92cd986`

State v9 : `sha256:010462c4543df240b987d1f05ba11046c04628f519a186f6eedf8225c702ffc1`

La validation conserve aussi le manifest de matérialisation historique et vérifie octets, taille et SHA-256 des blobs sous `knowledge-base/corpus/`.

**Limite :** cette validation ne remplace pas les tests de vérité du domaine, ni la qualification externe, ni la publication.
