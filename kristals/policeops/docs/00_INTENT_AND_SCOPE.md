# Intention et scope

## Pourquoi ce Kristal existe

PoliceOps conserve une mémoire sémantique et épistémique structurée pour le domaine police/judiciaire Québec–Lévis : terminologie, ressources cataloguées, voies et transitions judiciaires modélisées, relations/invariants, provenance et règles de lecture.

## Corpus de départ

Le canon préexistant est un `structured_epistemic_state/5.0` comprenant 538 assertions et 29 `source_refs`. La normalisation Local 3.2.2 n’en modifie pas les bytes ni la sémantique.

## Résultats attendus

- rendre le Kristal inspectable et buildable avec le Local Kit 3.2.2;
- conserver la forme native v5 et ses identités;
- séparer explicitement canon, projections, matérialisation de sources, build et publication;
- maintenir les limites d’autorité déjà déclarées;
- ne pas présenter le corpus de travail comme une validation juridique ou institutionnelle.

## Lacunes conservées

Le Source Store du snapshot est physiquement incomplet; certaines sources n’ont pas de canal d’autorité résolu; les transitions judiciaires sont encore à valider contre des sources juridiques versionnées.
