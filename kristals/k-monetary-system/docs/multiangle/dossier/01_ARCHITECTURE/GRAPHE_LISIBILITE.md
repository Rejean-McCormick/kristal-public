# Graphe de la transition (vue textuelle)

```mermaid
flowchart TD
  K[kOA : crédit populaire hypothétique] --> M[Médias, signes et marques]
  K --> A[Adoption volontaire]
  K --> I[Propositions à institutions existantes]
  M --> L[Lingots & produits vendus]
  L --> C[Capital K_C : actifs productifs]
  L -. marges réalisées et auditées .-> F[Financement d'amorçage]
  F --> A
  A --> P[K_M : paiement si régime juridiquement défini]
  P --> R[Commerces et usagers]
  P --> E[Réserves, règlement, protection fonds, rachat ou résolution]
  I --> D[Desjardins : décision par membres et organes compétents]
  D --> B[Proposition partage excédents]
  B --> U[Ristournes directes]
  B --> V[FADM : biens collectifs]
  D --> T[Guichets de confiance, si partenariats autorisés]
  T --> S[Ethikos / Konnaxion : interfaces externes]
  C --> H[Dividendes selon profits réels]
  V --> Q[Effets locaux évalués]
  R --> X[Usage économique observé]
  E --> G[Gates comptables et juridiques]
  S --> G
  Q --> G
  H --> G
```

Le graphe structuré `canon/domain/multiangle/graph.json` contient les liens de provenance S/P/W/D/G et est validé pour l'absence d'IDs manquants; il ne simule pas la causalité économique.
