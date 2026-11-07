# AI Context — Zoology

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:kristal-zoology`
- State Logical Commitment: `sha256:8d01ff8e0e9574125559dc7f348a5278a81776bb8344c4d4790b4e6df3517a22`
- Workspace profile: `layered`
- Native model: `lineage_dag_body_plan_adaptation_graph`
- Canonical artifacts: `12`
- Sources: `6`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et portée — Kristal-Zoology

## Intention d’origine (README)

# Kristal-Zoology v1.0.0

**Plans corporels + lignées + adaptations**

Corpus statique et reconstruisible décrivant la diversité animale sur trois axes complémentaires :

`lignée ↔ plan corporel ↔ adaptation`

avec des taxons exemplaires, contextes d'habitat, convergences et incertitudes explicites.

## Portée de la migration

Ajouter le workspace 3.2.2 sans refonte métier, changement de forme native ni modification des commitments existants. Statut du workspace : `validated`.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Zoology

Le modèle décrit : **lignée ↔ plan corporel ↔ adaptation ; convergence et incertitude**.

## Invariant

Fonction similaire ≠ homologie ; convergence ≠ origine commune ; incertitude ≠ négation ; la lignée forme un DAG éditorial.

## Ownership

La vérité propre du Kristal est la connaissance locale engagée et qualifiée par les sources existantes. Le Kristal ne possède pas les sources externes ou leur politique de publication.

## Identité

State ref : `urn:kristal:state:kristal-zoology`. Authority ref : `non spécifiée`.

Le v9 historique possède un `logical-artifact.json` issu du contrat `kristal.portable-epistemic-state/6.0`, sans `state.scope` ni `authority_ref` ; cette absence est maintenue pour préserver le State Commitment. Le `domain-profile.json` historique est conservé.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-Zoology

Forme native identifiée : `lineage_dag_body_plan_adaptation_graph`.

Axes métier : **lignée ↔ plan corporel ↔ adaptation ; convergence et incertitude**.

Fonction similaire ≠ homologie ; convergence ≠ origine commune ; incertitude ≠ négation ; la lignée forme un DAG éditorial.

Contrat historique conservé : `kristal.portable-epistemic-state/6.0`.

Référence d’origine : `knowledge-base/documentation/DOMAIN_MODEL.md`.

Les assertions, données de contexte, et registres métier restent dans `knowledge-base/` ; aucun graphe n’a été aplati ou remplacé.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique — Kristal-Zoology

Les assertions d’origine restent engagées, sans adjudication nouvelle. Catalogue d’origine : `knowledge-base/sources/source_catalog.json`.

**Une référence n’est pas automatiquement une autorité universelle.** Les divergences, qualifications, incertitudes et inconnus explicitement représentés doivent rester distincts.

Une IA future ne peut que proposer des évolutions à valider.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique, dérivé, matérialisation — Kristal-Zoology

## Adaptateur 3.2.2

`canon/domain/legacy-v6-state.payload.json` est le payload logique exact du v9 historique. `canon/state.index.json` l’engage sous le contrat existant via `compute-json-jcs`.

## Emplacements historiques conservés

- `knowledge-base/` : sources et fichiers historiques de vérité v6 selon l’autorité indiquée par le README original, autres vues reconstruites.
- `.kristal/v8/` : index et projections antérieurs.
- `.kristal/v9/` : artefact et manifestes v9 originaux.

La matérialisation historique `kristal.materialization/kristal-state-v6/1` est préservée sans substitution ; le builder 3.2.2 produit également `inline-json/1`. La compression/factorisation n’est **pas** annoncée si inexistante.
