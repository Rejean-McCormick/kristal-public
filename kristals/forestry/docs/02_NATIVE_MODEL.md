# Modèle natif

- **Kind** : `forest_stand_temporal_transition_model`
- **Description** : Peuplements forestiers, états dans le temps, croissance, perturbations, interventions et suivi.
- **Axes et coordonnées** : Peuplement, état, temps, perturbations, régénération et sylviculture.
- **Invariant** : Composition, structure et mesures restent distinctes, et un état observé n’est pas une transition présumée.

## Canal canonique de migration

Le Logical Artifact `urn:kristal:forestry:canonical` possède le contrat `kristal.v6-state-reference/1.0`. Son payload authoring se trouve dans `canon/domain/forestry.logical-payload.json` et est recalculé sans commitment `precomputed`.

Les modèles métier historiques sont dans `knowledge-base/` : leur forme native demeure autoritaire pour l'interprétation ; la seule enveloppe 3.2.2 ne redéfinit pas les sémantiques.
