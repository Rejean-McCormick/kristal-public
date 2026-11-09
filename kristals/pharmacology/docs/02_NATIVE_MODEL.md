# Modèle natif

`native_model.kind = pharmacology_exposure_mechanism_risk_graph` (qualification descriptive de la forme existante, non conversion).

Graphe mécanistique substance/cible/exposition/effet/risque, distinguant PK, PD et unités d’exposition.

**Orientation principale :** substance → cible → mécanisme → dose/exposition → effet → risque.

**Invariants :** Dose administrée, exposition interne, effet pharmacodynamique et risque demeurent des notions distinctes.

L'engagement v9 existant porte sur le payload logique à `canon/domain/v9-logical-payload.json`. Les relations et structures déjà déclarées dans le corpus historique demeurent la référence détaillée. Le seul changement de layout ne crée pas de nouveaux prédicats ni de nouveaux IDs.
