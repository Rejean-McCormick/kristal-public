# Modèle natif

`native_model.kind = population_exposure_intervention_outcome_graph` (qualification descriptive de la forme existante, non conversion).

Graphe population/contexte/exposition/intervention/résultat et mesures avec prise en compte des distributions.

**Orientation principale :** population → contexte → exposition → intervention → résultats.

**Invariants :** Le contexte, les expositions, les interventions et les résultats sont distincts et sensibles aux populations.

L'engagement v9 existant porte sur le payload logique à `canon/domain/v9-logical-payload.json`. Les relations et structures déjà déclarées dans le corpus historique demeurent la référence détaillée. Le seul changement de layout ne crée pas de nouveaux prédicats ni de nouveaux IDs.
