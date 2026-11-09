# AI Context — kOA / Koali Sales Pitch

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:koa-sales-pitch`
- State Logical Commitment: `sha256:97bf4babbe6111bd71cc2f4687c1320da4466f91aca3da2dcd37d9c8a83a224e`
- Workspace profile: `layered`
- Native model: `structured_qa_evidence_state`
- Canonical artifacts: `1`
- Sources: `51`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et scope

## Pourquoi ce Kristal existe

Ce Kristal fournit une base de connaissance structurée et un copilote de rencontre pour présenter kOA / Koali avec un langage adapté à l'interlocuteur, des réponses gouvernées, des preuves explicites et des limites de preuve visibles.

## Corpus / problème de départ

Le corpus combine des extraits du Business Plan, de l'écosystème kOA, du Kristal Framework, des mosaïques de scénarios, des références structurelles et des matériaux utilisateur. Il les transforme en chemins Q&A, profils de lecture, règles de preuve et surfaces de rencontre.

## Résultats attendus

- répondre d'abord au besoin puis à l'architecture ;
- conserver la provenance et les limites de chaque affirmation ;
- adapter la profondeur aux audiences sans modifier la vérité sous-jacente ;
- empêcher les surclaims sur traction, E2E, sécurité, marché et validation ;
- permettre la reconstruction des vues et index à partir du canon et des sources.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique

## Subject / territoire

Le Subject est le **Sales Pitch kOA / Koali** : connaissance structurée, positionnement, réponses de rencontre, preuves/limites et chemins conversationnels nécessaires à cette fonction.

## Possède

Le Kristal possède son état Sales Pitch compilé, ses 142 assertions Q&A gouvernées, son modèle local de preuve, ses règles de positionnement et sa composition locale des sources.

## Ne possède pas

Il ne possède pas l'autorité globale des dépôts kOA, du Business Plan, des scénarios externes ou des domaines HospitalOps/PoliceOps. Il ne possède pas non plus une vérité de marché courante, une certification de sécurité ou une preuve E2E absente.

## Relations avec d'autres Kristals

Les informations d'écosystème, de framework, de scénarios et de références structurelles sont ici des **sources** ou des références de contexte. Aucune relation externe n'est promue dans `external_references` sans Logical Commitment v9 piné.

## State identity v9

`state_ref = urn:kristal:state:koa-sales-pitch` et `authority_ref = urn:kristal:authority:koa-sales-pitch`. La normalisation 3.2.2 préserve le Logical Commitment v9 historique.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif

## Primitives du domaine

Les primitives dominantes sont : question canonique, variantes de question, audience, intention, réponse par profondeur, référence de preuve, posture de preuve, interdits de formulation, routage conversationnel et carte live.

Le state v6 ajoute provenance, avertissements, profils de lecteurs et extensions vers les règles de preuve, la terminologie, les pathways, le meeting-state et les autres modèles de support.

## Relations / transformations

`sources éditoriales → état structuré Q&A → profils/index → vues de rencontre → requête`. Les projections de lecture n'acquièrent pas d'autorité en étant matérialisées.

## Dimensions internes

Les axes épistémiques majeurs sont besoin/problème, technique/solution, commercial/marché et impact. Les axes de lecture incluent audience, famille de question, priorité et profondeur de réponse.

## Forme native retenue

`structured_qa_evidence_state`

Cette forme conserve simultanément les réponses, leur contexte, leurs limites, leur provenance et leur routage conversationnel.

## Logical Contracts v9

Le Logical Artifact canonique utilise `kristal.v6-state-reference/1.0`. Son commitment est `kristal.logical/jcs-sha256-v1` et est préservé depuis l'enveloppe v9 historique.

## Pourquoi cette forme ne perd pas d'information essentielle

Réduire le Kristal à une simple collection de textes ferait disparaître les niveaux de réponse, la posture de preuve, les interdits, le routage et les liens de provenance. Réduire le tout à un graphe générique masquerait la logique Q&A opérationnelle.

## Alternatives rejetées

- document Markdown unique ;
- ontologie générique unique ;
- fusion des sources et du canon ;
- promotion des vues/index au rang de vérité.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique

## Régimes d'information

Le Kristal distingue au minimum : source documentée, synthèse interne, illustration de design, état de rencontre mutable, preuve technique, validation commerciale, preuve d'impact et inconnus à rafraîchir.

## Provenance épistémique

La provenance est portée par les `evidence_refs`, le registre des sources et le state v6. Une source référencée soutient une affirmation dans un scope donné ; elle ne devient pas automatiquement autorité globale.

## Autorité

La carte kOA Ecosystem la plus récente contrôle les définitions courantes des composants ; le Business Plan contrôle les faits business/offres/marché/risques dans la limite de son snapshot ; le Kristal Framework contrôle les invariants de standard/query. Les synthèses locales servent le Sales Pitch mais ne remplacent pas ces autorités sources.

## Incertitude / conflits / inconnus

Les limites existantes sont conservées : E2E non vérifié sans artefact, scénarios non assimilés à une validation de marché, sécurité non assimilée à un audit/certification, données commerciales courantes à rafraîchir. `unknown` ou `non vérifié` est préférable à une affirmation inventée.

## Provenance de build

La derivation informatique v6/v8/v9 est distincte de la provenance épistémique. Les anciens read models `.kristal/v8`, les vues et les nouveaux `build/v9` sont reconstructibles.

## Politique des sorties IA

Les sorties IA sont des propositions jusqu'à validation explicite. Elles ne peuvent ni créer une preuve, ni lever un gate, ni devenir autorité par simple génération.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé

## Source de vérité

Le canon Local 3.2.2 est `canon/domain/sales-pitch.kristal-state.json`. Il est une copie byte-identique de l'ancien état compilé v6 afin de préserver la continuité sémantique.

`knowledge-base/corpus/sales-pitch.kristal-state.json` est conservé comme **miroir de compatibilité legacy** pour les outils v6/v8 et doit rester byte-identique au canon tant que ces outils existent.

## Logical Artifacts canoniques

`canon/state.index.json` enregistre `urn:kristal:koa-sales-pitch:canonical` sous le contrat `kristal.v6-state-reference/1.0`. Le commitment précomputed préserve l'identité logique v9 déjà établie.

## Artefacts dérivés / Runtime

Sont dérivés : `.kristal/v8`, `.kristal/v9` historique, `views/`, `knowledge-base/profiles/`, `knowledge-base/corpus/` comme miroir legacy, `derived/`, `runtime/`, `state/` et `build/`.

Les fichiers sous `knowledge-base/sources/` restent des entrées éditoriales/support ; ils ne sont pas promus individuellement comme Logical Artifacts canoniques dans cette migration.

## Materializations

La copie sous `canon/domain` est la matérialisation locale autoritative utilisée par le workspace 3.2.2. L'ancienne matérialisation v9 sous `.kristal/v9` demeure un artefact historique de compatibilité.

## Recettes de reconstruction

Le package conserve ses outils natifs `knowledge-base/tools/validate.py` et `query.py`. Le lifecycle Local 3.2.2 utilise `tools/kristal.py check .` puis `tools/kristal.py build-v9 .`.
