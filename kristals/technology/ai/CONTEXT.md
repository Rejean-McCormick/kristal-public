# AI Context — Technology

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:technology`
- State Logical Commitment: `sha256:9cd38c80303a2dd6f42435348ed94f35bf66355995f3276ce655f8a3548b3e17`
- Workspace profile: `layered`
- Native model: `typed_technical_function_chain_graph`
- Canonical artifacts: `13`
- Sources: `0`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et portée — Kristal-Technology

## Intention d’origine (README)

# Kristal-Technology v1.0.0

**Technology — fonction artificielle**

Chaîne canonique :

```text
besoin → fonction → principe → composant → système → usage → défaillance
```

Ce Kristal décrit la technologie à un niveau **générique et transversal**. Il répond à des questions comme :

- quel besoin une fonction technique satisfait-elle ?
- par quels principes une fonction peut-elle être réalisée ?
- quels composants incarnent ces principes ?
- dans quels systèmes ces composants s’intègrent-ils ?
- où ces systèmes sont-ils utilisés ?
- de quelles manières leur fonction peut-elle être perdue, dégradée ou détournée ?

Il n’est ni un catalogue de produits, ni un manuel OEM, ni un corpus de lois physiques. Les détails scientifiques profonds restent dans Physique/Chimie; les instances et procédures particulières restent dans les Kristals appliqués.

## Portée de la migration

Ajouter le workspace 3.2.2 sans refonte métier, changement de forme native ni modification des commitments existants. Statut du workspace : `validated`.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Technology

Le modèle décrit : **besoin → fonction → principe → composant → système → usage → défaillance**.

## Invariant

Fonction ≠ solution ; principe ≠ composant ; usage ≠ identité de système ; le modèle décrit des archétypes, pas des produits OEM.

## Ownership

La vérité propre du Kristal est la connaissance locale engagée et qualifiée par les sources existantes. Le Kristal ne possède pas les sources externes ou leur politique de publication.

## Identité

State ref : `urn:kristal:state:technology`. Authority ref : `urn:kristal:authority:technology`.

Le v9 historique possède un `canonical.logical-artifact.json` et un champ `state.scope` ; ils sont conservés.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-Technology

Forme native identifiée : `typed_technical_function_chain_graph`.

Axes métier : **besoin → fonction → principe → composant → système → usage → défaillance**.

Fonction ≠ solution ; principe ≠ composant ; usage ≠ identité de système ; le modèle décrit des archétypes, pas des produits OEM.

Contrat historique conservé : `kristal_state/6.0`.

Référence d’origine : `knowledge-base/documentation/DOMAIN_MODEL.md`.

Les assertions, données de contexte, et registres métier restent dans `knowledge-base/` ; aucun graphe n’a été aplati ou remplacé.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique — Kristal-Technology

Les assertions d’origine restent engagées, sans adjudication nouvelle. Catalogue d’origine : `aucun catalogue structuré identifié`.

**Une référence n’est pas automatiquement une autorité universelle.** Les divergences, qualifications, incertitudes et inconnus explicitement représentés doivent rester distincts.

Une IA future ne peut que proposer des évolutions à valider.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique, dérivé, matérialisation — Kristal-Technology

## Adaptateur 3.2.2

`canon/domain/legacy-v6-state.payload.json` est le payload logique exact du v9 historique. `canon/state.index.json` l’engage sous le contrat existant via `compute-json-jcs`.

## Emplacements historiques conservés

- `knowledge-base/` : sources et fichiers historiques de vérité v6 selon l’autorité indiquée par le README original, autres vues reconstruites.
- `.kristal/v8/` : index et projections antérieurs.
- `.kristal/v9/` : artefact et manifestes v9 originaux.

La matérialisation historique `kristal.materialization/native-blob/1` est préservée sans substitution ; le builder 3.2.2 produit également `inline-json/1`. La compression/factorisation n’est **pas** annoncée si inexistante.
