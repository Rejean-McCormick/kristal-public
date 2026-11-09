# Kristal-Hydrology

**Version 1.0.0 — Kristal Standard 6.0**

Kristal-Hydrology est un corpus statique, traçable et généraliste d’**hydrologie**. Son axe de navigation principal est :

`précipitation → infiltration → aquifère → écoulement → évaporation`

Cet axe est une vue pédagogique. Le modèle canonique est un **graphe couplé de stocks et flux** : l’eau peut être interceptée, stockée dans la neige ou le sol, ruisseler, percoler vers la nappe, ressortir vers un cours d’eau, ou retourner à l’atmosphère.

## Distinctions structurantes

- **infiltration ≠ recharge de nappe** ;
- **stock ≠ flux ≠ variation de stockage** ;
- **bassin versant de surface ≠ système aquifère** ;
- **débit de cours d’eau ≠ hauteur d’eau** ;
- **évaporation ≠ transpiration ≠ évapotranspiration** ;
- **ET de référence ≠ ET réelle** ;
- les échanges nappe–rivière peuvent être **bidirectionnels**.

## Canonique

- `knowledge-base/corpus/hydrology.kristal-state.json` — état v6 canonique
- `knowledge-base/corpus/referents.json` — registre des concepts
- `knowledge-base/sources/source-catalog.json` — catalogue des sources
- `knowledge-base/corpus/hydrologic-stock-flow-graph.json` — graphe complet
- projections : groundwater, watershed, evapotranspiration, water balance

### Taille

- Référents : **133**
- Assertions : **208**
- Sources : **16**
