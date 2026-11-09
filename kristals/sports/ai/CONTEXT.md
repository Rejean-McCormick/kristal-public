# AI Context — Sports

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:sports`
- State Logical Commitment: `sha256:9ad70993a86cd7f2f17f7d44cb8a79c1c7c9bdcacfeeac8e644bc57b15bf3750`
- Workspace profile: `layered`
- Native model: `typed_sport_rules_competition_graph`
- Canonical artifacts: `12`
- Sources: `11`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et portée — Kristal-Sports

## Intention d’origine (README)

# Kristal-Sports v1.0.0

**Domaine :** sports — règle → participant → action → événement → score/résultat → compétition  
**Statut :** `working`  
**Snapshot éditorial :** 2026-10-02  
**Langue principale :** français

## Portée de la migration

Ajouter le workspace 3.2.2 sans refonte métier, changement de forme native ni modification des commitments existants. Statut du workspace : `building`.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Sports

Le modèle décrit : **règle → participant → action → événement → résultat → compétition**.

## Invariant

Cet axe est un ordre de lecture, pas une chronologie ; action ≠ événement arbitré ≠ résultat agrégé.

## Ownership

La vérité propre du Kristal est la connaissance locale engagée et qualifiée par les sources existantes. Le Kristal ne possède pas les sources externes ou leur politique de publication.

## Identité

State ref : `urn:kristal:state:sports`. Authority ref : `urn:kristal:authority:sports`.

Le v9 historique possède un `canonical.logical-artifact.json` et un champ `state.scope` ; ils sont conservés.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-Sports

Forme native identifiée : `typed_sport_rules_competition_graph`.

Axes métier : **règle → participant → action → événement → résultat → compétition**.

Cet axe est un ordre de lecture, pas une chronologie ; action ≠ événement arbitré ≠ résultat agrégé.

Contrat historique conservé : `kristal_state/6.0`.

Référence d’origine : `knowledge-base/documentation/DOMAIN_MODEL.md`.

Les assertions, données de contexte, et registres métier restent dans `knowledge-base/` ; aucun graphe n’a été aplati ou remplacé.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique — Kristal-Sports

Les assertions d’origine restent engagées, sans adjudication nouvelle. Catalogue d’origine : `knowledge-base/sources/source_catalog.json`.

**Une référence n’est pas automatiquement une autorité universelle.** Les divergences, qualifications, incertitudes et inconnus explicitement représentés doivent rester distincts.

Une IA future ne peut que proposer des évolutions à valider.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique, dérivé, matérialisation — Kristal-Sports

## Adaptateur 3.2.2

`canon/domain/legacy-v6-state.payload.json` est le payload logique exact du v9 historique. `canon/state.index.json` l’engage sous le contrat existant via `compute-json-jcs`.

## Emplacements historiques conservés

- `knowledge-base/` : sources et fichiers historiques de vérité v6 selon l’autorité indiquée par le README original, autres vues reconstruites.
- `.kristal/v8/` : index et projections antérieurs.
- `.kristal/v9/` : artefact et manifestes v9 originaux.

La matérialisation historique `kristal.materialization/native-blob/1` est préservée sans substitution ; le builder 3.2.2 produit également `inline-json/1`. La compression/factorisation n’est **pas** annoncée si inexistante.
