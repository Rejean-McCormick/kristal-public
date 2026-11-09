# Validation — Kristal-Pouvoirs-Australie

Commandes exécutées :

```sh
python tools/kristal.py check .
python tools/build-preserving-v9.py
python knowledge-base/tools/validate.py
```

Le build combiné reconstruit le State v9, vérifie la préservation exacte des engagements, l'intégrité SHA-256 du blob original et, pour le profil v6 natif, la reconstruction de la partie logique après retrait des champs de transport `state_id` et `content_hash`.

State Commitment de référence : `sha256:fa3e5f53d784509e2c146ad2c823e6faab750b8ea6e16a019ac4454ae5fd84e5`.

Une validation de schéma ou de provenance **ne vérifie pas l'exactitude du droit en vigueur**. Pas de vérification juridique postérieure au corpus.
