# Validation du domaine et lifecycle

## Invariants structurels et référentiels

Le validateur historique `knowledge-base/tools/validate.py` contrôle le schéma `structured_epistemic_state`, l'unicité des identifiants, les résolutions de référents, les valeurs contrôlées et cardinalités, l'acyclicité de `power:is_type_of`, les doublons de graphe, la bibliographie, la cohérence index/corpus, le `state_id`, le `content_hash`, le rebuild déterministe et le manifeste SHA-256.

Il contrôle aussi la couverture Power Dynamics, les hashes des documents sources, les `pd_source_ids`, les schémas natifs et les relations entre profils dynamiques et référents.

## Invariants épistémiques

Un candidat documentaire externe n'est pas une preuve. Les sources et reconstructions conservent leur statut et leur attribution. Les classifications contextuelles ne deviennent pas primaires, et les claims internes au framework restent internes sauf corroboration externe explicitement qualifiée.

## Logical Commitments

Le contrat canonique utilise `kristal.logical/jcs-sha256-v1`; l'état utilise `kristal.state-commitment/jcs-sha256-v1`. Le `build-v9` Local doit reproduire le commitment logique du v9 historique lorsque le payload, le scope et le contrat sont identiques.

## Critères locaux

Avant publication :

1. `python knowledge-base/tools/validate.py` doit réussir ;
2. `python tools/kristal.py check .` doit réussir ;
3. `python tools/kristal.py build-v9 .` doit réussir ;
4. le commitment du candidat doit correspondre à la sémantique attendue ;
5. une qualification indépendante doit précéder toute publication.

Le `check` Local établit une cohérence structurelle, pas la vérité sémantique universelle.
