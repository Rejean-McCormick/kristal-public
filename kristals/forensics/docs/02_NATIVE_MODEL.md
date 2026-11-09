# Modèle natif

- **Kind** : `evidence_workflow_typed_graph`
- **Description** : Trace, acquisition, analyse, comparaison, interprétation et conclusion limitée.
- **Axes et coordonnées** : Étapes d’examen, provenance, méthode, qualité, incertitude, limites et propositions.
- **Invariant** : Observation ≠ interprétation ≠ conclusion ; les trois plans matériel, analytique et inférentiel ne se confondent pas.

## Canal canonique de migration

Le Logical Artifact `urn:kristal:forensics:canonical` possède le contrat `kristal.v6-state-reference/1.0`. Son payload authoring se trouve dans `canon/domain/forensics.logical-payload.json` et est recalculé sans commitment `precomputed`.

Les modèles métier historiques sont dans `knowledge-base/` : leur forme native demeure autoritaire pour l'interprétation ; la seule enveloppe 3.2.2 ne redéfinit pas les sémantiques.
