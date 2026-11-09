# AI Context — King Klown 4.2.0 MEDIA

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:king-klown-media`
- State Logical Commitment: `sha256:f237db441d6946b45b7cc06a82e96afe3f43d00dbb6192274e27785bb4f599ba`
- Workspace profile: `layered`
- Native model: `layered-registry-ledger-semantic-graph`
- Canonical artifacts: `9`
- Sources: `5`
- External pinned references: `0`
- Materialization manifests: `9`
- Workspace-local materialization blobs: `9`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et scope

## Pourquoi ce Kristal existe

Ce Kristal représente la couche **King Klown MEDIA** du domaine King Klown : œuvres, manifestations média, liens avec les événements de l'Univers, alias, règles de lecture et éléments épistémiques nécessaires pour interpréter ces relations. La normalisation 3.2.2 est architecturale : elle ne révise pas le contenu de domaine.

## Corpus / problème de départ

Le snapshot reçu contient une architecture v9 antérieure au Local Authoring Kit 3.2.2, avec 9 Logical Artifacts et une projection de compatibilité v6/v8. Le contenu v9 est déjà qualifié par ses outils historiques ; l'écart principal est l'absence de l'enveloppe `kristal.local-workspace/3.2.0`.

## Résultats attendus

- conserver `state_ref = urn:kristal:state:king-klown-media` ;
- conserver le Logical Commitment d'état `sha256:f237db441d6946b45b7cc06a82e96afe3f43d00dbb6192274e27785bb4f599ba` ;
- exposer les Logical Artifacts canoniques sous `canon/` sans réécriture sémantique ;
- distinguer canon, sources, projections, builds, matérialisations et opérations de publication/activation ;
- permettre `check` puis `build-v9` avec le kit 3.2.2.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique

## Subject / territoire

Le territoire est la couche média-et-univers de King Klown telle qu'elle est matérialisée par les Logical Artifacts v9 de ce paquet.

## Possède

Le Kristal possède les registres d'entités, d'œuvres et d'alias présents dans ses artefacts, le ledger d'événements d'univers, les relations sémantiques `media → work → event/arcs`, le noyau épistémique, le registre de contradictions, la reader policy et les clarifications du créateur effectivement emballées ici.

## Ne possède pas

Le Kristal ne possède pas l'inventaire brut des URL et objets média de UCKK Médiathèque. Les catalogues UCKK sont seulement pinés par hash lorsqu'ils sont absents du paquet. Il ne possède pas non plus le nom civil de `AUTHOR_REAL`, qui reste explicitement non affichable.

## Relations avec d'autres Kristals / registres

UCKK Médiathèque demeure le registre primaire de l'inventaire média et des URL. Ce Kristal conserve la sémantique King Klown correspondante. Aucune référence d'état v9 externe n'est inventée : les catalogues externes présents ici ne fournissent que des pins de fichiers, pas un Logical Commitment d'un autre State Snapshot.

## State identity v9

Le `state_ref` est `urn:kristal:state:king-klown-media`. Les références externes sémantiques restent vides tant qu'aucun engagement logique externe vérifiable n'est disponible.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif

## Primitives du domaine

Le modèle natif est composé de neuf artefacts logiques : **entities**, **works**, **universe events**, **media semantic layer**, **aliases**, **epistemic core**, **contradictions**, **reader policy** et **creator clarifications**.

## Relations / transformations

La couche média dépend des œuvres et événements ; les alias dépendent des entités et de la couche média ; le noyau épistémique dépend notamment des entités, œuvres, événements, reader policy et clarifications ; le registre de contradictions dépend du noyau épistémique. Ces dépendances sont conservées dans les Logical Artifacts eux-mêmes.

## Dimensions internes

Les dimensions utiles incluent le type d'objet (entité, œuvre, événement, manifestation), la plateforme média, les liens œuvre/événement/arcs, le statut épistémique et l'autorité. Elles ne sont pas aplaties en un schéma universel unique.

## Forme native retenue

`layered-registry-ledger-semantic-graph`

Le modèle combine des registres, un ledger d'événements, un graphe de relations sémantiques média et une couche épistémique transversale.

## Logical Contracts v9

Les contrats et versions sont ceux portés par `canon/state.index.json` et les neuf Logical Artifacts. Les engagements sont conservés en mode `precomputed` afin qu'une migration physique vers `canon/` ne change aucun Logical Commitment.

## Pourquoi cette forme ne perd pas d'information essentielle

Transformer l'ensemble en une simple table d'assertions ferait perdre la distinction entre registres structuraux, ledger d'événements, couche média, politiques de lecture, contradictions et provenance épistémique.

## Alternatives rejetées

- un JSON universel unique comme nouvelle source de vérité ;
- la projection v6 comme seul canon v9 ;
- les index v8 comme autorité sémantique ;
- la duplication des œuvres pour chaque plateforme média.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique

## Régimes d'information

Le paquet distingue les connaissances canoniques, les déclarations explicites mais non gouvernantes, les propositions et les informations provenant du catalogue média. L'absence d'une donnée n'implique pas qu'elle soit fausse.

## Provenance épistémique

La provenance est conservée dans le noyau épistémique, les sources emballées, les pins de catalogues externes et les clarifications du créateur. Une source et une autorité ne sont pas synonymes.

## Autorité

Ordre explicitement conservé par la reader policy : `current explicit creator clarification > DECISIONS > CANON > current canonical source > source branch > media catalog > interpretation`. UCKK Médiathèque est l'autorité primaire pour l'inventaire brut média/URL ; King Klown possède les relations sémantiques emballées ici.

## Incertitude / conflits / inconnus

Les contradictions sont conservées dans un artefact distinct. Les cas partiels ou manquants restent partiels/manquants ; ils ne sont pas complétés par inférence silencieuse.

## Provenance de build

La derivation informatique historique reste sous `.kristal/v9/derivations/`. La normalisation 3.2.2 ajoute une enveloppe d'authoring et copie byte-identiquement les artefacts canoniques vers `canon/artifacts/`; elle ne constitue pas une nouvelle preuve épistémique.

## Politique des sorties IA

Les sorties IA sont `proposal_only` jusqu'à validation explicite et ne sont jamais autorité par elles-mêmes.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé

## Source(s) de vérité

Pour l'authoring Local 3.2.2, `canon/state.index.json` est le registre des Logical Artifacts canoniques. Les fichiers sous `canon/artifacts/` sont des copies **byte-identiques** des neuf artefacts précédemment canoniques sous `.kristal/v9/artifacts/`. Leur déplacement physique ne change donc ni contrat ni engagement logique.

## Logical Artifacts canoniques

Les neuf artefacts sont déclarés dans `canon/state.index.json` en mode `precomputed` avec leurs engagements `kristal.logical/jcs-sha256-v1` existants.

## Artefacts dérivés / Runtime

`.kristal/v8/` reste un read model/query/index legacy. `.kristal/v9/` est conservé comme surface v9 historique de matérialisation, échange, activation locale et compatibilité. `knowledge-base/media_coverage_report.json`, les index et les sorties `build/` ne sont pas le canon.

## Materializations

Les materialization manifests historiques sous `.kristal/v9/materializations/` décrivent la représentation physique des Logical Artifacts. Ils ne remplacent pas l'identité logique.

## Recettes de reconstruction

- validation historique de domaine : `python knowledge-base/tools/validate.py` ;
- rebuild historique v9 : `python knowledge-base/tools/build_v9.py` ;
- validation Local 3.2.2 : `python tools/kristal.py check .` ;
- build Local 3.2.2 : `python tools/kristal.py build-v9 .`.
