# Kristal-Neuroscience

**Version:** 1.0.0  
**Édition:** 2026-10-02  
**Format canonique:** Kristal Standard 6.0 (`kristal_state`)

Kristal-Neuroscience est un corpus statique, traçable et orienté IA consacré à l'organisation fonctionnelle du système nerveux.

## Axe conceptuel

`cellule → connexion → circuit → région → signal → comportement`

La **fonction** n'est pas placée comme propriété exclusive d'une région. Elle constitue une couche relationnelle entre circuits, régions, signaux et comportements. Le modèle impose une lecture **many-to-many** et contextuelle.

## Principes

- une cellule est décrite par plusieurs dimensions (moléculaire, morphologique, physiologique, spatiale, connexionnelle);
- une connexion structurelle ne prouve pas à elle seule une fonction active;
- une région ne correspond pas à une fonction unique;
- un signal mesuré n'est pas nécessairement le phénomène neural lui-même (BOLD, calcium, LFP, EEG, etc.);
- corrélation, perturbation, lésion, nécessité et suffisance sont distinguées;
- espèce, stade, état, tâche, atlas, site et méthode peuvent changer le sens d'une assertion.

## Couverture

- cellules : neurones, glies et classes représentatives;
- connexions : synapses, projections, faisceaux et motifs de convergence/divergence;
- circuits : microcircuits, récurrence, inhibition latérale, désinhibition, boucles distribuées et systèmes représentatifs;
- régions : grandes structures du SNC et du SNP;
- signaux : potentiel de membrane, spikes, LFP, EEG/ECoG/MEG, calcium et BOLD;
- fonctions : sensation, mouvement, mémoire, apprentissage, attention, état, décision, homéostasie, etc.;
- comportements : locomotion, choix, parole, sommeil, exploration et autres observables;
- méthodes et preuves : électrophysiologie, imagerie, traçage, connectomique, perturbation et tâches.

## Frontière

Ce Kristal n'est ni un atlas clinique, ni un modèle diagnostique, ni un guide de traitement. Les taxonomies cellulaires et atlas détaillés restent des ressources externes versionnables. Les associations fonctionnelles sont des relations contextualisées, pas une cartographie phrénologique.

## Fichiers centraux

- `knowledge-base/corpus/neuroscience.kristal-state.json`
- `knowledge-base/corpus/neuroscience.referent-registry.json`
- `knowledge-base/sources/cell_model.json`
- `knowledge-base/sources/connection_circuit_model.json`
- `knowledge-base/sources/region_model.json`
- `knowledge-base/sources/signal_model.json`
- `knowledge-base/sources/function_behavior_model.json`
- `knowledge-base/sources/methods_evidence_context.json`
- `validation/neuroscience-validation-report.json`
