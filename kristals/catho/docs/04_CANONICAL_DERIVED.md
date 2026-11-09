# Canonique et dérivé — Kristal-Catho

## Canon authoring 3.2.2

- `canon/state.index.json` décrit l'unique Logical Artifact hérité, dans son contrat exact.
- `canon/domain/legacy-logical-artifact.payload.json` est un input JSON canonique construit par copie logique du payload v9 antérieur et réengagé avec `compute-json-jcs`.
- `knowledge-base/sources/` conserve les sources métier natives non modifiées. Le corpus historique reste conservé comme référence et artefact de compatibilité, sans changement de sa signification ni de son autorité déclarée.

## Historique v9 préservé

Le manifest `.kristal/v9/materialization-manifest.json` est conservé, y compris le profil natif `native-blob/1` du Kristal Catho. Le blob est vérifié par son digest physique, mais le `build-v9` du Kit 3.2.2 reconstruit sa propre matérialisation `inline-json/1` et ne réutilise pas automatiquement ce manifest.

## Dérivé

`build/v9`, les caches v8, `state/`, `derived/`, `projections/materialized/`, `runtime/`, `release/` et toute couche `ai/` sont des sorties opératoires distinctes.

La factorisation v9 est **permise par le framework**, mais **n'est pas revendiquée** pour ce Kristal : aucun manifest factorisé n'était présent dans l'archive. La réduction des duplications futures doit être lossless et n'affecter aucun Logical Commitment.



## Enrichissement canonique du 13 octobre 2026

- Second canon : `canon/domain/personnes-reconnaissances.json` (commitment nouvellement calculé).
- Dérivé lisible : `knowledge-base/exports/personnes-tags.csv` (fiches + tags filtrables).
- Dérivés de consultation : `build/v9` et `ai/` éventuel ; jamais constitutifs du canon.
- Source métier originale `knowledge-base/sources/editorial/editorial.json` et payload historique `legacy-logical-artifact.payload.json` préservés à l'identique.
- Historique `.kristal/v9` préservé, ancien State Commitment non réutilisé comme celui de cette nouvelle édition.
