# Kristal Fungi v1.0.0

Kristal Fungi décrit les **réseaux mycéliens et les cycles fongiques** comme un graphe de référence :

`substrat → digestion externe / absorption → croissance hyphale → mycélium → reproduction / dispersion`

avec un axe parallèle :

`champignon ↔ symbiose ↔ hôte / racine → échanges → cycles de nutriments`

Le paquet est natif **Kristal Standard 6.0** et utilise `kristal_state` comme couche canonique.

## Pourquoi ce découpage

Le Kristal traite le mode de vie fongique plutôt qu’une taxonomie exhaustive. Il relie structure, acquisition de ressources, croissance en réseau, reproduction, symbioses et décomposition sans transformer les métaphores populaires sur le mycélium en règles scientifiques.

## Invariants sémantiques

- **champignon visible ≠ organisme fongique entier** : le sporophore n’est qu’une structure reproductive de certains Fungi;
- **mycélium ≠ morphologie universelle** : les levures et formes dimorphiques empêchent cette généralisation;
- **spore ≠ graine**;
- **symbiose ≠ mutualisme**;
- **mycorhize ≠ réseau mycorhizien commun**;
- **connexion physique ≠ coopération générale**;
- **transfert de ressources ≠ bénéfice net démontré pour tous les partenaires**;
- **réseau mycélien ≠ Internet, cerveau ou système intentionnel de communication**;
- **décomposeur ≠ capacité universelle à dégrader toute matière organique**.

## Contenu

- 165 assertions atomiques;
- 80 référents;
- 10 sources de référence;
- index dérivés par sujet, prédicat, échelle et thème;
- rapport de couverture et validation structurelle;
- schéma Kristal v6 embarqué.

## Frontière

Inclus : cellule fongique, hyphes, mycélium, substrat, digestion extracellulaire, absorption, saprotrophie, croissance/réseaux, spores, reproduction sexuée et asexuée, mycorhizes, lichens, réseaux mycorhiziens communs avec limites d’inférence, décomposition et cycles de nutriments/carbone.

Exclus volontairement : taxonomie exhaustive, identification d’espèces, mycologie clinique, toxicologie, protocoles de culture, pharmacologie, écologie complète des communautés et biochimie enzymatique détaillée.

## Statut épistémique

Le paquet est `reference` et les assertions sont `sourced`. Les affirmations fortement médiatisées sur les réseaux mycorhiziens communs sont explicitement bornées : une connexion ou un flux mesuré ne suffit pas à démontrer une coopération universelle ou un bénéfice net.

## Fichiers principaux

```text
knowledge-base/
  corpus/fungi.kristal-state.json
  corpus/referents.json
  corpus/index.json
  corpus/coverage-report.json
  corpus/validation-report.json
  sources/source-catalog.json
  sources/evidence-registry.json
  documentation/CONTENT_BOUNDARY.md
  documentation/NETWORK_MODEL.md
  documentation/SEMANTIC_GUARDRAILS.md
  schemas/kristal-state.schema.json
  tools/validate.py
```

## Kristal v9

Ce repo est migré vers **Kristal 9.0.0-draft.1 — Semantic State Architecture** sans supprimer les surfaces v6/v8 existantes.

- canon v9 : le state v6 canonique `knowledge-base/corpus/fungi.kristal-state.json`;
- snapshot logique immuable : `.kristal/v9/state-snapshot.json`;
- matérialisation(s) : `.kristal/v9/materialization.*.json`;
- projection portable v6 : conservée sous `.kristal/v8/portable-state.kristal-state.json` et explicitement dérivée;
- indexes/read models v8 : restent dérivés et reconstruisibles;
- identité logique v9 : séparée des digests physiques des fichiers.

Voir `.kristal/v9/README.md` et `V9-MIGRATION.md`.
