# AI Context — Demography

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:demography`
- State Logical Commitment: `sha256:68ccf60bbd27d024864bb3f948126f9d3efd14d998a0d88b5e153cc5fd42f019`
- Workspace profile: `layered`
- Native model: `stock_flow_cohort_graph`
- Canonical artifacts: `5`
- Sources: `12`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et scope — Kristal-Demography

## Intention originale (extrait README)

# Kristal Demography v1.0.0

Corpus statique et validable sur population + temps : naissance, décès, migration, âge et cohorte.

- Assertions atomiques : 200
- Axes de couverture : 32
- Référents : 232
- Sources externes / synthèse : 12
- Langue éditoriale : français
- Schéma : Kristal v6

Le noyau distingue explicitement stocks, flux, comptes, taux, probabilités et proportions, et organise le temps selon âge × période × cohorte (Lexis). Les séries empiriques nationales et projections courantes sont volontairement exclues du corpus canonique : elles doivent rester des données versionnées.

## Normalisation 3.2.2

Enveloppe de construction locale sans modification des assertions v6 ni des snapshots v9 historiques. Statut local `validated`, sans nouvelle publication ni activation.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Demography

## Objet

stock de population → naissances / décès / migration ; âge × période × cohorte.

## Invariant

Stocks, flux, taux, probabilités, proportions et dimensions de Lexis restent distincts.

## Ownership

Le Kristal engage sa connaissance locale existante. Les références externes ont leur propre autorité et le Kristal ne possède ni les sources amont ni leur maintenance.

## Identité stable

`state_ref`: `urn:kristal:state:demography` ; `authority_ref`: `urn:kristal:authority:demography`.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-Demography

Type conservé : `stock_flow_cohort_graph`.

Orientation documentée : **stock de population → naissances / décès / migration ; âge × période × cohorte**.

Stocks, flux, taux, probabilités, proportions et dimensions de Lexis restent distincts.

Les assertions typées, identités, provenances et contraintes restent dans le payload v6 historique. Le contrat logique est `kristal_state/6.0`. Le contenu original des modèles est conservé sous `knowledge-base/` sans conversion sémantique.

## Référence historique

`knowledge-base/documentation/ARCHITECTURE.md`.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique — Kristal-Demography

Les assertions historiques sont conservées avec leurs données de provenance. Le catalogue original est `knowledge-base/sources/source_catalog.json`. La version normalisée est un index d’accès ; elle ne promeut pas un enregistrement externe en vérité universelle.

Un conflit ne se résout pas par écrasement silencieux ; une absence de valeur n’équivaut pas à `false`. Les résultats d’une IA future ne sont pas des assertions canoniques sans décision explicite.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé — Kristal-Demography

## Canon 3.2.2

`canon/domain/legacy-v6-state.payload.json` est un adaptateur lossless du payload du Logical Artifact historique `urn:kristal:demography:canonical-state`.

`canon/state.index.json` lie le contenu à son contrat, son scope, son authority_ref et au calcul `compute-json-jcs`.

## Legacy / matérialisation

Les répertoires `knowledge-base/` originaux ne sont ni écrasés ni désactivés. Le manifest d’origine `.kristal/v9/materialization-manifest.json` enregistre `kristal.materialization/native-blob/1` et les blobs immuables référencés. La couche 3.2.2 génère en plus `inline-json/1`; elle **ne remplace pas** le manifest d’origine, ni ne réclame une factorisation non construite.

Les projections historiques sous `knowledge-base/corpus/` et les index `.kristal/v8/` restent disponibles.
