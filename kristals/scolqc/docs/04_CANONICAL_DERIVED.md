# Canonique et dérivé

## Canon v9 du workspace 3.2.2

Les quatre Logical Artifacts qualifiés de la migration v9 sont conservés sous `canon/artifacts/` :

- `authoring-basis.logical-artifact.json`;
- `contract-basis.logical-artifact.json`;
- `canonical-state.logical-artifact.json`;
- `domain-state.logical-artifact.json`.

Ils sont byte-identiques à leurs homologues historiques sous `.kristal/v9/artifacts/` au moment de la normalisation. Leurs commitments préexistants sont enregistrés dans `canon/state.index.json` pour préserver l'identité v9.

Les ressources qu'ils pinent restent à leurs chemins historiques stables sous `knowledge-base/edition/`, `knowledge-base/sources/`, `knowledge-base/integration/`, `knowledge-base/profiles/`, `knowledge-base/schemas/` et `knowledge-base/corpus/`.

## Dérivé ou opérationnel

- `.kristal/v8/` : portable state, lexiques et index de lecture;
- `.kristal/v9/` : ancienne enveloppe de migration/materialisation/activation conservée pour provenance;
- `build/`, `release/`, `state/`, `runtime/`, `derived/`, `projections/materialized/`, `validation/`;
- `external-source-library/` : état opérationnel du Source Store;
- `source-manager/` : outil opérationnel de capture/résolution.

Un artefact dérivé ne devient pas canon du seul fait qu'il est matérialisé sur disque.
