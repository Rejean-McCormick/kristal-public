# Modèle natif — Kristal-EngineeringConstraints

Le modèle déclaré par `.kristal/v9/domain-profile.json` est : **requirements / architecture / tradeoff / verification traceability graph**.

Axe canonique historique : `need → requirements → architecture → tradeoff → verification`.

## Distinctions à préserver

- iterative traceability
- tradeoff decision
- verification
- validation

## Supports locaux du modèle

- `knowledge-base/corpus/traceability-model.json`
- `knowledge-base/corpus/tradeoff-model.json`
- `knowledge-base/corpus/verification-model.json`

L'unique artefact logique v9 importé possède le contrat `kristal.portable-epistemic-state/6.0` et porte le payload du portable state v6 original. La nouvelle structure n'aplatit pas les primitives du domaine.
