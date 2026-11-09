
## Contraintes de migration propres au domaine

- **Invariant** : Stocks, flux, réservoirs et sphères restent distincts, avec échanges et boucles rétroactives.
- Modèle natif déclaré : `coupled_reservoir_flow_graph`.
- Les fichiers `.kristal/v9/` historiques conservent leur identité logique et leurs profils de matérialisation.
- Ne pas activer `factorization=true` ou `segmentation=true` sans artefact physique produit et testé.
- Toute évolution du canon exige validation sémantique et justification d’un nouveau Logical Commitment.
