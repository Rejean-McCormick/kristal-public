# Validation — Kristal-Development

## Commandes

```shell
python tools/kristal.py check .
python tools/kristal.py build-v9 .
```

## Golden commitments

Logical Artifact : `sha256:ffcfef299a7a8ac38e4e1b10001e1bcaa008c5f3ea801bdb404ad9bef299afd8`

State v9 : `sha256:7ec525b058e256bb235c645c29bc6303159408a5e920e64d798c55d487e31f2d`

La validation conserve aussi le manifest de matérialisation historique et vérifie octets, taille et SHA-256 des blobs sous `knowledge-base/corpus/`.

**Limite :** cette validation ne remplace pas les tests de vérité du domaine, ni la qualification externe, ni la publication.
