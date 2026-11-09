# Protocole de validation — Kristal-Atmosphere

```sh
python tools/kristal.py check .
python tools/build-preserving-v9.py
```

Le deuxième script exécute `check`, `build-v9`, vérifie les commitments et **tous les segments natifs**, copie leurs manifests sous `build/v9/imported-materializations/`, et fusionne honnêtement les capacités observées dans `build/v9/v9-capabilities.json`.

Golden State Commitment : `sha256:e64f7ce8d8433be97d62101e71595d2189a38597d3b1956661f027340e231f96`.

Les tests métier propres à `knowledge-base/tools/validate.py`, lorsqu'ils existent, restent distincts des vérifications structurelles. Ils ne sont pas remplacés par `check`.
