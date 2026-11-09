# Modèle natif

## Primitives du domaine

Le modèle natif est composé de neuf artefacts logiques : **entities**, **works**, **universe events**, **media semantic layer**, **aliases**, **epistemic core**, **contradictions**, **reader policy** et **creator clarifications**.

## Relations / transformations

La couche média dépend des œuvres et événements ; les alias dépendent des entités et de la couche média ; le noyau épistémique dépend notamment des entités, œuvres, événements, reader policy et clarifications ; le registre de contradictions dépend du noyau épistémique. Ces dépendances sont conservées dans les Logical Artifacts eux-mêmes.

## Dimensions internes

Les dimensions utiles incluent le type d'objet (entité, œuvre, événement, manifestation), la plateforme média, les liens œuvre/événement/arcs, le statut épistémique et l'autorité. Elles ne sont pas aplaties en un schéma universel unique.

## Forme native retenue

`layered-registry-ledger-semantic-graph`

Le modèle combine des registres, un ledger d'événements, un graphe de relations sémantiques média et une couche épistémique transversale.

## Logical Contracts v9

Les contrats et versions sont ceux portés par `canon/state.index.json` et les neuf Logical Artifacts. Les engagements sont conservés en mode `precomputed` afin qu'une migration physique vers `canon/` ne change aucun Logical Commitment.

## Pourquoi cette forme ne perd pas d'information essentielle

Transformer l'ensemble en une simple table d'assertions ferait perdre la distinction entre registres structuraux, ledger d'événements, couche média, politiques de lecture, contradictions et provenance épistémique.

## Alternatives rejetées

- un JSON universel unique comme nouvelle source de vérité ;
- la projection v6 comme seul canon v9 ;
- les index v8 comme autorité sémantique ;
- la duplication des œuvres pour chaque plateforme média.
