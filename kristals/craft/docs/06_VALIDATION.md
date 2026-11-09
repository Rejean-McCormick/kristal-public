# Validation — Kristal-Craft

## Commandes

```shell
python tools/kristal.py check .
python tools/kristal.py build-v9 .
```

## Golden commitments

Logical Artifact : `sha256:9d1783f86a31cef1cf05bb82aaa974e0b14649acaca3f274a1ca7a8f731c9c3a`

State v9 : `sha256:92fbb598e2452b02b0bcec5df97e352be44e899bed1f713c428d72775d49c8d5`

La validation conserve aussi le manifest de matérialisation historique et vérifie octets, taille et SHA-256 des blobs sous `knowledge-base/corpus/`.

**Limite :** cette validation ne remplace pas les tests de vérité du domaine, ni la qualification externe, ni la publication.
