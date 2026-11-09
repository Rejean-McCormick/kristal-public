# AI Context — ScolQc — Éducation Québec

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:education-quebec`
- State Logical Commitment: `sha256:76020a229f3db812d3b10c3f51ebc56818281966bd0dd93c562003e0541a71b9`
- Workspace profile: `education-quebec/local-kristal-3.2.2`
- Native model: `temporal-jurisdictional-education-rule-transition-curriculum-admission-source-governance-graph`
- Canonical artifacts: `4`
- Sources: `122`
- External pinned references: `0`
- Materialization manifests: `4`
- Workspace-local materialization blobs: `48`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et portée

Kristal-ScolQc représente des connaissances structurées sur le parcours scolaire et les règles éducatives du Québec. La release domaine conservée lors de cette normalisation est **1.4.0**.

Le Kristal couvre notamment les secteurs et ordres d'enseignement, cycles et années, parcours, sanctions, disciplines, règles atomiques, transitions conditionnelles, curriculum, progression, évaluation, admission collégiale et formation professionnelle, avec provenance et temporalité.

La normalisation 3.2.2 est **additive** : elle ne modifie pas les assertions éducatives ni les octets des ressources de domaine existantes. Elle ajoute l'enveloppe de workspace local, explicite les responsabilités, et promeut les quatre Logical Artifacts v9 déjà qualifiés dans une zone canonique dédiée.

La validation technique du Kristal ne constitue ni une validation ministérielle, ni une décision d'admission, ni une interprétation juridique ou institutionnelle.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique

## Le Kristal possède

- les assertions structurées du domaine éducatif et leur provenance;
- leur statut, certitude, typage, applicabilité et temporalité;
- les identités et relations `authority → document → edition → representation`;
- les règles atomiques, transitions, curriculum et sémantiques d'admission explicitement modélisées;
- la politique d'admission des sources et la couverture représentée.

## Le Kristal ne possède pas

- les octets PDF/HTML, captures et métadonnées HTTP du Source Store;
- les décisions réelles d'admission, classement, sanction, équivalence ou décisions pédagogiques/administratives;
- les conditions détaillées propres aux programmes universitaires institutionnels;
- une vérité institutionnelle implicite pour les zones non couvertes.

## Séparations obligatoires

`authority != document != edition != representation != local_snapshot`

`discovered_link != source_ref`

`page_index != implicit_child_source_set`

`transition != admission`

`curriculum != admission_rule`

`coverage_status != truth_status`

`technical_validation != institutional_recognition`

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif

Le modèle natif est un **graphe éducatif temporel et juridictionnel** combinant règles, transitions, curriculum, admission, provenance et gouvernance des sources.

Les types de domaine principaux restent ceux définis par le Kristal : `sector`, `education_order`, `cycle`, `grade`, `pathway`, `discipline`, `credential`, `atomic_rule` et `transition`.

La normalisation 3.2.2 ne les aplatie pas dans une ontologie générique. Les invariants historiques restent normatifs, notamment : ordre distinct du secteur, cycle distinct de l'année, parcours distinct de l'ordre, diplôme distinct du parcours, transition non équivalente à une admission, et document distinct de son édition et de sa représentation.

Le `structured_epistemic_state` v5 est conservé comme projection canonique historique du corpus. Les projections portables v6 et lectures v8 restent dérivées/reconstructibles.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique

La connaissance est contextualisée par provenance, autorité, statut, certitude, typage, juridiction et temporalité.

Une source officielle n'est pas une décision institutionnelle. Une édition observée à une date donnée n'est pas une vérité intemporelle. Une absence de couverture dans le Kristal n'implique pas que l'énoncé soit faux.

Le temps fait partie de la sémantique lorsque pertinent : `observed_on`, `school_year`, `effective_from`, `effective_to` et les statuts de publication future doivent rester distincts.

Les conflits ou variations entre éditions doivent être représentés par leurs contextes et provenances plutôt que résolus par écrasement silencieux.

Toute sortie IA éventuelle est une proposition de lecture ou d'édition; elle ne devient pas autorité ni canon sans validation explicite.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé

## Canon v9 du workspace 3.2.2

Les quatre Logical Artifacts qualifiés de la migration v9 sont conservés sous `canon/artifacts/` :

- `authoring-basis.logical-artifact.json`;
- `contract-basis.logical-artifact.json`;
- `canonical-state.logical-artifact.json`;
- `domain-state.logical-artifact.json`.

Ils sont byte-identiques à leurs homologues historiques sous `.kristal/v9/artifacts/` au moment de la normalisation. Leurs commitments préexistants sont enregistrés dans `canon/state.index.json` pour préserver l'identité v9.

Les ressources qu'ils pinent restent à leurs chemins historiques stables sous `knowledge-base/edition/`, `knowledge-base/sources/`, `knowledge-base/integration/`, `knowledge-base/profiles/`, `knowledge-base/schemas/` et `knowledge-base/corpus/`.

## Dérivé ou opérationnel

- `.kristal/v8/` : portable state, lexiques et index de lecture;
- `.kristal/v9/` : ancienne enveloppe de migration/materialisation/activation conservée pour provenance;
- `build/`, `release/`, `state/`, `runtime/`, `derived/`, `projections/materialized/`, `validation/`;
- `external-source-library/` : état opérationnel du Source Store;
- `source-manager/` : outil opérationnel de capture/résolution.

Un artefact dérivé ne devient pas canon du seul fait qu'il est matérialisé sur disque.
