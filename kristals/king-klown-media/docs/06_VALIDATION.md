# Validation du domaine et lifecycle

## Invariants structurels

- 9 Logical Artifacts v9 membres de l'état ;
- identifiants d'artefact uniques ;
- engagements précomputés valides ;
- `state_ref = urn:kristal:state:king-klown-media` ;
- séparation canon / build / matérialisation / activation.

## Invariants épistémiques

- UCKK Médiathèque reste primaire pour l'inventaire média/URL ;
- les manifestations média ne créent pas automatiquement de nouvelles œuvres ni de nouveaux événements diégétiques ;
- le nom civil de `AUTHOR_REAL` ne doit pas être reconstruit ;
- les statuts épistémiques existants restent distincts ;
- les contradictions ne sont pas supprimées silencieusement.

## Tests de reconstruction

Le validateur historique vérifie notamment la stabilité de la projection v6, les comptes média, les relations vers les œuvres, les schémas v9, les Logical Commitments, les matérialisations, l'échange et les golden vectors. Le kit 3.2.2 ajoute `check` et un build v9 déterministe à partir du registre d'authoring.

## Logical Commitments

Profil artefact : `kristal.logical/jcs-sha256-v1`. Profil état : `kristal.state-commitment/jcs-sha256-v1`. L'état attendu après normalisation reste `sha256:f237db441d6946b45b7cc06a82e96afe3f43d00dbb6192274e27785bb4f599ba`.

## Critères de publication

`check` puis `build-v9` doivent réussir et le State Logical Commitment reconstruit doit être identique à l'engagement historique. Toute qualification, publication ou activation réseau reste une étape séparée et explicitement demandée.
