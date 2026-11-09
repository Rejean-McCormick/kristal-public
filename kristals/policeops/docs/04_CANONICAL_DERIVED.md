# Canonique et dérivé

## Source de vérité

Le seul Logical Artifact membre du State v9 courant est `knowledge-base/corpus/policeops.structured-epistemic-state.json`. Il reste byte-for-byte inchangé par cette normalisation.

`canon/state.index.json` est le registre d’authoring. Le commitment y est `precomputed` afin de préserver exactement le commitment PoliceOps v9 déjà vérifié; ce choix évite de recalculer naïvement sur les champs auto-référentiels du fichier natif.

## Entrées et soutien

`knowledge-base/sources/`, les schémas, profils et documents décrivent les inputs et politiques ayant servi au corpus. `sources/source-catalog.json` normalise les 29 `source_refs` sans les promouvoir en Logical Artifacts canoniques.

## Dérivés / runtime

- `.kristal/v8/` : projection portable v6, lexiques et indexes v8;
- `.kristal/v9/` : build/qualification v9 legacy;
- `build/` : candidats construits avec le Local Kit 3.2.2;
- `validation/` : preuves de validation;
- `knowledge-base/runtime/` : baseline/matérialisation opérationnelle;
- `external-source-library/` : matérialisation/index de sources;
- `source-manager/` : outillage d’acquisition/résolution.

## Matérialisation

Un changement de bytes physiques d’une représentation de source, d’un index ou d’un packing ne doit pas modifier le Logical Commitment du corpus canonique.
