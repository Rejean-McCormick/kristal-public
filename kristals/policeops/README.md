# Kristal-PoliceOps

**Type :** Local Kristal 3.2.2  
**Workspace :** `kristal.local-workspace/3.2.0`  
**État sémantique cible :** `kristal.state/9.0`  
**Lifecycle local :** `building`

PoliceOps cristallise un corpus épistémique police/judiciaire centré sur Québec/Lévis. La normalisation Local 3.2.2 ajoute l’enveloppe d’authoring actuelle **sans réécrire le corpus natif**.

## Canon

Le Logical Artifact canonique demeure :

`knowledge-base/corpus/policeops.structured-epistemic-state.json`

Il contient 538 assertions. Les anciens `.kristal/v8` et `.kristal/v9` sont conservés comme projections/builds legacy dérivés et comme preuve de migration, pas comme nouvelle source d’autorité.

## Limites connues

- le corpus natif est encore `artifact_status=working`;
- sa validation sémantique globale est `not_evaluated` et sa reconnaissance est `under_review`;
- le snapshot ne contient pas les objets physiques `objects/` du Source Store externe;
- les transitions judiciaires restent des projections à relier à des sources juridiques versionnées et validées avant usage décisionnel en production.

## Validation

```bash
python knowledge-base/tools/validate.py
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python tools/kristal.py inspect .
```

Le build v9 n’est ni une publication ni une activation. Aucun hébergement GitHub n’est inventé par cette normalisation.

## Source Store

`external-source-library/` reste une matérialisation externe/non canonique. Le snapshot reçu conserve ses métadonnées et index, mais pas toutes les représentations physiques référencées.

## Historique

Le README antérieur à la normalisation 3.2.2 est conservé dans `docs/history/README.pre-local-3.2.2.md`.
