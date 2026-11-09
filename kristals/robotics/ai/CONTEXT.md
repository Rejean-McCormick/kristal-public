# AI Context — Robotics

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:robotics`
- State Logical Commitment: `sha256:31e7ed7434833bbd4a15aeb6371dd4571b822f5f607dae6c468733de92ac4d8b`
- Workspace profile: `layered`
- Native model: `perception_estimation_control_feedback_graph`
- Canonical artifacts: `1`
- Sources: `15`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et périmètre — Kristal-Robotics

Ce dépôt conserve son domaine et sa sémantique historique. L'enveloppe Local Kristal 3.2.2 est ajoutée sans modifier les fichiers préexistants.

**Forme :** Boucle de robotique perception, estimation d’état, planification/décision, actionnement et rétroaction.

**State v9 :** `urn:kristal:state:robotics` ; **scope initial :** `{"domain": "robotics", "subdomain": "perceive-estimate-decide-act-feedback", "language": "fr"}`.

Le contrat natif v9 déjà présent est `kristal.compat/v6-portable-state-logical-projection/1.0`, caractérisé ici comme projection de connaissance compatible v6 engagée logiquement en v9. Aucun reclassement du canon historique n'est imposé.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique

## Ownership positif

Référentiel des fonctions et relations des systèmes robotiques et de leurs boucles de commande.

## Ne possède pas

Pilotage effectif d’un robot ou décisions de contrôle en temps réel sans système de contrôle explicite. Le dépôt ne possède pas automatiquement ses sources externes et ne publie ni n'active de State v9 à l'occasion de cette normalisation.

## State et références

`urn:kristal:state:robotics` ; membres : 1 ; références externes pinées : 0. L’absence de références pinées n’implique pas absence de sources bibliographiques dans le catalogue.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif

`native_model.kind = perception_estimation_control_feedback_graph` (qualification descriptive de la forme existante, non conversion).

Boucle de robotique perception, estimation d’état, planification/décision, actionnement et rétroaction.

**Orientation principale :** perception → estimation → décision → action → rétroaction.

**Invariants :** Monde réel, mesure, état estimé, décision et action ne sont pas des identités interchangeables.

L'engagement v9 existant porte sur le payload logique à `canon/domain/v9-logical-payload.json`. Les relations et structures déjà déclarées dans le corpus historique demeurent la référence détaillée. Le seul changement de layout ne crée pas de nouveaux prédicats ni de nouveaux IDs.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Épistémologie et autorité

Le catalogue d’origine `knowledge-base/sources/source-catalog.json` est conservé, avec une concordance sous `sources/source-catalog.json`. Les notices y sont copiées dans `legacy_record` pour conserver les classes d'évidence/autorité explicites du corpus.

La provenance d'une source n'implique pas vérité automatique ou autorité d'édition. Une divergence ne doit pas être effacée silencieusement ; `unknown != false`. Les sorties d’IA éventuelles restent des propositions et non des faits canoniques.

**Règle métier :** Monde réel, mesure, état estimé, décision et action ne sont pas des identités interchangeables.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé

## Canon local 3.2.2

`canon/domain/v9-logical-payload.json` est une extraction à l’identique des données `payload` du Logical Artifact v9 préexistant, engagée en `compute-json-jcs` via `canon/state.index.json`.

Les fichiers sources historiques et leurs règles sémantiques ne sont ni supprimés ni modifiés. `build/v9`, `.kristal/v8`, les caches/index et les projections `knowledge-base/corpus` ne doivent pas devenir une nouvelle autorité par le fait d'être matérialisés.

## Matérialisations v9

La matérialisation historique `kristal.materialization/kristal-state-v6/1` est conservée sous `.kristal/v9/materialization.json`, avec 1 segment(s) identifié(s) par SHA-256. Le builder officiel 3.2.2 génère aussi sa représentation `inline-json/1`. Le workflow `tools/build_verified_v9.py` réenregistre ensuite le manifeste historique sous `build/v9/materializations/` **après validation des blobs et de leur lien au Logical Commitment**.

Le succès de la vérification physique n’équivaut pas à une preuve indépendante de toute la procédure de reconstruction lossless.
