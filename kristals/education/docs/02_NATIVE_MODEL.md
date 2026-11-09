# Modèle natif — Kristal-Education

Le modèle déclaré par `.kristal/v9/domain-profile.json` est : **learner-state / objective / activity / evidence / progression cycle**.

Axe canonique historique : `state(t) → objective → activity → evidence → interpretation → decision → state(t+1)`.

## Distinctions à préserver

- activity ≠ objective
- evidence ≠ mastery
- score ≠ competence
- growth ≠ mastery
- retention ≠ transfer

## Supports locaux du modèle

- `knowledge-base/corpus/learning-cycle-model.json`
- `knowledge-base/corpus/learning-record-model.json`
- `knowledge-base/corpus/objective-alignment-model.json`
- `knowledge-base/corpus/assessment-evidence-model.json`
- `knowledge-base/corpus/progression-model.json`

L'unique artefact logique v9 importé possède le contrat `kristal.portable-epistemic-state/6.0` et porte le payload du portable state v6 original. La nouvelle structure n'aplatit pas les primitives du domaine.
