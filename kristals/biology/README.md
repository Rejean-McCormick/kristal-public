# Kristal Biology v1.0.0

Kristal Biology décrit l'**organisation du vivant** comme un graphe de référence multi-échelle :

`cellule → tissu → organisme → population`

Quatre processus transversaux structurent le corpus : **fonction, reproduction, hérédité/héritabilité et évolution**. Le paquet est natif **Kristal Standard 6.0** et utilise `kristal_state` comme couche canonique.

## Pourquoi ce découpage

Le Kristal vise le noyau conceptuel général de la biologie plutôt qu'une encyclopédie taxonomique ou biomédicale. Il relie les mécanismes cellulaires à leurs conséquences organismiques et populationnelles sans confondre les échelles.

## Invariants sémantiques

- **hérédité ≠ héritabilité** : la première est une transmission; la seconde est une propriété statistique de variation dans une population et un contexte;
- **division cellulaire ≠ reproduction de l'organisme** : elles coïncident souvent chez les unicellulaires mais pas chez les multicellulaires;
- **sélection naturelle ≠ évolution** : la sélection est un mécanisme parmi plusieurs;
- **l'individu ne remplace pas la population comme unité de changement évolutif intergénérationnel**;
- **fonction ≠ intention** : les fonctions sont représentées comme rôles/contributions biologiques;
- **tissu/organe ne sont pas universels** : le corpus ne force pas l'organisation animale sur tout le vivant;
- **héritabilité ≠ pourcentage d'un caractère individuel causé par les gènes**.

## Contenu

- 129 assertions atomiques;
- 67 référents;
- 17 sources de référence;
- index dérivés par sujet, prédicat, échelle et thème;
- rapport de couverture et validation structurelle;
- schéma Kristal v6 embarqué.

## Frontière

Inclus : théorie cellulaire, organisation multicellulaire, fonctions générales, division/reproduction, génétique de base, héritabilité, variation, génétique des populations et mécanismes évolutifs.

Exclus volontairement : biochimie détaillée (Kristal Chemistry), anatomie/physiologie humaine spécialisée (HumanBody), maladie et traitement, communautés/écosystèmes (futur Ecology), taxonomie exhaustive, virologie détaillée et origines de la vie.

## Statut épistémique

Le paquet est `reference` et les assertions sont `sourced`. La validation fournie vérifie le schéma, les références, la traçabilité et les garde-fous sémantiques. Elle **ne prétend pas** qu'un hash, un build ou une source stockée crée à lui seul une autorité scientifique.

## Fichiers principaux

```text
knowledge-base/
  corpus/biology.kristal-state.json
  corpus/referents.json
  corpus/index.json
  corpus/coverage-report.json
  corpus/validation-report.json
  sources/source-catalog.json
  sources/evidence-registry.json
  documentation/CONTENT_BOUNDARY.md
  documentation/SCALE_MODEL.md
  documentation/SEMANTIC_GUARDRAILS.md
  schemas/kristal-state.schema.json
  tools/validate.py
```
