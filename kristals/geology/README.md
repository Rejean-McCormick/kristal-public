# Kristal-Geology v1.0.0

**Matière terrestre dans le temps** — matériau → processus → structure → strate → événement géologique.

Kristal-Geology décrit comment les matériaux terrestres sont produits, transformés, déformés, déposés, organisés en unités stratigraphiques et interprétés comme un enregistrement d'événements dans le temps profond.

## Noyau conceptuel

```text
EarthMaterial ──process──> transformed material
      │                         │
      └──────────────> Structure / Stratum
                                │
                          Stratigraphic record
                                │
                     GeologicEvent + GeologicAge
```

Le modèle distingue explicitement :

- **processus** : type atemporel de transformation (`faulting`, `deposition`, `metamorphism`);
- **événement** : occurrence temporelle d'un ou plusieurs processus;
- **strate** : couche matérielle;
- **unité lithostratigraphique** : corps de roche défini/cartographié par ses caractères lithologiques;
- **unité géochronologique** : intervalle de temps;
- **unité chronostratigraphique** : corps de roche correspondant à un intervalle de temps.

## Portée v1

- matériaux : magma/lave, sédiments, 3 grandes familles de roches, exemples de roches et minéraux;
- processus : magmatiques, sédimentaires, diagénétiques, métamorphiques, structuraux et tectoniques;
- structures : litage, foliation, failles, plis, contacts, intrusions et discordances;
- stratigraphie : strate, banc, membre, formation, groupe, supergroupe et autres types d'unités;
- temps : ICS **2026/06**, du Précambrien au Quaternaire aux rangs Super-Eon/Eon/Era/Period;
- datation : principes relatifs + familles de méthodes radiométriques;
- événements : gabarits explicites reliant processus, produits et âge;
- cartographie : concepts minimaux compatibles avec les cartes géologiques et structures FGDC/USGS.

## Hors portée volontaire

Kristal-Geology n'est pas :

- un double de **Kristal-Earth** (stocks/flux/cycles du système Terre);
- une base de **géographie physique / géomorphologie** exhaustive;
- un catalogue mondial de formations nommées, gisements ou cartes locales;
- une base de sismologie temps réel ou de risques naturels;
- une minéralogie/cristallographie exhaustive;
- une paléontologie ou histoire de la vie détaillée.

Ces domaines peuvent devenir des Kristals voisins.

## Reproductibilité

```bash
python knowledge-base/tools/build.py
python knowledge-base/tools/validate.py
python knowledge-base/tools/query.py --concept unconformity
```

Les sources distantes sont cataloguées par métadonnées; leur texte intégral n'est pas embarqué. Tous les artefacts canoniques sont reconstruits de façon déterministe et couverts par SHA-256.

## Kristal v9

Ce repo est migré vers **Kristal 9.0.0-draft.1 — Semantic State Architecture** sans supprimer les surfaces v6/v8 existantes.

- canon v9 : le state v6 canonique `knowledge-base/corpus/geology.kristal-state.json`;
- snapshot logique immuable : `.kristal/v9/state-snapshot.json`;
- matérialisation(s) : `.kristal/v9/materialization.*.json`;
- projection portable v6 : conservée sous `.kristal/v8/portable-state.kristal-state.json` et explicitement dérivée;
- indexes/read models v8 : restent dérivés et reconstruisibles;
- identité logique v9 : séparée des digests physiques des fichiers.

Voir `.kristal/v9/README.md` et `V9-MIGRATION.md`.
