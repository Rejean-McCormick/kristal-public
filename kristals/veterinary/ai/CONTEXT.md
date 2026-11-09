# AI Context — Veterinary

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:kristal-veterinary`
- State Logical Commitment: `sha256:bf3c1c3b16a3a38e85177352a43c7e768cc4e6b02bed018af1402b5566ff3053`
- Workspace profile: `layered`
- Native model: `species_system_pathology_intervention_graph`
- Canonical artifacts: `13`
- Sources: `10`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et périmètre — Kristal-Veterinary

Espèce × système physiologique × pathologie × intervention, avec contexte et populations.

Cette migration met à disposition un workspace Local 3.2.2 compatible State v9 sans réécriture des assertions, ni changement de leur engagement logique. Elle ajoute une matérialisation factorisée, entièrement dérivée et réversible.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique

Propriété : Espèce × système physiologique × pathologie × intervention, avec contexte et populations.

Invariant métier préservé : Une relation représentative n’est pas un produit cartésien ; spécificité d’espèce ≠ affirmation universelle.

L’autorité des références externes reste celle des artefacts historiques ; aucun ownership des données externes ni des autres Kristals n’est créé.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif

Kind : `species_system_pathology_intervention_graph`

Espèce × système physiologique × pathologie × intervention, avec contexte et populations.

Invariant : Une relation représentative n’est pas un produit cartésien ; spécificité d’espèce ≠ affirmation universelle.

La forme logique engagée reste un artifact v9 avec le contrat `kristal.portable-epistemic-state/6.0` et le payload d’assertions d’origine. Ne pas confondre lecture, compression et ontologie.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Épistémologie, autorité et provenance

Les valeurs `assertion_status`, `evidence_refs`, `provenance_refs`, `valuations`, `applicability`, et autres qualificatifs existants sont conservés lorsqu’ils sont présents. Le nouveau catalogue `sources/source-catalog.json` est une vue du catalogue historique `knowledge-base/sources/source_catalog.json`. Une source référencée ne doit pas être automatiquement promue à vérité générale.

Les conflits, inconnus et restrictions d’applicabilité ne sont ni supprimés ni fusionnés.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique versus dérivé

Entrée canonique de build 3.2.2 : `canon/domain/kristal-veterinary.canonical-payload.json`. Les sources métier historiques restent sous `knowledge-base/sources`. Le fichier `.kristal/v9` historique n’est pas réécrit.

`materializations/v9/factorized/` est une représentation physique réversible avec dictionnaire des clés et valeurs communes. `knowledge-base/corpus`, `build/v9`, `runtime` et les indices hérités sont des read models et/ou matérialisations, pas de nouvelles autorités.

Logical Commitment attendu : `sha256:cd9c4412ab085003bac823908849f301a62720c8cffc4d10aa796cc971b4da09`. Changer compression ou emplacement ne doit pas le modifier.
