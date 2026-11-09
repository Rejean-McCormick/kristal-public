# Kristal-Bible v1.2.0

**Human & Spiritual Systems Graph** — Kristal biblique polymorphe, multi-graphe, multi-échelle, polyphonique et désormais entièrement traversable.

## Architecture

Kristal-Bible sépare six plans couplés :

1. **Témoins source** — WLC hébreu/araméen, LXX grecque, NT grec historique;
2. **Corpus** — œuvres et localisateurs;
3. **Observations textuelles** — descriptions proches des passages;
4. **Modèles humains** — mécanismes, dynamiques, émotions, désir, pouvoir, transformations;
5. **Polyphonie** — voix, tensions, contre-modèles et stress-tests;
6. **Herméneutique** — lectures symboliques/spirituelles explicitement marquées.

Le noyau reste : **référent → assertion → preuve/provenance → projection**.

## v1.2 — connexions internes

La base n’est plus seulement une collection de modèles : tous les plans sont connectés dans un graphe interne unique.

- 162 KnowledgeUnits;
- 73 observations textuelles;
- 73 œuvres;
- 4 témoins source;
- 1 412 relations internes;
- 1 067 relations porteuses de sens/provenance;
- 345 affinités de navigation dérivées et non canoniques;
- 3 778 assertions Kristal v5;
- 312 nœuds dans une seule composante connectée;
- 10 parcours transversaux validés.

Les relations calculées `derived_navigation` ne deviennent jamais des assertions canoniques. Voir `knowledge-base/documentation/INTERNAL_CONNECTIONS.md`.

## Rebuild / validation

```bash
cd knowledge-base
python tools/build.py
python tools/validate.py
python tools/audit.py
```

`build.py` reconstruit d’abord les connexions via `tools/connect.py`, puis compile l’état Kristal et toutes les projections.

## Exploration

```bash
python tools/query.py --node motif:heart --neighbors --depth 1 --include-navigation
python tools/query.py --node desire:control --path-to power:servant-leadership
```

## Invariants centraux

- passage ≠ interprétation;
- description ≠ prescription;
- voix locale ≠ position globale;
- symbolique ≠ assertion historique;
- analogue psychologique ≠ intention d’auteur;
- densité ≠ couverture ≠ certitude ≠ importance;
- connexion sémantique ≠ affinité de navigation;
- chemin de graphe ≠ chaîne causale biblique;
- projection dérivée ≠ source de vérité.
