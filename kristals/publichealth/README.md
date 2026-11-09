# Kristal-PublicHealth

**Édition 1.0.0 — Kristal v6 natif**

Kristal-PublicHealth décrit la **santé à l’échelle des populations** : comment une population est définie, comment son contexte façonne ses expositions, comment des interventions modifient ces expositions ou déterminants, et comment les résultats sont mesurés et distribués.

## Thèse de domaine

```text
population
    ↓
contexte / déterminants
    ↓
exposition
    ↓                 ↘
intervention ─────────→ résultat
    ↘                    ↙
      mesure / évaluation
             ↓
      distribution / équité
```

Les six axes canoniques sont **population, contexte/déterminants, exposition, intervention, résultat, mesure/évaluation**.

## Contenu

- `corpus/publichealth.kristal-state.json` — état canonique v6;
- `corpus/referents.json` — vocabulaire bilingue FR/EN;
- `corpus/public-health-pathways.json` — parcours conceptuels à travers les axes;
- `corpus/invariants.json` — distinctions à ne pas effondrer;
- `corpus/navigation.json` — hubs et chemin de lecture;
- `corpus/boundaries.json` — frontières avec médecine clinique, HumanBody, statistiques, environnement, droit et systèmes de santé;
- `sources/source-catalog.json` — références institutionnelles;
- `validation/validation-report.json` — validation structurelle, référentielle et de provenance;
- `manifest.sha256.json` — intégrité de l’édition.

## Principe éditorial

Le corpus privilégie les **relations stables** entre population, déterminants, expositions, interventions et résultats. Il ne contient ni alertes en cours, ni recommandations locales, ni seuils opérationnels, ni données épidémiologiques temps réel.
