# Kristal-CivilEngineering

**Version 1.0.0 — Kristal Standard 6.0**

Kristal-CivilEngineering est un corpus statique, traçable et généraliste de **génie civil**. Son expression de navigation principale est :

`charge × matériau × géométrie × sol → ouvrage`

Le symbole `×` signifie ici **couplage** : aucun de ces termes ne détermine seul l’ouvrage. Les actions créent des sollicitations; la géométrie et les conditions d’appui déterminent leur distribution; les matériaux donnent des lois de comportement et résistances; le terrain fournit support, contraintes et aléas géotechniques. La conception résulte de leurs interactions sous des critères d’états limites et de cycle de vie.

## Distinctions structurantes

- **charge ≠ sollicitation interne ≠ contrainte** ;
- **propriété matériau ≠ résistance d’un élément** ;
- **géométrie ≠ matériau**, mais les deux déterminent la rigidité et la capacité ;
- **capacité portante ≠ tassement** : rupture et serviceabilité géotechniques sont distinctes ;
- **superstructure ≠ fondation ≠ terrain** ;
- **résistance ≠ serviceabilité ≠ durabilité ≠ résilience** ;
- les valeurs de calcul et facteurs restent **dépendants du code, du site et du projet**.

## Canonique

- `knowledge-base/corpus/civil-engineering.kristal-state.json` — état v6 canonique
- `knowledge-base/corpus/referents.json` — registre des concepts
- `knowledge-base/sources/source-catalog.json` — catalogue des sources
- `knowledge-base/corpus/civil-engineering-design-graph.json` — graphe complet
- projections : charges, matériaux/géométrie, géotechnique, ouvrages, états limites/cycle de vie

### Taille

- Référents : **141**
- Assertions : **238**
- Sources : **17**
