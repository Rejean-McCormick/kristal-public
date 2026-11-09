# Kristal-AI

**Version 1.0.0 — Kristal Standard 6.0**

Kristal-AI est un corpus statique, traçable et généraliste sur les systèmes d’**intelligence artificielle**. Son expression de navigation principale est :

`données → représentation → modèle → apprentissage → inférence → évaluation`

Le pipeline est une **vue de navigation**, pas une hypothèse de stricte linéarité. L’évaluation peut rétroagir sur les données, le modèle et l’apprentissage; des systèmes symboliques peuvent utiliser peu ou pas d’apprentissage statistique; des systèmes complets peuvent combiner modèles, récupération, outils, règles et supervision humaine.

## Distinctions structurantes

- **donnée ≠ représentation ≠ paramètre de modèle** ;
- **modèle ≠ système d’IA complet** ;
- **apprentissage ≠ inférence** ;
- **score de confiance ≠ probabilité calibrée** ;
- **performance moyenne ≠ robustesse ≠ équité ≠ fiabilité** ;
- **évaluation interne ≠ validation externe** ;
- **génération plausible ≠ vérité factuelle** ;
- **trace de raisonnement exposée ≠ preuve du mécanisme causal interne**.

## Canonique

- `knowledge-base/corpus/ai.kristal-state.json` — état v6 canonique
- `knowledge-base/corpus/referents.json` — registre des concepts
- `knowledge-base/sources/source-catalog.json` — catalogue des sources
- `knowledge-base/corpus/ai-lifecycle-graph.json` — graphe complet
- projections : données, représentation, modèle, apprentissage, inférence, évaluation, transversal

### Taille

- Référents : **179**
- Assertions : **360**
- Sources : **20**
