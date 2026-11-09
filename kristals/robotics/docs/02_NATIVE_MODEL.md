# Modèle natif

`native_model.kind = perception_estimation_control_feedback_graph` (qualification descriptive de la forme existante, non conversion).

Boucle de robotique perception, estimation d’état, planification/décision, actionnement et rétroaction.

**Orientation principale :** perception → estimation → décision → action → rétroaction.

**Invariants :** Monde réel, mesure, état estimé, décision et action ne sont pas des identités interchangeables.

L'engagement v9 existant porte sur le payload logique à `canon/domain/v9-logical-payload.json`. Les relations et structures déjà déclarées dans le corpus historique demeurent la référence détaillée. Le seul changement de layout ne crée pas de nouveaux prédicats ni de nouveaux IDs.
