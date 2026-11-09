# AI Context — Droit-International-Global

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:droit-international-global`
- State Logical Commitment: `sha256:84d79fa1357a31d282ae5aafd639f752d3183bb26a426bfd9b64c5de0f1759ad`
- Workspace profile: `layered`
- Native model: `normative_jurisdiction_relation_graph`
- Canonical artifacts: `1`
- Sources: `36`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et scope — Kristal-Droit-International-Global

## Intention originale (extrait README)

# Kristal — Droit international global

Version **0.1.0** — état des sources et participations au **2 octobre 2026**.

Ce Kristal couvre uniquement le **droit international public à portée mondiale ou très large**. Il exclut volontairement les lois nationales du Canada, du Québec et des autres pays.

## Normalisation 3.2.2

Enveloppe de construction locale sans modification des assertions v6 ni des snapshots v9 historiques. Statut local `validated`, sans nouvelle publication ni activation.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Droit-International-Global

## Objet

source normative → portée → force obligatoire → juridiction → exécution.

## Invariant

L’existence d’une norme ne prouve pas sa force obligatoire universelle ni son exécution ; exclut les lois nationales.

## Ownership

Le Kristal engage sa connaissance locale existante. Les références externes ont leur propre autorité et le Kristal ne possède ni les sources amont ni leur maintenance.

## Identité stable

`state_ref`: `urn:kristal:state:droit-international-global` ; `authority_ref`: `urn:kristal:authority:droit-international-global`.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-Droit-International-Global

Type conservé : `normative_jurisdiction_relation_graph`.

Orientation documentée : **source normative → portée → force obligatoire → juridiction → exécution**.

L’existence d’une norme ne prouve pas sa force obligatoire universelle ni son exécution ; exclut les lois nationales.

Les assertions typées, identités, provenances et contraintes restent dans le payload v6 historique. Le contrat logique est `kristal_state/6.0`. Le contenu original des modèles est conservé sous `knowledge-base/` sans conversion sémantique.

## Référence historique

`knowledge-base/documentation/DOMAIN_MODEL.md`.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique — Kristal-Droit-International-Global

Les assertions historiques sont conservées avec leurs données de provenance. Le catalogue original est `knowledge-base/sources/source_catalog.json`. La version normalisée est un index d’accès ; elle ne promeut pas un enregistrement externe en vérité universelle.

Un conflit ne se résout pas par écrasement silencieux ; une absence de valeur n’équivaut pas à `false`. Les résultats d’une IA future ne sont pas des assertions canoniques sans décision explicite.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé — Kristal-Droit-International-Global

## Canon 3.2.2

`canon/domain/legacy-v6-state.payload.json` est un adaptateur lossless du payload du Logical Artifact historique `urn:kristal:droit-international-global:canonical-state`.

`canon/state.index.json` lie le contenu à son contrat, son scope, son authority_ref et au calcul `compute-json-jcs`.

## Legacy / matérialisation

Les répertoires `knowledge-base/` originaux ne sont ni écrasés ni désactivés. Le manifest d’origine `.kristal/v9/materialization-manifest.json` enregistre `kristal.materialization/native-blob/1` et les blobs immuables référencés. La couche 3.2.2 génère en plus `inline-json/1`; elle **ne remplace pas** le manifest d’origine, ni ne réclame une factorisation non construite.

Les projections historiques sous `knowledge-base/corpus/` et les index `.kristal/v8/` restent disponibles.
