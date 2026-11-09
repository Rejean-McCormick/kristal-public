# AI Context — Power — Topologie du pouvoir / Power Dynamics

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:power`
- State Logical Commitment: `sha256:7b9a4cbfa76756d13a50753ecb9faf0bdeaae015da5487366ad09c48b02f696e`
- Workspace profile: `layered`
- Native model: `layered_structured_epistemic_state_with_native_power_dynamics_contracts`
- Canonical artifacts: `1`
- Sources: `3`
- External pinned references: `0`
- Materialization manifests: `1`
- Workspace-local materialization blobs: `1`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et scope

## Pourquoi ce Kristal existe

Ce Kristal représente une **topologie du pouvoir** enrichie par le cadre source Power Dynamics. Il maintient une ontologie, un lexique, des régimes épistémiques, des graphes, des configurations contrôlées, des positions théoriques, du contexte, des contrats analytiques natifs Power Dynamics et une couche de preuve savante externe.

## Corpus / problème de départ

Le corpus de travail conserve les sources Power Dynamics, leurs schémas analytiques et leur provenance, puis les compile dans un `structured_epistemic_state/5.0`. La couche savante ajoute des référents, identifiants, graines de recherche, politiques de résolution et EvidenceLinks sans transformer le Kristal en bibliothèque locale de textes externes.

## Résultat normatif local

Le membre logique autoritatif est `knowledge-base/corpus/power-topology.structured-epistemic-state.json`. La normalisation Local Kristal 3.2.2 ajoute une enveloppe d'authoring et de lifecycle autour de cet artefact **sans réécriture sémantique**.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique

## Subject / territoire

Le territoire est la topologie du pouvoir et les mécanismes analytiques Power Dynamics associés : domaines, relations, ressources/capacités, dynamiques, conversions, routage, retours, boucles, autorité, reconnaissance/coordination, contre-pouvoirs et instruments d'évaluation.

## Possède

Le Kristal possède son modèle conceptuel local, ses assertions compilées et attribuées, ses contrats analytiques natifs, ses règles épistémiques locales et les liens de preuve qui ont été explicitement promus/qualifiés.

## Ne possède pas

Il ne possède ni les corpus savants distants, ni leur disponibilité, ni les index SQLite/FTS locaux du CorpusIndex. Un résultat de recherche externe reste un **candidat documentaire** tant qu'il n'a pas été revu et lié. Le Kristal ne transforme pas non plus un statut de source récent en rang de vérité.

## Relations avec d'autres composants

`corpus-indexer/` est un sidecar en lecture du Kristal : il peut importer des graines et produire des candidats, mais il ne modifie pas le canon. Les anciens paquets `.kristal/v8` et `.kristal/v9` sont conservés comme représentations/materialisations dérivées.

## State identity v9

- `state_ref`: `urn:kristal:state:power`
- `authority_ref`: `urn:kristal:authority:power`

Toute référence externe destinée à participer à l'état v9 devra être pinée à un Logical Commitment avant publication.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif

## Primitives du domaine

Le modèle combine des référents conceptuels stables avec des assertions séparées (libellés, alias, définitions éditoriales ou sourcées, positions, relations, contextes), ainsi que des objets analytiques Power Dynamics structurés. Les contrats natifs couvrent notamment `PowerRelation`, `AuthorityScope`, conversions, boucles, événements dynamiques, domaines, routages, surfaces, reconnaissance/coordination et profils de système.

## Relations / transformations

Les graphes de taxonomie, relations sémantiques et relations contextuelles sont distingués. Les relations dynamiques Power Dynamics restent attribuées à leurs sources et ne sont pas fusionnées silencieusement avec les relations statiques générales. Le builder déterministe compile ces couches dans l'état structuré.

## Dimensions internes

Le corpus emploie des dimensions typées et à cardinalité explicite. Power Dynamics ajoute des dimensions portant notamment sur l'état ontologique, les processus dynamiques, le routage, les possibilités effectives, la maturité des preuves et les types de claims.

## Forme native retenue

`layered_structured_epistemic_state_with_native_power_dynamics_contracts`

Cette forme est volontairement **layered** : elle conserve simultanément référents, assertions, provenance, graphes, configurations, contrats analytiques et distinctions épistémiques.

## Logical Contract v9

Le membre canonique est :

- Artifact ID : `urn:kristal:power:canonical-state`
- Contract : `structured_epistemic_state/5.0`
- Physical source : `knowledge-base/corpus/power-topology.structured-epistemic-state.json`

Le registre `canon/state.index.json` enveloppe ce contrat sans imposer une nouvelle ontologie universelle.

## Alternatives rejetées

Une simple taxonomie ou un graphe générique unique ferait perdre les distinctions entre document source, définition, objet analytique, assertion compilée, statut épistémique et preuve. Une conversion destructive n'est donc pas retenue.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique

## Régimes d'information

Le dépôt sépare explicitement : document source, terme/définition source, objet analytique structuré et assertion Kristal compilée. Les pages wiki et les fichiers canoniques du dépôt source gardent des statuts distincts. Une reconstruction analytique n'est pas présentée comme une citation textuelle.

## Provenance épistémique

Les assertions conservent leurs références et leur type de claim. La couche Scholarly Evidence Backbone distingue le candidat bibliographique de l'EvidenceLink promu après revue. Les rôles de preuve peuvent notamment supporter, définir, attribuer, illustrer, qualifier, disputer ou contredire.

## Autorité

`CURRENT-CORE`, `CURRENT-EXPERIMENTAL`, `CURRENT-DESIGN-NOTES`, `LEGACY-PROPOSAL` et `ANALYTICAL-RECONSTRUCTION` décrivent des statuts de source ou de maturité, **pas un classement automatique de vérité**. Les notes confirmées par l'architecte restent des intentions de design tant qu'une preuve technique ou d'adoption indépendante manque.

## Incertitude / conflits / inconnus

Les désaccords entre documents sont préservés. Les claims techniques actuels restent provisoires sans spécification ou code direct. La multiplicité de notices n'implique pas l'indépendance des preuves. La valeur par défaut de l'indépendance savante peut rester `unknown`.

## Provenance de build

`knowledge-base/tools/build.py` produit de manière déterministe le Structured Epistemic State, l'index et les EvidenceLinks compilés. Cette dérivation informatique est séparée de la provenance épistémique des claims.

## Politique des sorties IA

Toute sortie IA est une proposition jusqu'à validation explicite. Elle ne peut pas promouvoir seule un candidat documentaire, inventer une autorité ou modifier silencieusement les statuts épistémiques.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé

## Source de vérité v9

Le Logical Artifact autoritatif est le `structured_epistemic_state/5.0` situé historiquement à `knowledge-base/corpus/power-topology.structured-epistemic-state.json`. Son emplacement historique est conservé pour éviter une relocalisation ou duplication sémantiquement inutile.

## Logical Artifact canonique

`canon/state.index.json` enregistre l'Artifact ID `urn:kristal:power:canonical-state`, son contrat logique, son scope et son autorité. Le commitment est calculé par JCS + SHA-256 selon `kristal.logical/jcs-sha256-v1`.

## Inputs d'authoring et reconstruction

Les couches sous `knowledge-base/sources/`, les schémas et les règles de build constituent les entrées de reconstruction du corpus. Le validateur du domaine vérifie notamment résolution référentielle, provenance, intégrité du manifeste et rebuild déterministe.

## Artefacts dérivés / runtime

Sont dérivés ou opérationnels : `.kristal/v8`, `.kristal/v9`, `build/`, `state/`, `runtime/`, `projections/materialized/`, `local-corpus-index`, `knowledge-base/corpus/index.json` et `knowledge-base/corpus/evidence-links.json`.

`corpus-indexer/` est un outil/sidecar et non une seconde autorité sémantique.

## Materializations

Le paquet `.kristal/v9` préexistant matérialise le même membre logique et lie le blob canonique historique. La nouvelle sortie `build/v9` sert de candidat reproductible Local Kristal 3.2.2 ; elle ne devient publiée ou active que par des étapes distinctes.
