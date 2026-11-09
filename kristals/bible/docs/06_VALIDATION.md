# Protocole de validation — Kristal-Bible

```sh
python tools/kristal.py check .
python tools/build-preserving-v9.py
```

Le deuxième script exécute `check`, `build-v9`, vérifie les commitments et **tous les segments natifs**, copie leurs manifests sous `build/v9/imported-materializations/`, et fusionne honnêtement les capacités observées dans `build/v9/v9-capabilities.json`.

Golden State Commitment : `sha256:fdfe6188a76261d875c77ab743e6cdec138bf41152fa74b0b6de20c7091b72d6`.

Les tests métier propres à `knowledge-base/tools/validate.py`, lorsqu'ils existent, restent distincts des vérifications structurelles. Ils ne sont pas remplacés par `check`.
