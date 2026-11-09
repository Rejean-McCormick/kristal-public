# Validation — Kristal-Infrastructure

Effectuer depuis la racine du Kristal :

```bash
python tools/kristal.py check .
python tools/build_with_materializations.py .
```

Le build étend `build-v9` par l'enregistrement validé des anciennes matérialisations v9 : schéma framework, source/contrat/commitment, tailles et SHA-256 de chaque blob. Il compare aussi le State Commitment au snapshot v9 historique.

Le State Commitment original est `sha256:db12ec9e4bfcbe0794ee87be217d28f813695cd1900bfaf0d7f8bf4649b2f6bc`.

Cette passe ne prétend pas avoir revalidé toute la sémantique métier : les rapports historiques sont conservés comme preuves séparées. Les déclarations `reconstructability.lossless` anciennes sont vérifiées comme déclarations, sans reconstruire indépendamment toutes les ressources.
