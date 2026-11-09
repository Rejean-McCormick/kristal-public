# Validation — Kristal-History

Effectuer depuis la racine du Kristal :

```bash
python tools/kristal.py check .
python tools/build_with_materializations.py .
```

Le build étend `build-v9` par l'enregistrement validé des anciennes matérialisations v9 : schéma framework, source/contrat/commitment, tailles et SHA-256 de chaque blob. Il compare aussi le State Commitment au snapshot v9 historique.

Le State Commitment original est `sha256:6b6e001618f32e71e39e0cc4f4a2ac87de481db07fcebd769c3ee57a3ed4e235`.

Cette passe ne prétend pas avoir revalidé toute la sémantique métier : les rapports historiques sont conservés comme preuves séparées. Les déclarations `reconstructability.lossless` anciennes sont vérifiées comme déclarations, sans reconstruire indépendamment toutes les ressources.
