# AI Context — Organizations

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:organizations`
- State Logical Commitment: `sha256:109c045d52d519e036c482e7089d6237e1da9f8ca859b5f7a5958a7b170898d9`
- Workspace profile: `layered`
- Native model: `feedback_organizational_process_graph`
- Canonical artifacts: `9`
- Sources: `18`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et périmètre — Kristal-Organizations

Ce dépôt conserve son domaine et sa sémantique historique. L'enveloppe Local Kristal 3.2.2 est ajoutée sans modifier les fichiers préexistants.

**Forme :** Graphe de coordination finalisée avec rôles, unités, décisions, processus, résultats et boucles de rétroaction.

**State v9 :** `urn:kristal:state:organizations` ; **scope initial :** `{"domain": "organizations", "subdomain": "general-organization-theory", "language": "fr"}`.

Le contrat natif v9 déjà présent est `kristal.compat/v6-portable-state-logical-projection/1.0`, caractérisé ici comme projection de connaissance compatible v6 engagée logiquement en v9. Aucun reclassement du canon historique n'est imposé.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique

## Ownership positif

Modèle de coordination organisationnelle, rôles, processus, décisions, résultats et leurs relations documentées.

## Ne possède pas

Gestion d’organisations réelles, décisions opérationnelles ou prétention à une causalité universelle. Le dépôt ne possède pas automatiquement ses sources externes et ne publie ni n'active de State v9 à l'occasion de cette normalisation.

## State et références

`urn:kristal:state:organizations` ; membres : 1 ; références externes pinées : 0. L’absence de références pinées n’implique pas absence de sources bibliographiques dans le catalogue.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif

`native_model.kind = feedback_organizational_process_graph` (qualification descriptive de la forme existante, non conversion).

Graphe de coordination finalisée avec rôles, unités, décisions, processus, résultats et boucles de rétroaction.

**Orientation principale :** objectif → rôle → unité → processus → décision → résultat (orientation, pas causalité universelle).

**Invariants :** Les boucles et rétroactions organisationnelles ne sont pas aplaties en une chaîne causale universelle.

L'engagement v9 existant porte sur le payload logique à `canon/domain/v9-logical-payload.json`. Les relations et structures déjà déclarées dans le corpus historique demeurent la référence détaillée. Le seul changement de layout ne crée pas de nouveaux prédicats ni de nouveaux IDs.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Épistémologie et autorité

Le catalogue d’origine `knowledge-base/sources/source-catalog.json` est conservé, avec une concordance sous `sources/source-catalog.json`. Les notices y sont copiées dans `legacy_record` pour conserver les classes d'évidence/autorité explicites du corpus.

La provenance d'une source n'implique pas vérité automatique ou autorité d'édition. Une divergence ne doit pas être effacée silencieusement ; `unknown != false`. Les sorties d’IA éventuelles restent des propositions et non des faits canoniques.

**Règle métier :** Les boucles et rétroactions organisationnelles ne sont pas aplaties en une chaîne causale universelle.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé

## Canon local 3.2.2

`canon/domain/v9-logical-payload.json` est une extraction à l’identique des données `payload` du Logical Artifact v9 préexistant, engagée en `compute-json-jcs` via `canon/state.index.json`.

Les fichiers sources historiques et leurs règles sémantiques ne sont ni supprimés ni modifiés. `build/v9`, `.kristal/v8`, les caches/index et les projections `knowledge-base/corpus` ne doivent pas devenir une nouvelle autorité par le fait d'être matérialisés.

## Matérialisations v9

La matérialisation historique `kristal.materialization/kristal-state-v6/1` est conservée sous `.kristal/v9/materialization.json`, avec 1 segment(s) identifié(s) par SHA-256. Le builder officiel 3.2.2 génère aussi sa représentation `inline-json/1`. Le workflow `tools/build_verified_v9.py` réenregistre ensuite le manifeste historique sous `build/v9/materializations/` **après validation des blobs et de leur lien au Logical Commitment**.

Le succès de la vérification physique n’équivaut pas à une preuve indépendante de toute la procédure de reconstruction lossless.
