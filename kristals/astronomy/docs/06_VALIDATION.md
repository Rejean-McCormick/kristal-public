# Protocole de validation — Kristal-Astronomy

```sh
python tools/kristal.py check .
python tools/build-preserving-v9.py
```

Le deuxième script exécute `check`, `build-v9`, vérifie les commitments et **tous les segments natifs**, copie leurs manifests sous `build/v9/imported-materializations/`, et fusionne honnêtement les capacités observées dans `build/v9/v9-capabilities.json`.

Golden State Commitment : `sha256:f3d9ccdc2863b562176f4d6f25f5e02d87e989f325bf4d0f67d8e8270aec5b8e`.

Les tests métier propres à `knowledge-base/tools/validate.py`, lorsqu'ils existent, restent distincts des vérifications structurelles. Ils ne sont pas remplacés par `check`.
