# Validation — Kristal-Pouvoirs-France

Commandes exécutées :

```sh
python tools/kristal.py check .
python tools/build-preserving-v9.py
python knowledge-base/tools/validate.py
```

Le build combiné reconstruit le State v9, vérifie la préservation exacte des engagements, l'intégrité SHA-256 du blob original et, pour le profil v6 natif, la reconstruction de la partie logique après retrait des champs de transport `state_id` et `content_hash`.

State Commitment de référence : `sha256:abd1fe8fc65dfa6730886124c4b0cb159bf69ed8a46ccddb5dda3798d7e0f880`.

Une validation de schéma ou de provenance **ne vérifie pas l'exactitude du droit en vigueur**. Pas de vérification juridique postérieure au corpus.
