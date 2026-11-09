# Modèle natif

`native_model.kind = procedural_transformation_graph_and_family_variants` (qualification descriptive de la forme existante, non conversion).

Programmes culinaires de transformation de matière, familles, variantes versionnées, sources et graphes procéduraux.

**Orientation principale :** RecipeFamily → RecipeVariant → transformations/états → résultats.

**Invariants :** RecipeFamily != RecipeVariant != RecipeSourceInstance ; préserver étapes, états et provenance.

L'engagement v9 existant porte sur le payload logique à `canon/domain/v9-logical-payload.json`. Les relations et structures déjà déclarées dans le corpus historique demeurent la référence détaillée. Le seul changement de layout ne crée pas de nouveaux prédicats ni de nouveaux IDs.
