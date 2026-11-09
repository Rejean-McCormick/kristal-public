# AI Context — Design

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:design`
- State Logical Commitment: `sha256:45b1c8fa68e71451468b9bb2e30350d1570e0fcf81849f92a76218c6c3e5e8a2`
- Workspace profile: `layered`
- Native model: `iterative_design_relation_graph`
- Canonical artifacts: `1`
- Sources: `14`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et scope — Kristal-Design

## Intention originale (extrait README)

# Kristal-Design

**Kristal-Design 1.0.0** est un corpus statique Kristal v6 centré sur la chaîne :

**problème → utilisateur → contrainte → solution → prototype → évaluation**

La chaîne sert d’axe de navigation et non de processus linéaire obligatoire. L’évaluation peut ramener au prototype, à la solution, aux contraintes, à la compréhension des utilisateurs ou au cadrage du problème. Les interfaces et boucles d’itération sont donc des objets de premier rang.

Le corpus couvre design produit, interaction, service et information à un niveau transversal. Il sépare besoin, exigence, contrainte, critère de réussite et compromis; il définit un prototype par la question qu’il permet d’explorer plutôt que par sa fidélité maximale.

État canonique : `knowledge-base/corpus/design.kristal-state.json`

Validation : `python knowledge-base/tools/validate.py`

## Normalisation 3.2.2

Enveloppe de construction locale sans modification des assertions v6 ni des snapshots v9 historiques. Statut local `validated`, sans nouvelle publication ni activation.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Design

## Objet

problème → utilisateur → contrainte → solution → prototype → évaluation.

## Invariant

L’orientation est navigable et itérative, pas un processus linéaire obligatoire.

## Ownership

Le Kristal engage sa connaissance locale existante. Les références externes ont leur propre autorité et le Kristal ne possède ni les sources amont ni leur maintenance.

## Identité stable

`state_ref`: `urn:kristal:state:design` ; `authority_ref`: `urn:kristal:authority:design`.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-Design

Type conservé : `iterative_design_relation_graph`.

Orientation documentée : **problème → utilisateur → contrainte → solution → prototype → évaluation**.

L’orientation est navigable et itérative, pas un processus linéaire obligatoire.

Les assertions typées, identités, provenances et contraintes restent dans le payload v6 historique. Le contrat logique est `kristal_state/6.0`. Le contenu original des modèles est conservé sous `knowledge-base/` sans conversion sémantique.

## Référence historique

`knowledge-base/documentation/ARCHITECTURE.md`.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique — Kristal-Design

Les assertions historiques sont conservées avec leurs données de provenance. Le catalogue original est `knowledge-base/sources/source_catalog.json`. La version normalisée est un index d’accès ; elle ne promeut pas un enregistrement externe en vérité universelle.

Un conflit ne se résout pas par écrasement silencieux ; une absence de valeur n’équivaut pas à `false`. Les résultats d’une IA future ne sont pas des assertions canoniques sans décision explicite.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé — Kristal-Design

## Canon 3.2.2

`canon/domain/legacy-v6-state.payload.json` est un adaptateur lossless du payload du Logical Artifact historique `urn:kristal:design:canonical-state`.

`canon/state.index.json` lie le contenu à son contrat, son scope, son authority_ref et au calcul `compute-json-jcs`.

## Legacy / matérialisation

Les répertoires `knowledge-base/` originaux ne sont ni écrasés ni désactivés. Le manifest d’origine `.kristal/v9/materialization-manifest.json` enregistre `kristal.materialization/native-blob/1` et les blobs immuables référencés. La couche 3.2.2 génère en plus `inline-json/1`; elle **ne remplace pas** le manifest d’origine, ni ne réclame une factorisation non construite.

Les projections historiques sous `knowledge-base/corpus/` et les index `.kristal/v8/` restent disponibles.
