# Validation — Kristal-Hydrology

Effectuer depuis la racine du Kristal :

```bash
python tools/kristal.py check .
python tools/build_with_materializations.py .
```

Le build étend `build-v9` par l'enregistrement validé des anciennes matérialisations v9 : schéma framework, source/contrat/commitment, tailles et SHA-256 de chaque blob. Il compare aussi le State Commitment au snapshot v9 historique.

Le State Commitment original est `sha256:bee2f3e0bbf4cc06fa3e6f2193602589000709b7ad54c59ee015d741a8a196e0`.

Cette passe ne prétend pas avoir revalidé toute la sémantique métier : les rapports historiques sont conservés comme preuves séparées. Les déclarations `reconstructability.lossless` anciennes sont vérifiées comme déclarations, sans reconstruire indépendamment toutes les ressources.
