# Validation — Kristal-Pouvoirs-Finlande

Commandes exécutées :

```sh
python tools/kristal.py check .
python tools/build-preserving-v9.py
python knowledge-base/tools/validate.py
```

Le build combiné reconstruit le State v9, vérifie la préservation exacte des engagements, l'intégrité SHA-256 du blob original et, pour le profil v6 natif, la reconstruction de la partie logique après retrait des champs de transport `state_id` et `content_hash`.

State Commitment de référence : `sha256:d3d6e89d8b7a6193f2ef0084bcca065b8cd0fda92a42e9998dda8ab81c1ca398`.

Une validation de schéma ou de provenance **ne vérifie pas l'exactitude du droit en vigueur**. Pas de vérification juridique postérieure au corpus.
