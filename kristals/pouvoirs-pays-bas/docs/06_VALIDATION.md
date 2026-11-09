# Validation — Kristal-Pouvoirs-Pays-Bas

Commandes exécutées :

```sh
python tools/kristal.py check .
python tools/build-preserving-v9.py
python knowledge-base/tools/validate.py
```

Le build combiné reconstruit le State v9, vérifie la préservation exacte des engagements, l'intégrité SHA-256 du blob original et, pour le profil v6 natif, la reconstruction de la partie logique après retrait des champs de transport `state_id` et `content_hash`.

State Commitment de référence : `sha256:33a01a6ccc5dc180a044af71bb4c6cc7f6ca581908eebdd09943131e30150ff1`.

Une validation de schéma ou de provenance **ne vérifie pas l'exactitude du droit en vigueur**. Pas de vérification juridique postérieure au corpus.
