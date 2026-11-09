# Modèle épistémique

## Régimes d'information

Le dépôt sépare explicitement : document source, terme/définition source, objet analytique structuré et assertion Kristal compilée. Les pages wiki et les fichiers canoniques du dépôt source gardent des statuts distincts. Une reconstruction analytique n'est pas présentée comme une citation textuelle.

## Provenance épistémique

Les assertions conservent leurs références et leur type de claim. La couche Scholarly Evidence Backbone distingue le candidat bibliographique de l'EvidenceLink promu après revue. Les rôles de preuve peuvent notamment supporter, définir, attribuer, illustrer, qualifier, disputer ou contredire.

## Autorité

`CURRENT-CORE`, `CURRENT-EXPERIMENTAL`, `CURRENT-DESIGN-NOTES`, `LEGACY-PROPOSAL` et `ANALYTICAL-RECONSTRUCTION` décrivent des statuts de source ou de maturité, **pas un classement automatique de vérité**. Les notes confirmées par l'architecte restent des intentions de design tant qu'une preuve technique ou d'adoption indépendante manque.

## Incertitude / conflits / inconnus

Les désaccords entre documents sont préservés. Les claims techniques actuels restent provisoires sans spécification ou code direct. La multiplicité de notices n'implique pas l'indépendance des preuves. La valeur par défaut de l'indépendance savante peut rester `unknown`.

## Provenance de build

`knowledge-base/tools/build.py` produit de manière déterministe le Structured Epistemic State, l'index et les EvidenceLinks compilés. Cette dérivation informatique est séparée de la provenance épistémique des claims.

## Politique des sorties IA

Toute sortie IA est une proposition jusqu'à validation explicite. Elle ne peut pas promouvoir seule un candidat documentaire, inventer une autorité ou modifier silencieusement les statuts épistémiques.
