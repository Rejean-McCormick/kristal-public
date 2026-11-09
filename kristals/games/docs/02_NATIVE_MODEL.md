# Modèle natif

- **Kind** : `state_rule_action_transition_graph`
- **Description** : Jeux comme systèmes : règles, états, actions, transitions, objectifs et résultats.
- **Axes et coordonnées** : État, règle, action, transition, objectif, résultat.
- **Invariant** : Règle, état, action, transition, objectif et résultat ne sont pas des synonymes.

## Canal canonique de migration

Le Logical Artifact `urn:kristal:games:canonical` possède le contrat `kristal.v6-state-reference/1.0`. Son payload authoring se trouve dans `canon/domain/games.logical-payload.json` et est recalculé sans commitment `precomputed`.

Les modèles métier historiques sont dans `knowledge-base/` : leur forme native demeure autoritaire pour l'interprétation ; la seule enveloppe 3.2.2 ne redéfinit pas les sémantiques.
