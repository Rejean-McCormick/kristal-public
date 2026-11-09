# Kristal-History

**Version 0.1.0 — Kristal Standard 6.0**

Kristal-History représente l'histoire comme un graphe temporel et causal sourcé plutôt que comme une suite de paragraphes.

## Objets centraux

- **événements** — occurrences ponctuelles ou étendues;
- **acteurs** — personnes, collectifs, organisations;
- **lieux** — lieux physiques ou régions historiques;
- **périodes** — fenêtres historiographiques explicitement conventionnelles lorsque nécessaire;
- **relations temporelles** — antériorité, chevauchement, inclusion, terminaison;
- **liens causaux** — contributeur, déclencheur, pression habilitante, précondition, processus institutionnel, etc.;
- **sources** — chaque événement et chaque lien causal possède ses propres références.

## Principe majeur

`avant(A,B)` n'implique jamais `cause(A,B)`.

Une causalité historique n'est stockée que lorsqu'une source la soutient, avec un type, un niveau de confiance et une note épistémique. Les explications concurrentes doivent coexister plutôt qu'être fusionnées artificiellement.

## Entrée canonique v6

`knowledge-base/corpus/history.kristal-state.json`

Les autres JSON sont des vues de travail dérivées et plus faciles à interroger.

## Validation

```bash
python knowledge-base/tools/validate.py
```

## Requêtes rapides

```bash
python knowledge-base/tools/query.py event event:magna-carta-1215
python knowledge-base/tools/query.py causes event:apollo11-moon-landing-1969
python knowledge-base/tools/query.py consequences event:web-public-domain-1993
python knowledge-base/tools/query.py timeline 1940 1970
```

## Portée v0.1.0

Cette livraison est un **socle mondial diachronique de validation du modèle**, pas une histoire universelle complète. `coverage.json` rend les zones encore absentes explicites afin que l'enrichissement reste contrôlé.
