# Validation — Kristal-Pouvoirs-Coree-du-Sud

Commandes exécutées :

```sh
python tools/kristal.py check .
python tools/build-preserving-v9.py
python knowledge-base/tools/validate.py
```

Le build combiné reconstruit le State v9, vérifie la préservation exacte des engagements, l'intégrité SHA-256 du blob original et, pour le profil v6 natif, la reconstruction de la partie logique après retrait des champs de transport `state_id` et `content_hash`.

State Commitment de référence : `sha256:386d84f1aedb7f14f23a09b3de9b60f9dd82ffd6e00764a43e9ff00daef929c7`.

Une validation de schéma ou de provenance **ne vérifie pas l'exactitude du droit en vigueur**. Pas de vérification juridique postérieure au corpus.
