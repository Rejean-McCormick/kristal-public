# Canonique et dérivé

## Source(s) de vérité

La couche éditoriale autoritaire est `knowledge-base/sources/**`. Le build métier normalise ces sources en un modèle logique v9.

## Logical Artifacts canoniques

Le workspace 3.2.2 enregistre deux payloads state-bearing :

- `canon/domain/reference-model.json` → `vehiclediag.reference-model/3.0`;
- `canon/epistemic/epistemic-overlay.json` → `kristal_state.hash_target/6.0`.

Ces payloads ont été extraits du build v9 métier validé et doivent rester reproductibles depuis `knowledge-base/sources/**`.

## Artefacts dérivés / Runtime

`knowledge-base/corpus/**`, `.kristal/v8/**`, `.kristal/v9/**`, `build/**`, `runtime/**`, `derived/**` et les projections matérialisées sont reconstructibles.

## Materializations

Les graphes runtime, indexes, diagnostics de cas, portable v6 et anciens wrappers v9 sont des représentations physiques ou surfaces de lecture; leur existence ne change pas le Logical Commitment.

## Recettes de reconstruction

Depuis `knowledge-base/` : `python tools/build.py`, `python tools/build_v9.py`, `python tools/validate_v9.py`. Ensuite, depuis le kit 3.2.2 : `python tools/kristal.py check <workspace>` puis `python tools/kristal.py build-v9 <workspace>`.
