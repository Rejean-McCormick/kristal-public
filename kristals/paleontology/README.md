# Kristal Paleontology v1.0.0

Kristal Paleontology modélise la **reconstruction du vivant passé à partir du registre géologique** :

`fossile → organisme → strate → âge → environnement → lignée`

Cette chaîne n’est pas traitée comme une suite de certitudes. Elle devient une **chaîne d’inférence** où les observations directes (spécimen, matrice, position stratigraphique) sont séparées des interprétations (identification, âge, paléoenvironnement, phylogénie).

Le paquet est natif **Kristal Standard 6.0** et utilise `kristal_state` comme couche canonique.

## Invariants sémantiques

- **fossile ≠ organisme complet**;
- **fossile ≠ ancêtre direct**;
- **strate ≠ âge numérique exact**;
- **âge relatif ≠ âge numérique**;
- **milieu de dépôt ≠ automatiquement habitat de vie**;
- **première occurrence ≠ apparition évolutive exacte**;
- **dernière occurrence ≠ extinction exacte**;
- **assemblage fossile ≠ photographie d’un instant**;
- **similarité morphologique ≠ homologie**;
- **registre incomplet ≠ absence d’information**.

## Contenu

- 164 assertions atomiques;
- 84 référents;
- 14 sources de référence;
- fossiles corporels et traces;
- fossilisation, taphonomie et biais de préservation;
- stratigraphie, superposition, corrélation et biozones;
- âges relatifs et numériques, datation radiométrique et échelle des temps géologiques;
- reconstruction des milieux de dépôt et paléoenvironnements;
- caractères, homologie/homoplasie, cladistique, lignées et incertitude phylogénétique;
- index dérivés, rapport de couverture et validation v6.

## Frontière

Inclus : fossiles et occurrences, taphonomie, contexte stratigraphique, datation, paléoenvironnement et placement phylogénétique.

Exclus volontairement : catalogue exhaustif des taxons fossiles, bases mondiales de localités, protocoles de fouille, géochimie isotopique détaillée, sédimentologie complète, paléoclimat exhaustif et reconstruction biomécanique spécialisée.

## Modèle épistémique

Le Kristal conserve explicitement les niveaux suivants :

`observation → contexte → contrainte temporelle → reconstruction environnementale → hypothèse phylogénétique`

Un maillon peut être révisé sans invalider nécessairement les autres.

## Fichiers principaux

```text
knowledge-base/
  corpus/paleontology.kristal-state.json
  corpus/referents.json
  corpus/index.json
  corpus/coverage-report.json
  corpus/validation-report.json
  sources/source-catalog.json
  sources/evidence-registry.json
  documentation/CONTENT_BOUNDARY.md
  documentation/EVIDENCE_CHAIN.md
  documentation/SEMANTIC_GUARDRAILS.md
  schemas/kristal-state.schema.json
  tools/validate.py
```
