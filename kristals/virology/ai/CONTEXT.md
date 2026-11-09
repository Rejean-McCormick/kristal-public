# AI Context — Virology

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:kristal-virology`
- State Logical Commitment: `sha256:f19ab9812d60d79ab76d1b4bc65a066261a05cbc399db365cbe95f54008f97c2`
- Workspace profile: `layered`
- Native model: `multiplane_viral_process_graph`
- Canonical artifacts: `10`
- Sources: `16`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et périmètre — Kristal-Virology

Génome/particule, cycle intracellulaire, transmission interhôtes et stratégie Baltimore.

Cette migration met à disposition un workspace Local 3.2.2 compatible State v9 sans réécriture des assertions, ni changement de leur engagement logique. Elle ajoute une matérialisation factorisée, entièrement dérivée et réversible.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique

Propriété : Génome/particule, cycle intracellulaire, transmission interhôtes et stratégie Baltimore.

Invariant métier préservé : Taxonomie ≠ classification Baltimore ; entrée cellulaire ≠ transmission interhôtes.

L’autorité des références externes reste celle des artefacts historiques ; aucun ownership des données externes ni des autres Kristals n’est créé.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif

Kind : `multiplane_viral_process_graph`

Génome/particule, cycle intracellulaire, transmission interhôtes et stratégie Baltimore.

Invariant : Taxonomie ≠ classification Baltimore ; entrée cellulaire ≠ transmission interhôtes.

La forme logique engagée reste un artifact v9 avec le contrat `kristal.portable-epistemic-state/6.0` et le payload d’assertions d’origine. Ne pas confondre lecture, compression et ontologie.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Épistémologie, autorité et provenance

Les valeurs `assertion_status`, `evidence_refs`, `provenance_refs`, `valuations`, `applicability`, et autres qualificatifs existants sont conservés lorsqu’ils sont présents. Le nouveau catalogue `sources/source-catalog.json` est une vue du catalogue historique `knowledge-base/sources/source_catalog.json`. Une source référencée ne doit pas être automatiquement promue à vérité générale.

Les conflits, inconnus et restrictions d’applicabilité ne sont ni supprimés ni fusionnés.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique versus dérivé

Entrée canonique de build 3.2.2 : `canon/domain/kristal-virology.canonical-payload.json`. Les sources métier historiques restent sous `knowledge-base/sources`. Le fichier `.kristal/v9` historique n’est pas réécrit.

`materializations/v9/factorized/` est une représentation physique réversible avec dictionnaire des clés et valeurs communes. `knowledge-base/corpus`, `build/v9`, `runtime` et les indices hérités sont des read models et/ou matérialisations, pas de nouvelles autorités.

Logical Commitment attendu : `sha256:3cc5eb9afa33f4380ceb97f731367f7fcafe86cd181198f7a747c8f5880f5725`. Changer compression ou emplacement ne doit pas le modifier.
