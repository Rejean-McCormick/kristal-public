# Kristal Medicine v1.0.0

Kristal Medicine décrit l’**état clinique** comme un graphe de référence :

`normal / référence → anomalie → syndrome → diagnostic → intervention → résultat`

Cette chaîne sert de **navigation**, pas de causalité ni de séquence obligatoire. La médecine réelle est itérative : certaines étapes sont absentes, répétées, parallèles ou révisées.

## Ce que le Kristal modélise

Le noyau couvre la différence entre référence et anomalie, symptômes/signes/constats, syndrome, raisonnement diagnostique probabiliste, test diagnostique, incertitude, décision d’intervention, bénéfices/risques, préférences, suivi, résultats cliniques et pronostic.

## Invariants sémantiques

- **intervalle de référence ≠ santé absolue**;
- **anomalie ≠ diagnostic**;
- **syndrome ≠ diagnostic ni cause unique**;
- **facteur de risque ≠ causalité démontrée**;
- **résultat de test ≠ diagnostic certain**;
- **sensibilité/spécificité ≠ valeurs prédictives**;
- **diagnostic ≠ certitude absolue**;
- **diagnostic ≠ indication automatique d’un traitement**;
- **intervention ≠ garantie de résultat**;
- **résultat observé après intervention ≠ preuve automatique que l’intervention l’a causé**;
- **rémission ≠ guérison définitive**;
- **échec thérapeutique ≠ effet indésirable**.

## Contenu

- 165 assertions atomiques;
- 90 référents;
- 19 sources institutionnelles, méthodologiques ou de consensus;
- index par sujet, prédicat, étape et thème;
- rapport de couverture et validation structurelle;
- schéma Kristal v6 embarqué.

## Frontière

Inclus : modèle clinique général, observation, anomalie, syndrome, diagnostic différentiel, probabilités et tests, incertitude, décision partagée, catégories générales d’intervention, suivi, résultats, fonctionnement et pronostic.

Exclus volontairement : catalogue de maladies, prescriptions, posologies, protocoles de procédures, algorithmes d’urgence/triage, recommandations pour un patient particulier, anatomie/physiologie détaillée (HumanBody) et opérations hospitalières (HospitalOps).

## Statut épistémique et sécurité

Le paquet est `reference` et les assertions sont `sourced`. Il s’agit d’un **corpus encyclopédique statique**, non d’un système de décision clinique. Les assertions portant sur une décision de soins sont marquées `human_decision` ou `human_review`; aucune autorité clinique humaine n’est revendiquée.

## Fichiers principaux

```text
knowledge-base/
  corpus/medicine.kristal-state.json
  corpus/referents.json
  corpus/index.json
  corpus/coverage-report.json
  corpus/validation-report.json
  sources/source-catalog.json
  sources/evidence-registry.json
  documentation/CONTENT_BOUNDARY.md
  documentation/CLINICAL_STATE_MODEL.md
  documentation/SEMANTIC_GUARDRAILS.md
  documentation/CLINICAL_SAFETY_BOUNDARY.md
  schemas/kristal-state.schema.json
  tools/validate.py
```
