# Kristal Climate v1.0.0

Kristal Climate décrit le **climat comme distribution statistique de long terme d’un système physique**, structurée autour de :

`forçages → réponse → rétroactions → distributions → variabilité → tendances`

Cette chaîne est une navigation conceptuelle, pas une séquence temporelle obligatoire. Les rétroactions font partie de la réponse du système; la variabilité interne peut masquer ou amplifier temporairement une tendance; les distributions peuvent changer par leur moyenne, leur dispersion, leur saisonnalité ou leurs queues.

## Noyau

- système climatique et bilan énergétique;
- forçages naturels et anthropiques;
- forçage radiatif effectif;
- inertie thermique et réponse transitoire;
- rétroactions positives/négatives et principales familles physiques;
- climat comme distribution, moyenne, variance, anomalies et normales;
- variabilité interne, variabilité forcée, ENSO et téléconnexions;
- tendances, émergence du signal, détection, attribution et incertitude;
- extrêmes comme propriétés des queues d’une distribution.

## Invariants sémantiques

- **climat ≠ météo**;
- **climat ≠ moyenne seulement**;
- **normale climatologique ≠ climat immuable ni stationnarité**;
- **anomalie ≠ erreur**;
- **forçage ≠ rétroaction**;
- **forçage positif ≠ rétroaction positive**;
- **variabilité interne ≠ toute variabilité naturelle**;
- **tendance ≠ cause** : l’attribution est une opération distincte;
- **tendance globale ≠ même trajectoire locale partout**;
- **un événement météo isolé ≠ démonstration ou réfutation du changement climatique**;
- **rétroaction positive ≠ emballement nécessaire**.

## Contenu

- 159 assertions atomiques;
- 77 référents;
- 12 sources de référence;
- index par sujet, prédicat, échelle et thème;
- rapport de couverture et validation structurelle;
- schéma Kristal v6 embarqué.

## Frontière

Inclus : climat physique général, statistiques de long terme, bilan énergétique, forçages, rétroactions, variabilité, tendances, détection/attribution et incertitude.

Exclus : prévision météo opérationnelle, bulletins climatiques courants, impacts, risques socio-économiques, adaptation, mitigation, politique climatique, géographie régionale exhaustive, paléoclimatologie exhaustive et mécanique détaillée de l’atmosphère ou de l’océan.

## Fichiers principaux

```text
knowledge-base/
  corpus/climate.kristal-state.json
  corpus/referents.json
  corpus/index.json
  corpus/coverage-report.json
  corpus/validation-report.json
  sources/source-catalog.json
  sources/evidence-registry.json
  documentation/CONTENT_BOUNDARY.md
  documentation/CLIMATE_MODEL.md
  documentation/SEMANTIC_GUARDRAILS.md
  schemas/kristal-state.schema.json
  tools/validate.py
```
