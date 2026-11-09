# Kristal-Infrastructure

**Édition 1.0.0 — Kristal v6 natif**

Kristal-Infrastructure décrit les **réseaux physiques de service** : des actifs reliés qui fournissent un service en transportant, distribuant, convertissant ou mettant à disposition une ressource ou une capacité.

## Thèse de domaine

```text
nœuds + liens
     ↓
service + flux
     ↓
capacité ↔ demande
     ↓
dépendances
     ↓
perturbation → dégradation / défaillance → perte de service
     ↓
résilience → absorption / substitution / rétablissement / adaptation
```

Les six axes canoniques sont **topologie, service, capacité, dépendances, défaillances, résilience**.

## Contenu

- `corpus/infrastructure.kristal-state.json` — état canonique v6;
- `corpus/referents.json` — vocabulaire bilingue FR/EN;
- `corpus/network-archetypes.json` — projections légères vers énergie, eau, transport, conduites, télécoms physiques et logistique;
- `corpus/invariants.json` — distinctions structurelles à préserver;
- `corpus/navigation.json` — chemin de lecture et hubs inter-axes;
- `corpus/boundaries.json` — frontières avec ingénierie, Computing, Security, Geography et opérations temps réel;
- `sources/source-catalog.json` — références institutionnelles;
- `validation/validation-report.json` — validation structurelle et référentielle;
- `manifest.sha256.json` — intégrité de l'édition.

## Principe éditorial

Le noyau représente des **relations stables** plutôt que des inventaires d'actifs réels. Il doit pouvoir décrire une conduite d'eau, une ligne électrique, une route ou une fibre avec les mêmes primitives sans nier leurs différences physiques.
