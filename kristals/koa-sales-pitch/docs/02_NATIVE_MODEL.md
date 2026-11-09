# Modèle natif

## Primitives du domaine

Les primitives dominantes sont : question canonique, variantes de question, audience, intention, réponse par profondeur, référence de preuve, posture de preuve, interdits de formulation, routage conversationnel et carte live.

Le state v6 ajoute provenance, avertissements, profils de lecteurs et extensions vers les règles de preuve, la terminologie, les pathways, le meeting-state et les autres modèles de support.

## Relations / transformations

`sources éditoriales → état structuré Q&A → profils/index → vues de rencontre → requête`. Les projections de lecture n'acquièrent pas d'autorité en étant matérialisées.

## Dimensions internes

Les axes épistémiques majeurs sont besoin/problème, technique/solution, commercial/marché et impact. Les axes de lecture incluent audience, famille de question, priorité et profondeur de réponse.

## Forme native retenue

`structured_qa_evidence_state`

Cette forme conserve simultanément les réponses, leur contexte, leurs limites, leur provenance et leur routage conversationnel.

## Logical Contracts v9

Le Logical Artifact canonique utilise `kristal.v6-state-reference/1.0`. Son commitment est `kristal.logical/jcs-sha256-v1` et est préservé depuis l'enveloppe v9 historique.

## Pourquoi cette forme ne perd pas d'information essentielle

Réduire le Kristal à une simple collection de textes ferait disparaître les niveaux de réponse, la posture de preuve, les interdits, le routage et les liens de provenance. Réduire le tout à un graphe générique masquerait la logique Q&A opérationnelle.

## Alternatives rejetées

- document Markdown unique ;
- ontologie générique unique ;
- fusion des sources et du canon ;
- promotion des vues/index au rang de vérité.
