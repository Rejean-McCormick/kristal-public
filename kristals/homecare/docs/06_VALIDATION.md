# Validation — Kristal-HomeCare

Effectuer depuis la racine du Kristal :

```bash
python tools/kristal.py check .
python tools/build_with_materializations.py .
```

Le build étend `build-v9` par l'enregistrement validé des anciennes matérialisations v9 : schéma framework, source/contrat/commitment, tailles et SHA-256 de chaque blob. Il compare aussi le State Commitment au snapshot v9 historique.

Le State Commitment original est `sha256:de24b8d9ac4f924f4b6ea71b635cfe324a9875fa78680eab3c7ac6237f799895`.

Cette passe ne prétend pas avoir revalidé toute la sémantique métier : les rapports historiques sont conservés comme preuves séparées. Les déclarations `reconstructability.lossless` anciennes sont vérifiées comme déclarations, sans reconstruire indépendamment toutes les ressources.
