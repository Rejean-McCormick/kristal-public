
## Contraintes de migration propres au domaine

- **Invariant** : Schéma, valeur, transformation, provenance, qualité et requête ne sont pas interchangeables.
- Modèle natif déclaré : `typed_data_lineage_graph`.
- Les fichiers `.kristal/v9/` historiques conservent leur identité logique et leurs profils de matérialisation.
- Ne pas activer `factorization=true` ou `segmentation=true` sans artefact physique produit et testé.
- Toute évolution du canon exige validation sémantique et justification d’un nouveau Logical Commitment.
