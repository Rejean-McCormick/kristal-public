# Kristal-Pharmacology

**Version 1.0.0 — Kristal Standard 6.0**

Kristal-Pharmacology est un corpus statique, traçable et généraliste de **pharmacologie**. Son axe principal est :

`substance → cible → mécanisme → dose/exposition → effet → risque`

Le parcours est une vue conceptuelle. Le corpus distingue explicitement **dose administrée**, **exposition systémique**, **engagement de cible**, **effet pharmacodynamique** et **risque**.

## Canonique

- `knowledge-base/corpus/pharmacology.kristal-state.json` — état Kristal v6 canonique
- `knowledge-base/corpus/referents.json` — registre des concepts
- `knowledge-base/sources/source-catalog.json` — catalogue de sources
- `knowledge-base/corpus/pharmacology-chain-graph.json` — graphe dérivé complet
- `knowledge-base/corpus/pk-map.json` — projection PK/exposition
- `knowledge-base/corpus/pd-map.json` — projection cibles/mécanismes/effets
- `knowledge-base/corpus/risk-map.json` — projection sécurité/interactions
- `knowledge-base/tools/validate.py` — validation locale

## Distinctions structurantes

- **dose ≠ concentration ≠ exposition ≠ effet**;
- **affinité ≠ puissance ≠ efficacité**;
- **événement indésirable ≠ causalité démontrée**;
- une interaction peut être **PK**, **PD**, ou combiner les deux;
- la variabilité interindividuelle est représentée séparément de l’effet moyen.

## Frontière clinique

Ce Kristal n’est pas un guide de prescription. Il ne contient ni dose thérapeutique spécifique, ni recommandation patient-spécifique, ni algorithme de traitement. Ces usages appartiennent à des corpus cliniques contextualisés et révisables.

### Taille

- Référents : **143**
- Assertions : **196**
- Sources : **19**
