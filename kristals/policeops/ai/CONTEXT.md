# AI Context — PoliceOps

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:policeops`
- State Logical Commitment: `sha256:46b7848a7c82b0a98f735fe993dcfab545d50f47ce44f1c8bc5ab2875f9f3ca1`
- Workspace profile: `layered`
- Native model: `structured_epistemic_state`
- Canonical artifacts: `1`
- Sources: `29`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et scope

## Pourquoi ce Kristal existe

PoliceOps conserve une mémoire sémantique et épistémique structurée pour le domaine police/judiciaire Québec–Lévis : terminologie, ressources cataloguées, voies et transitions judiciaires modélisées, relations/invariants, provenance et règles de lecture.

## Corpus de départ

Le canon préexistant est un `structured_epistemic_state/5.0` comprenant 538 assertions et 29 `source_refs`. La normalisation Local 3.2.2 n’en modifie pas les bytes ni la sémantique.

## Résultats attendus

- rendre le Kristal inspectable et buildable avec le Local Kit 3.2.2;
- conserver la forme native v5 et ses identités;
- séparer explicitement canon, projections, matérialisation de sources, build et publication;
- maintenir les limites d’autorité déjà déclarées;
- ne pas présenter le corpus de travail comme une validation juridique ou institutionnelle.

## Lacunes conservées

Le Source Store du snapshot est physiquement incomplet; certaines sources n’ont pas de canal d’autorité résolu; les transitions judiciaires sont encore à valider contre des sources juridiques versionnées.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique

## Subject / territoire

PoliceOps couvre un corpus épistémique police/judiciaire de conception pour le Canada / Québec / Ville de Lévis, en français.

## Possède

- les identités de sources et leur provenance PoliceOps;
- les assertions et relations du corpus, leurs statuts épistémiques, evidence refs et métadonnées de portée;
- les référents éditoriaux et modèles de voies/transitions judiciaires présents dans le corpus;
- les références aux reader policies propres à PoliceOps.

## Ne possède pas

- les bytes et statuts de téléchargement du Source Store externe;
- les Cases, Tasks, workflows et décisions en cours appartenant à Orgo;
- l’autorité des publications externes et les décisions des autorités judiciaires;
- une reconnaissance juridique globale des assertions.

## State identity v9

`state_ref`: `urn:kristal:state:policeops`  
`authority_ref`: `urn:kristal:authority-boundary:policeops:repository-canon`

Les publications externes du catalogue sont des **sources de provenance**. Elles ne sont pas importées comme `external_references` du State Snapshot v9 puisqu’aucun Logical Commitment v9 externe piné n’est fourni par le snapshot.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif

## Primitives du domaine

Le document natif combine `source_refs`, assertions, provenance, reader policies, portée/applicabilité, valuations épistémiques, relations et extensions métier.

Familles déclarées dans le corpus : 447 termes de glossaire, 62 ressources, 5 voies judiciaires, 4 modèles/axes d’état, 14 transitions judiciaires et 6 relations épistémiques.

## Forme retenue

`structured_epistemic_state/5.0` est conservé comme forme native. Il s’agit d’un document d’état épistémique structuré, riche en assertions adressables et en métadonnées de provenance; il ne doit pas être aplati en une topologie universelle.

## Logical Contract v9

- Artifact ID : `urn:kristal:policeops:artifact:native-canon`
- Contract : `policeops.structured-epistemic-state/5.0`
- Commitment : `kristal.logical/jcs-sha256-v1` conservé en mode `precomputed` depuis le build v9 PoliceOps vérifié. Le build historique applique la `hash_target_policy` native et exclut les champs auto-référentiels (`state_id`, `content_hash`, `signatures`) avant engagement logique; le Local Kit générique ne doit pas redéfinir cette identité.

## Compatibilité

La projection v6 sous `.kristal/v8/` et les indexes v8 sont dérivés/rebuildables. Le build v9 legacy sous `.kristal/v9/` est conservé comme trace de migration mais n’est plus l’enveloppe d’authoring courante.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique

## Régimes d’information

Le corpus distingue actuellement 219 assertions `sourced`, 313 `claimed` et 6 `reviewed`. Les niveaux de certitude déclarés sont 141 `high` et 397 `medium`. Ces niveaux ne représentent pas des seuils juridiques.

## Validation et reconnaissance

Le `validation_summary` natif indique `validation_status=not_evaluated` et `recognition_status=under_review`. La réussite des validateurs structurels ne change pas ces statuts.

## Provenance et autorité

Une source et une provenance documentent d’où vient une information; elles ne suffisent pas à lui conférer une autorité normative. Les canaux d’autorité sont conservés lorsqu’ils existent, et leur absence reste explicite.

## Conflits / inconnus

La baseline déclare notamment `disagreement_preserved`. Les absences de source, d’autorité ou de représentation physique ne doivent pas être transformées en `false` ni en assertions inventées.

## Provenance de build

Les `.kristal/v8`, `.kristal/v9` et `build/v9` décrivent des transformations ou matérialisations techniques distinctes de la provenance épistémique des assertions.

## Sorties IA

Toute sortie IA est `proposal_only` jusqu’à acceptation explicite par le processus d’autorité approprié.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé

## Source de vérité

Le seul Logical Artifact membre du State v9 courant est `knowledge-base/corpus/policeops.structured-epistemic-state.json`. Il reste byte-for-byte inchangé par cette normalisation.

`canon/state.index.json` est le registre d’authoring. Le commitment y est `precomputed` afin de préserver exactement le commitment PoliceOps v9 déjà vérifié; ce choix évite de recalculer naïvement sur les champs auto-référentiels du fichier natif.

## Entrées et soutien

`knowledge-base/sources/`, les schémas, profils et documents décrivent les inputs et politiques ayant servi au corpus. `sources/source-catalog.json` normalise les 29 `source_refs` sans les promouvoir en Logical Artifacts canoniques.

## Dérivés / runtime

- `.kristal/v8/` : projection portable v6, lexiques et indexes v8;
- `.kristal/v9/` : build/qualification v9 legacy;
- `build/` : candidats construits avec le Local Kit 3.2.2;
- `validation/` : preuves de validation;
- `knowledge-base/runtime/` : baseline/matérialisation opérationnelle;
- `external-source-library/` : matérialisation/index de sources;
- `source-manager/` : outillage d’acquisition/résolution.

## Matérialisation

Un changement de bytes physiques d’une représentation de source, d’un index ou d’un packing ne doit pas modifier le Logical Commitment du corpus canonique.
