# Intention et scope

## Pourquoi ce Kristal existe

Ce Kristal représente la couche **King Klown MEDIA** du domaine King Klown : œuvres, manifestations média, liens avec les événements de l'Univers, alias, règles de lecture et éléments épistémiques nécessaires pour interpréter ces relations. La normalisation 3.2.2 est architecturale : elle ne révise pas le contenu de domaine.

## Corpus / problème de départ

Le snapshot reçu contient une architecture v9 antérieure au Local Authoring Kit 3.2.2, avec 9 Logical Artifacts et une projection de compatibilité v6/v8. Le contenu v9 est déjà qualifié par ses outils historiques ; l'écart principal est l'absence de l'enveloppe `kristal.local-workspace/3.2.0`.

## Résultats attendus

- conserver `state_ref = urn:kristal:state:king-klown-media` ;
- conserver le Logical Commitment d'état `sha256:f237db441d6946b45b7cc06a82e96afe3f43d00dbb6192274e27785bb4f599ba` ;
- exposer les Logical Artifacts canoniques sous `canon/` sans réécriture sémantique ;
- distinguer canon, sources, projections, builds, matérialisations et opérations de publication/activation ;
- permettre `check` puis `build-v9` avec le kit 3.2.2.
