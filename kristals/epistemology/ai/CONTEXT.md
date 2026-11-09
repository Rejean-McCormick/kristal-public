# AI Context — Epistemology

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:kristal-epistemology`
- State Logical Commitment: `sha256:fb66ac9686855d6b2b4b551b279e36fe1ad7ddd2ce6d06ce6fa41b5243d37f2c`
- Workspace profile: `layered`
- Native model: `layered_epistemic_support_defeat_graph`
- Canonical artifacts: `9`
- Sources: `12`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et portée — Kristal-Epistemology

Ce Kristal conserve la connaissance originale associée à **Epistemology**, sous sa forme native : **layered epistemic support/defeat graph**.

Le profil historique donne comme axe principal : **proposition ← evidence ← source/provenance; reasons → justification → belief → possible knowledge**.

Cette mise à jour ajoute une enveloppe `kristal.local-workspace/3.2.0` sans modification des assertions. Le Snapshot v9 et les commitments préexistants doivent être reconstruits à l'identique.

Les modèles/recettes/données sous `knowledge-base/` et les manifests sous `.kristal/` sont conservés tels quels pour les consommateurs historiques.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Epistemology

**Territoire propre** : layered epistemic support/defeat graph.

**Orientation primaire fournie par le domaine** : proposition ← evidence ← source/provenance; reasons → justification → belief → possible knowledge.

Les observations enregistrées ne constituent pas une autorité universelle sur des sources externes. Le Kristal possède ses assertions et distinctions internes, pas le cycle éditorial des documents externes, ni les états/runtime d'autres Kristals.

`state_ref` historique : `urn:kristal:state:kristal-epistemology`. Aucune référence extérieure n'est ajoutée à la migration.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-Epistemology

Le modèle déclaré par `.kristal/v9/domain-profile.json` est : **layered epistemic support/defeat graph**.

Axe canonique historique : `proposition ← evidence ← source/provenance; reasons → justification → belief → possible knowledge`.

## Distinctions à préserver

- truth ≠ belief
- evidence ≠ source
- provenance ≠ reliability
- support ≠ implication
- justification ≠ truth

## Supports locaux du modèle

Aucun fichier de support listé explicitement dans le profil v9.

L'unique artefact logique v9 importé possède le contrat `kristal.portable-epistemic-state/6.0` et porte le payload du portable state v6 original. La nouvelle structure n'aplatit pas les primitives du domaine.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique — Kristal-Epistemology

Le payload historique contient `171` assertions, leurs champs de provenance et leurs éventuelles références aux sources.

La provenance, les assertions, et les politiques de lecture ont été conservées exactement dans `canon/domain/portable-epistemic-state.payload.json`. Les originaux sous `knowledge-base/sources/` et `external-source-library/` demeurent inchangés.

La nouvelle liste `sources/source-catalog.json` indexe la provenance disponible, mais n'élève pas les sources à une autorité nouvelle. Les contradictions et les inconnues ne sont pas arbitrairement résolues. Toute future sortie IA reste une proposition.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique, matérialisations et dérivés — Kristal-Epistemology

## Canon authoring v3.2.2

- `canon/domain/portable-epistemic-state.payload.json` : payload original du Logical Artifact v9.
- `canon/state.index.json` : identité et contrat du même artefact.
- `knowledge-base/sources/` : données/source policies historiques conservées.

## Materializations physiques existantes

- `.kristal/v9/materialization-manifest.json` : profil `kristal.materialization/kristal-state-v6/1`.
- `knowledge-base/corpus/epistemology.kristal-state.json` : représentation v6 physique historisée, avec ses champs de métadonnées d'enveloppe.
- `build/v9/materializations/` : représentation inline JSON du kit ET enregistrement du manifest v6 existant.

La relation entre le JSON v6 et le payload logique est vérifiée par projection exacte des clés du payload ; les seuls champs physiques supplémentaires admis sont `state_id`, `content_hash` et `signatures`.

Les indexes v8, snapshots legacy, caches de lecture et projections sous `knowledge-base/corpus/` et `.kristal/` ne sont pas reconnus comme une nouvelle autorité logique par la normalisation.

**Aucun nouveau profil factorisé n'est inventé** pour ce petit corpus : le framework v9 autorise des alternatives sans imposer factorization ni segmentation.
