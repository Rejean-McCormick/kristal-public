# Canonique, matérialisations et dérivés — Kristal-EngineeringConstraints

## Canon authoring v3.2.2

- `canon/domain/portable-epistemic-state.payload.json` : payload original du Logical Artifact v9.
- `canon/state.index.json` : identité et contrat du même artefact.
- `knowledge-base/sources/` : données/source policies historiques conservées.

## Materializations physiques existantes

- `.kristal/v9/materialization-manifest.json` : profil `kristal.materialization/kristal-state-v6/1`.
- `knowledge-base/corpus/engineeringconstraints.kristal-state.json` : représentation v6 physique historisée, avec ses champs de métadonnées d'enveloppe.
- `build/v9/materializations/` : représentation inline JSON du kit ET enregistrement du manifest v6 existant.

La relation entre le JSON v6 et le payload logique est vérifiée par projection exacte des clés du payload ; les seuls champs physiques supplémentaires admis sont `state_id`, `content_hash` et `signatures`.

Les indexes v8, snapshots legacy, caches de lecture et projections sous `knowledge-base/corpus/` et `.kristal/` ne sont pas reconnus comme une nouvelle autorité logique par la normalisation.

**Aucun nouveau profil factorisé n'est inventé** pour ce petit corpus : le framework v9 autorise des alternatives sans imposer factorization ni segmentation.
