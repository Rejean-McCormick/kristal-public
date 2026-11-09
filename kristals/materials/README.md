# Kristal-Materials

**Version:** 1.0.0  
**Édition:** 2026-10-02  
**Format canonique:** Kristal Standard 6.0 (`kristal_state`)

Kristal-Materials est un corpus statique, traçable et orienté IA consacré à la **science des matériaux**.

## Axe conceptuel

`structure → propriété → comportement → usage`

Quatre axes contextuels empêchent les raccourcis :

`composition / identité → procédé / état → environnement → méthode de mesure`

Le principe fondamental est qu’une valeur de propriété n’appartient pas simplement à un nom de matériau. Elle appartient à un **matériau dans un état déterminé, mesuré selon une méthode et sous des conditions déterminées**.

## Contenu

- familles : métaux/allisages, céramiques/verres/cimentaires, polymères, composites, semi-conducteurs, biomatériaux, poreux, nanostructurés, revêtements;
- structure : phases, cristallinité, grains, joints, texture, défauts, porosité, interfaces, architecture fibreuse/polymère, état de surface;
- propriétés : mécaniques, thermiques, électriques, magnétiques, optiques, environnementales et transport;
- comportements : élasticité/plasticité, viscoélasticité, fluage, fatigue, rupture, usure, corrosion, transformations, diffusion, vieillissement;
- procédés : coulée, déformation, traitements thermiques, frittage, fabrication additive, soudage, polymères, composites, dépôts et surfaces;
- usages : structure, haute température, cyclique, corrosion, tribologie, électrique, thermique, optique, barrière, biomédical;
- mesures : contexte, unité, méthode, état, géométrie, orientation, température, fréquence/vitesse, environnement et incertitude.

## Frontière

Ce Kristal n’est ni un catalogue fournisseur, ni une base d’allowables de conception. Une relation `candidate_for` signifie seulement « famille plausible à considérer ». Une sélection d’ingénierie exige le grade précis, l’état, le lot, la géométrie, les charges, l’environnement, la durée, les facteurs de sécurité et les normes applicables.

Les textes propriétaires ASTM sont référencés comme standards externes; ils ne sont pas recopiés.

## Fichiers centraux

- `knowledge-base/corpus/materials.kristal-state.json`
- `knowledge-base/corpus/materials.referent-registry.json`
- `knowledge-base/sources/measurement_context.json`
- `knowledge-base/sources/structure_model.json`
- `knowledge-base/sources/property_model.json`
- `knowledge-base/sources/behavior_model.json`
- `knowledge-base/sources/processing_model.json`
- `validation/materials-validation-report.json`
