# Modèle natif

- **Kind** : `typed_genotype_phenotype_relation_graph`
- **Description** : Locus, variants, génotypes, expression, phénotypes et transmission.
- **Axes et coordonnées** : Locus, variant, génotype, expression, phénotype, transmission.
- **Invariant** : Variant ≠ maladie : aucune recommandation clinique ou risque personnel n’est inféré du modèle de référence.

## Canal canonique de migration

Le Logical Artifact `urn:kristal:genetics:canonical` possède le contrat `kristal.v6-state-reference/1.0`. Son payload authoring se trouve dans `canon/domain/genetics.logical-payload.json` et est recalculé sans commitment `precomputed`.

Les modèles métier historiques sont dans `knowledge-base/` : leur forme native demeure autoritaire pour l'interprétation ; la seule enveloppe 3.2.2 ne redéfinit pas les sémantiques.
