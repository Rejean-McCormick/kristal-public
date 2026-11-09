# Modèle natif

- **Kind** : `financial_claim_temporal_relation_graph`
- **Description** : Actifs et passifs, droits/obligations, flux datés, risque, rendement, mesure et valorisation.
- **Axes et coordonnées** : Flux datés, devise, instrument/claim, scénario, facteurs de risque et méthode de mesure.
- **Invariant** : Le risque et le prix observé restent distincts des hypothèses et valorisations modélisées.

## Canal canonique de migration

Le Logical Artifact `urn:kristal:finance:canonical` possède le contrat `kristal.v6-state-reference/1.0`. Son payload authoring se trouve dans `canon/domain/finance.logical-payload.json` et est recalculé sans commitment `precomputed`.

Les modèles métier historiques sont dans `knowledge-base/` : leur forme native demeure autoritaire pour l'interprétation ; la seule enveloppe 3.2.2 ne redéfinit pas les sémantiques.
