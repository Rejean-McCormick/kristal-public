# AI Context — Textiles

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:textiles`
- State Logical Commitment: `sha256:c0435fd0259ff4ef21c92a7f92a6e64afae8ec1fed3dcde12e66f2ca8a44f095`
- Workspace profile: `layered`
- Native model: `textile_transformation_property_graph`
- Canonical artifacts: `13`
- Sources: `14`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et périmètre — Kristal-Textiles

Fibre → fil → structure textile → traitement → propriété → produit.

Cette migration met à disposition un workspace Local 3.2.2 compatible State v9 sans réécriture des assertions, ni changement de leur engagement logique. Elle ajoute une matérialisation factorisée, entièrement dérivée et réversible.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique

Propriété : Fibre → fil → structure textile → traitement → propriété → produit.

Invariant métier préservé : Les propriétés dépendent de la composition, de la structure et de l’usage ; éviter de transformer le parcours de navigation en causalité absolue.

L’autorité des références externes reste celle des artefacts historiques ; aucun ownership des données externes ni des autres Kristals n’est créé.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif

Kind : `textile_transformation_property_graph`

Fibre → fil → structure textile → traitement → propriété → produit.

Invariant : Les propriétés dépendent de la composition, de la structure et de l’usage ; éviter de transformer le parcours de navigation en causalité absolue.

La forme logique engagée reste un artifact v9 avec le contrat `kristal_state/6.0` et le payload d’assertions d’origine. Ne pas confondre lecture, compression et ontologie.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Épistémologie, autorité et provenance

Les valeurs `assertion_status`, `evidence_refs`, `provenance_refs`, `valuations`, `applicability`, et autres qualificatifs existants sont conservés lorsqu’ils sont présents. Le nouveau catalogue `sources/source-catalog.json` est une vue du catalogue historique `knowledge-base/sources/source-catalog.json`. Une source référencée ne doit pas être automatiquement promue à vérité générale.

Les conflits, inconnus et restrictions d’applicabilité ne sont ni supprimés ni fusionnés.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique versus dérivé

Entrée canonique de build 3.2.2 : `canon/domain/kristal-textiles.canonical-payload.json`. Les sources métier historiques restent sous `knowledge-base/sources`. Le fichier `.kristal/v9` historique n’est pas réécrit.

`materializations/v9/factorized/` est une représentation physique réversible avec dictionnaire des clés et valeurs communes. `knowledge-base/corpus`, `build/v9`, `runtime` et les indices hérités sont des read models et/ou matérialisations, pas de nouvelles autorités.

Logical Commitment attendu : `sha256:e9934a06bcd24c36e1dc5c6457e5a5e543875aa2c8fee8707d0bdd91eba184a6`. Changer compression ou emplacement ne doit pas le modifier.
