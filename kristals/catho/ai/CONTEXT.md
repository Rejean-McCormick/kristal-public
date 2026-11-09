# AI Context — Catho

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:catho`
- State Logical Commitment: `sha256:f0769f86b8bb05ae41d7380094c9ebdfabb6fabdce6cde598f6f9abb7ea51718`
- Workspace profile: `layered`
- Native model: `doctrinal_semantic_corpus_with_provenance`
- Canonical artifacts: `6`
- Sources: `145`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et scope — Kristal-Catho

Ce workspace apporte une enveloppe **Local Kristal 3.2.2** au corpus historique doté d’un état v9 sans modification éditoriale ni refonte sémantique.

## Forme et sujet déjà établis

corpus sémantique chrétien / catholique et documentation des positions, références, dossiers et registres de preuve.

Lire le `README.md` historique pour la description complète du corpus. `state_ref`: `urn:kristal:state:catho`.

## Portée de cette mise à jour

- Préserver les données sources et anciens fichiers v8/v9.
- Conserver le Logical Commitment et le State Commitment historiques.
- Ajouter un input canonique v9 recalculable, le catalogue de navigation des sources, les protocoles et le build.
- Ne pas prétendre à une qualification métier indépendante, ni à une publication v10.



## Extension 2026-10-13 — figures et reconnaissances

Le périmètre inclut désormais un registre distinct des personnes et distinctions, placé dans `canon/domain/personnes-reconnaissances.json`. Il comprend l'ensemble des entrées de pontificat publiées par le Saint-Siège, les 38 docteurs de l'Église et les trois répertoires institutionnels explicitement sélectionnés (Commission théologique internationale, Académie pontificale de Saint-Thomas-d'Aquin, prix Ratzinger). Aucun jugement implicite de catholicité n'est tiré d'une simple appartenance ou distinction.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Catho

## Possession logique

Ce Kristal possède les assertions statiques et identités de son corpus de référence dans le domaine `culture` et les règles d'interprétation associées.

Géométrie native déclarée : corpus sémantique chrétien / catholique et documentation des positions, références, dossiers et registres de preuve.

## Ce qui n'est pas possédé ou garanti

La stratégie de projet et les supports de communication ne sont pas une autorité doctrinale ni un engagement logique autonome.

Les sources amont et leur autorité éditoriale ne sont pas contrôlées par cet état local ; la présence d'une assertion ne la transforme pas en vérité universelle.

## Documents historiques de frontière / architecture

- `knowledge-base/documentation/audit-fiabilite.md`
- `knowledge-base/documentation/couverture-et-sources.md`
- `knowledge-base/documentation/dossiers-doctrinaux.md`
- `knowledge-base/documentation/dossiers-philosophiques.md`
- `knowledge-base/documentation/dossiers.md`
- `knowledge-base/documentation/inventaire.md`
- `knowledge-base/documentation/positions.md`
- `knowledge-base/documentation/reseau-idees-auteurs.md`
- `knowledge-base/documentation/vocabulaire.md`

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-Catho

**Kind local** : `doctrinal_semantic_corpus_with_provenance`.

**Géométrie conservée** : corpus sémantique chrétien / catholique et documentation des positions, références, dossiers et registres de preuve.

**Invariant essentiel** : les positions et attestations dépendent de leur tradition, source et degré de reconnaissance ; ne pas assimiler stratégie de diffusion et canon doctrinal.

Le contrat engagé par le v9 historique reste `kristal.catho.semantic-corpus/1.0`. Ce contrat utilise le payload d'origine engagé dans v9 (corpus sémantique natif pour Catho ; `kristal_state` v6 pour les autres), avec les informations de provenance existantes. Cette migration ne convertit pas ce graphe en ontologie uniforme, en table ou en pipeline artificiel.

La vue authoring `canon/domain/legacy-logical-artifact.payload.json` est une photographie canonique du payload existant. Les fichiers du domaine dans `knowledge-base` restent inchangés. Le maintien en synchronisation future de ces deux sources exige une procédure éditoriale explicite.



## Contrat complémentaire — personnes et reconnaissances

Un second Logical Artifact enregistré sous `urn:kristal:catho:artifact:personnes-reconnaissances` implémente `kristal.catho.personnes-reconnaissances/1.0`. Son modèle est **relationnel à catégories multiples** (`personne` ← `reconnaissance` → `source`) : une personne peut être pape, docteur, membre de la CTI, académicien et lauréat du prix. Chaque lien de reconnaissance conserve sa provenance et, si disponible, son mandat, année, section et numéro de pontificat. Il n'altère pas le payload historique.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique — Kristal-Catho

## Preuves et sources

La bibliographie / provenance historique est accessible dans `.kristal/v9/logical-artifact.json#payload.source_refs`. Sa vue normalisée est `sources/source-catalog.json` (138 entrées). Les métadonnées complètes et politiques historiques demeurent dans le fichier d'origine ou dans le payload engagé.

## Interprétation

Une source, une assertion, un auteur et un engagement logique ont des fonctions distinctes : provenance ≠ autorité ≠ vérité. Un désaccord ne doit pas être résolu sans justifier l'autorité. `unknown` ≠ `false`.

Invariant disciplinaire : les positions et attestations dépendent de leur tradition, source et degré de reconnaissance ; ne pas assimiler stratégie de diffusion et canon doctrinal.

Une réponse d'IA reste une proposition. Un index de requête ou une projection peut montrer une information sans devenir une source d'autorité.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé — Kristal-Catho

## Canon authoring 3.2.2

- `canon/state.index.json` décrit l'unique Logical Artifact hérité, dans son contrat exact.
- `canon/domain/legacy-logical-artifact.payload.json` est un input JSON canonique construit par copie logique du payload v9 antérieur et réengagé avec `compute-json-jcs`.
- `knowledge-base/sources/` conserve les sources métier natives non modifiées. Le corpus historique reste conservé comme référence et artefact de compatibilité, sans changement de sa signification ni de son autorité déclarée.

## Historique v9 préservé

Le manifest `.kristal/v9/materialization-manifest.json` est conservé, y compris le profil natif `native-blob/1` du Kristal Catho. Le blob est vérifié par son digest physique, mais le `build-v9` du Kit 3.2.2 reconstruit sa propre matérialisation `inline-json/1` et ne réutilise pas automatiquement ce manifest.

## Dérivé

`build/v9`, les caches v8, `state/`, `derived/`, `projections/materialized/`, `runtime/`, `release/` et toute couche `ai/` sont des sorties opératoires distinctes.

La factorisation v9 est **permise par le framework**, mais **n'est pas revendiquée** pour ce Kristal : aucun manifest factorisé n'était présent dans l'archive. La réduction des duplications futures doit être lossless et n'affecter aucun Logical Commitment.



## Enrichissement canonique du 13 octobre 2026

- Second canon : `canon/domain/personnes-reconnaissances.json` (commitment nouvellement calculé).
- Dérivé lisible : `knowledge-base/exports/personnes-tags.csv` (fiches + tags filtrables).
- Dérivés de consultation : `build/v9` et `ai/` éventuel ; jamais constitutifs du canon.
- Source métier originale `knowledge-base/sources/editorial/editorial.json` et payload historique `legacy-logical-artifact.payload.json` préservés à l'identique.
- Historique `.kristal/v9` préservé, ancien State Commitment non réutilisé comme celui de cette nouvelle édition.
