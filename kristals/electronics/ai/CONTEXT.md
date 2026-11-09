# AI Context — Electronics

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:kristal-electronics`
- State Logical Commitment: `sha256:a27f48934b79771b6f5dbd9a6c383b39e9587bb6b3f787bc5973660f11f4e059`
- Workspace profile: `layered`
- Native model: `electronics_component_relation_model`
- Canonical artifacts: `1`
- Sources: `13`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et portée — Kristal-Electronics

Ce Kristal conserve la connaissance originale associée à **Electronics**, sous sa forme native : **component / circuit / function / signal transformation graph**.

Le profil historique donne comme axe principal : **component → circuit → function → signal**.

Cette mise à jour ajoute une enveloppe `kristal.local-workspace/3.2.0` sans modification des assertions. Le Snapshot v9 et les commitments préexistants doivent être reconstruits à l'identique.

Les modèles/recettes/données sous `knowledge-base/` et les manifests sous `.kristal/` sont conservés tels quels pour les consommateurs historiques.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Electronics

**Territoire propre** : component / circuit / function / signal transformation graph.

**Orientation primaire fournie par le domaine** : component → circuit → function → signal.

Les observations enregistrées ne constituent pas une autorité universelle sur des sources externes. Le Kristal possède ses assertions et distinctions internes, pas le cycle éditorial des documents externes, ni les états/runtime d'autres Kristals.

`state_ref` historique : `urn:kristal:state:kristal-electronics`. Aucune référence extérieure n'est ajoutée à la migration.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-Electronics

Le modèle déclaré par `.kristal/v9/domain-profile.json` est : **component / circuit / function / signal transformation graph**.

Axe canonique historique : `component → circuit → function → signal`.

## Distinctions à préserver

- physical component
- circuit topology
- obtained function
- observed signal

## Supports locaux du modèle

- `knowledge-base/corpus/electronic-pathways.json`
- `knowledge-base/corpus/navigation.json`
- `knowledge-base/corpus/boundaries.json`
- `knowledge-base/corpus/invariants.json`

L'unique artefact logique v9 importé possède le contrat `kristal.portable-epistemic-state/6.0` et porte le payload du portable state v6 original. La nouvelle structure n'aplatit pas les primitives du domaine.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique — Kristal-Electronics

Le payload historique contient `359` assertions, leurs champs de provenance et leurs éventuelles références aux sources.

La provenance, les assertions, et les politiques de lecture ont été conservées exactement dans `canon/domain/portable-epistemic-state.payload.json`. Les originaux sous `knowledge-base/sources/` et `external-source-library/` demeurent inchangés.

La nouvelle liste `sources/source-catalog.json` indexe la provenance disponible, mais n'élève pas les sources à une autorité nouvelle. Les contradictions et les inconnues ne sont pas arbitrairement résolues. Toute future sortie IA reste une proposition.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique, matérialisations et dérivés — Kristal-Electronics

## Canon authoring v3.2.2

- `canon/domain/portable-epistemic-state.payload.json` : payload original du Logical Artifact v9.
- `canon/state.index.json` : identité et contrat du même artefact.
- `knowledge-base/sources/` : données/source policies historiques conservées.

## Materializations physiques existantes

- `.kristal/v9/materialization-manifest.json` : profil `kristal.materialization/kristal-state-v6/1`.
- `knowledge-base/corpus/electronics.kristal-state.json` : représentation v6 physique historisée, avec ses champs de métadonnées d'enveloppe.
- `build/v9/materializations/` : représentation inline JSON du kit ET enregistrement du manifest v6 existant.

La relation entre le JSON v6 et le payload logique est vérifiée par projection exacte des clés du payload ; les seuls champs physiques supplémentaires admis sont `state_id`, `content_hash` et `signatures`.

Les indexes v8, snapshots legacy, caches de lecture et projections sous `knowledge-base/corpus/` et `.kristal/` ne sont pas reconnus comme une nouvelle autorité logique par la normalisation.

**Aucun nouveau profil factorisé n'est inventé** pour ce petit corpus : le framework v9 autorise des alternatives sans imposer factorization ni segmentation.
