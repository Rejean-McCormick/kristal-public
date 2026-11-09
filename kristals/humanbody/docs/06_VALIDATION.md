# Validation — Kristal-HumanBody

Effectuer depuis la racine du Kristal :

```bash
python tools/kristal.py check .
python tools/build_with_materializations.py .
```

Le build étend `build-v9` par l'enregistrement validé des anciennes matérialisations v9 : schéma framework, source/contrat/commitment, tailles et SHA-256 de chaque blob. Il compare aussi le State Commitment au snapshot v9 historique.

Le State Commitment original est `sha256:15ca3b248c573d0870258e09e6c1a597f3ddd27f815cb2d498dacf7c064adc05`.

Cette passe ne prétend pas avoir revalidé toute la sémantique métier : les rapports historiques sont conservés comme preuves séparées. Les déclarations `reconstructability.lossless` anciennes sont vérifiées comme déclarations, sans reconstruire indépendamment toutes les ressources.
