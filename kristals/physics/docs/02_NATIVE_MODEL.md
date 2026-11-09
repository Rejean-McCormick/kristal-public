# Modèle natif

`native_model.kind = multiscale_multiplex_physical_state_graph` (qualification descriptive de la forme existante, non conversion).

Graphe physique multiplexe/multi-échelle centré sur le système, les états et les évolutions sous régime de validité.

**Orientation principale :** PhysicalSystem → PhysicalState(t) → process → PhysicalState(t+Δt).

**Invariants :** PhysicalSystem != PhysicalState ; modèle != loi ; mesure != valeur idéale ; validité dépend du régime.

L'engagement v9 existant porte sur le payload logique à `canon/domain/v9-logical-payload.json`. Les relations et structures déjà déclarées dans le corpus historique demeurent la référence détaillée. Le seul changement de layout ne crée pas de nouveaux prédicats ni de nouveaux IDs.
