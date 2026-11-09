# Kristal Power — paquet consolidé (Power Dynamics v6.5 intégré)

Structure stable, explicite et sans numéro de version dans les noms de dossiers.

```text
Kristal-Power/
├── knowledge-base/   # base canonique de la topologie du pouvoir
├── corpus-indexer/         # indexeur de métadonnées savantes
└── local-corpus-index/     # état local généré, non canonique
```

Les versions restent dans les métadonnées techniques (`VERSION`, manifestes, changelogs et documents de migration) afin de conserver la compatibilité et l’historique.

Le corpus indexer lit `knowledge-base/` sans le modifier et écrit sa base SQLite dans `local-corpus-index/`.


## Enveloppe Local Kristal — Kit 3.2.3

Ce snapshot est normalisé comme workspace `kristal.local-workspace/3.2.0` sans réécriture sémantique du corpus.

- État logique : `urn:kristal:state:power`
- Artefact canonique : `knowledge-base/corpus/power-topology.structured-epistemic-state.json`
- Contrat natif : `structured_epistemic_state/5.0`
- Registre d'authoring : `canon/state.index.json`
- Catalogue de sources : `sources/source-catalog.json`
- Documentation normative locale : `docs/00_INTENT_AND_SCOPE.md` à `docs/07_HOSTING_AND_PUBLICATION.md`
- V8/V9 historiques : conservés sous `.kristal/` comme dérivés/materialisations
- Manifest v9 historique `native-blob/1` enregistré dans `materializations/v9/manifests/` avec le Kit 3.2.3, sans modification du State Commitment.

Validation locale recommandée :

```bash
python knowledge-base/tools/validate.py
python tools/kristal.py check .
python tools/kristal.py build-v9 .
```

La construction, la publication et l'activation restent des étapes séparées.

## Actualisation du corpus — octobre 2026

La source Power Dynamics v6.5 est intégrée comme corpus attribué. Les nouveaux documents traitent des récits et de la légitimité, de « Gather to Liberate », des attestations polycentriques directionnelles et sélectives, des règles de reconnaissance versionnées et révocables, et des instances fédérées duplicables. Trois objets analytiques structurés illustrent ces thèmes.

**Portée épistémique :** ce sont des intentions de conception, des reconstructions analytiques et des scénarios hypothétiques, sans preuve de déploiement ou de partenariat d'organisations citées en exemple. Le clonage des logiciels n'entraîne pas celui des mandats juridiques, des marques ni de la réputation des institutions.

Voir `knowledge-base/documentation/ENRICHMENT_v0.7_POWER_DYNAMICS.md` pour la provenance, les bornes et la validation.

## Compatibilité et portabilité du présent snapshot

- Domaine : **Topologie du pouvoir v0.7.0** sur la source Power Dynamics v6.5.
- Entrée canonique : `knowledge-base/corpus/power-topology.structured-epistemic-state.json` (état recalculé).
- Nouveau candidat v9 : `build/v9/` et `state/state-snapshot.json`, sans publication ni activation automatique.
- Nouveau read model IA hors ligne : `AI_START_HERE.md`, `AI_MANIFEST.json` et `ai/`, lié au même State Logical Commitment.
- `.kristal/v8` et `.kristal/v9` sont les **archives techniques historiques** de l'ancien état ; ne pas les traiter comme la matérialisation courante de v0.7.
- `materializations/v9/manifests/` contient le manifeste actualisé de la matérialisation canonique ; il peut être vérifié sans copie physique supplémentaire.
- La conformité du paquet n'est ni une validation académique des hypothèses ni une qualification indépendante de production.
