# Frontière sémantique

## Subject / territoire

Le territoire est la topologie du pouvoir et les mécanismes analytiques Power Dynamics associés : domaines, relations, ressources/capacités, dynamiques, conversions, routage, retours, boucles, autorité, reconnaissance/coordination, contre-pouvoirs et instruments d'évaluation.

## Possède

Le Kristal possède son modèle conceptuel local, ses assertions compilées et attribuées, ses contrats analytiques natifs, ses règles épistémiques locales et les liens de preuve qui ont été explicitement promus/qualifiés.

## Ne possède pas

Il ne possède ni les corpus savants distants, ni leur disponibilité, ni les index SQLite/FTS locaux du CorpusIndex. Un résultat de recherche externe reste un **candidat documentaire** tant qu'il n'a pas été revu et lié. Le Kristal ne transforme pas non plus un statut de source récent en rang de vérité.

## Relations avec d'autres composants

`corpus-indexer/` est un sidecar en lecture du Kristal : il peut importer des graines et produire des candidats, mais il ne modifie pas le canon. Les anciens paquets `.kristal/v8` et `.kristal/v9` sont conservés comme représentations/materialisations dérivées.

## State identity v9

- `state_ref`: `urn:kristal:state:power`
- `authority_ref`: `urn:kristal:authority:power`

Toute référence externe destinée à participer à l'état v9 devra être pinée à un Logical Commitment avant publication.
