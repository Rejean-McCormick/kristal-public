# Kristal-Sports v1.0.0

**Domaine :** sports — règle → participant → action → événement → score/résultat → compétition  
**Statut :** `working`  
**Snapshot éditorial :** 2026-10-02  
**Langue principale :** français

## Axe canonique

`règle → participant → action → événement → score/résultat → compétition`

Cet axe est un **ordre de lecture** du domaine, pas une chronologie universelle. Une règle peut gouverner directement une compétition, un événement peut ne pas modifier le score, et un résultat peut être mesuré plutôt que compté.

## Principe central

Sports modélise **la grammaire formelle de la compétition sportive** : contraintes, rôles, actions admissibles, événements arbitrables, mécanismes de résultat et formats de compétition. Il ne contient pas de résultats en direct, de prédictions ou de classements actuels.

## Garde-fous

- `action ≠ événement arbitré`
- `événement ≠ résultat agrégé`
- `score ≠ vainqueur automatique`
- `règle générique ≠ règle identique dans tous les sports`
- `participant organisationnel ≠ concurrent`
- `format de compétition ≠ sport`
- `temps ≠ points ≠ distance ≠ score de juges`
- toute règle spécifique est liée à une édition/source datée

## Contenu

Voir `knowledge-base/corpus/index.json`, `corpus/sports.kristal-state.json`, `corpus/sport-projections.json` et `sources/source_catalog.json`.

## Validation

```bash
cd knowledge-base
python tools/build.py
python tools/validate.py
python -m unittest tests/test_model.py
```

Le corpus est reconstruit de façon déterministe à partir de `sources/*.json`.
