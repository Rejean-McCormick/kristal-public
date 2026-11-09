# Protocole de validation — Kristal-Agriculture

```sh
python tools/kristal.py check .
python tools/build-preserving-v9.py
```

Le deuxième script exécute `check`, `build-v9`, vérifie les commitments et **tous les segments natifs**, copie leurs manifests sous `build/v9/imported-materializations/`, et fusionne honnêtement les capacités observées dans `build/v9/v9-capabilities.json`.

Golden State Commitment : `sha256:8a80b42d934b6854951d06180a12b965b9c0913a77d7f6c7f3dd83e79f8c94ee`.

Les tests métier propres à `knowledge-base/tools/validate.py`, lorsqu'ils existent, restent distincts des vérifications structurelles. Ils ne sont pas remplacés par `check`.
