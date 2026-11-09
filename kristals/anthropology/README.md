# Kristal-Anthropology

**Version 0.1.0 — Kristal Standard 6.0**

Kristal-Anthropology représente des **systèmes culturels comparables sans les réduire à des essences**. Chaque assertion est attachée à une population, un lieu, une portée temporelle et une source.

## Objets centraux

- **systèmes culturels** — unités de comparaison contextualisées;
- **éléments culturels** — pratiques, parenté, symboles, institutions, normes, langues, moyens d’existence et relations environnementales;
- **relations** — liens sourcés entre éléments;
- **axes de comparaison** — index analytiques, jamais des classements;
- **sources** — provenance explicite par système, élément et relation.

## Principe majeur

`observé_dans(X, contexte)` n’implique jamais `essentiel_à(X)`.

Les formulations universelles du type « les X sont… » sont exclues du canonical state si la source ne justifie pas explicitement cette portée. Une description doit pouvoir changer selon le lieu, la période, le sous-groupe ou la source.

## Entrée canonique v6

`knowledge-base/corpus/anthropology.kristal-state.json`

## Validation

```bash
python knowledge-base/tools/validate.py
```

## Requêtes rapides

```bash
python knowledge-base/tools/query.py system system:bali-subak
python knowledge-base/tools/query.py axis axis:kinship
python knowledge-base/tools/query.py element element:whakapapa
python knowledge-base/tools/query.py compare axis:environment
```

## Portée v0.1.0

Seed comparatif volontairement dispersé : Māori, Inuit du Nunavut, Yolŋu, Sámi, subak balinais, Haudenosaunee et Kallawaya. Il sert à éprouver le modèle avant densification régionale. Les lacunes sont rendues explicites dans `coverage.json`.
