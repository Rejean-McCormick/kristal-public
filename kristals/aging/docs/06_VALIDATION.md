# Protocole de validation — Kristal-Aging

```sh
python tools/kristal.py check .
python tools/build-preserving-v9.py
```

Le deuxième script exécute `check`, `build-v9`, vérifie les commitments et **tous les segments natifs**, copie leurs manifests sous `build/v9/imported-materializations/`, et fusionne honnêtement les capacités observées dans `build/v9/v9-capabilities.json`.

Golden State Commitment : `sha256:b3a52020a6774ff8d58615d11366ec994d8d81aa8f3519500c959cf285b91903`.

Les tests métier propres à `knowledge-base/tools/validate.py`, lorsqu'ils existent, restent distincts des vérifications structurelles. Ils ne sont pas remplacés par `check`.
