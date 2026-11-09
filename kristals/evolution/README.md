# Kristal Evolution 1.0.0

Kristal Evolution est un corpus statique de **biologie évolutive fondamentale**. Son axe principal est :

**variation → transmission / descendance → tri différentiel ou processus stochastiques → changement des populations → lignées → divergence**

Le corpus décrit l’évolution comme un changement intergénérationnel de populations et de lignées. La sélection naturelle y occupe une place centrale, mais elle n’est pas confondue avec l’évolution entière : mutation, dérive génétique et flux génique sont représentés explicitement.

## Périmètre

Sept axes canoniques : **variation, sélection, descendance, populations, pressions, lignées, divergence**.

Les concepts de génome, niche écologique, développement, espèce, taxon et registre fossile sont inclus seulement comme interfaces avec d’autres Kristals. Ce corpus n’est ni un manuel complet de génétique, ni une taxonomie du vivant, ni une base d’espèces, ni une encyclopédie d’écologie ou de paléontologie.

## État

- Kristal Standard **v6** (`kristal_state`)
- corpus **1.0.0**
- 193 référents
- 521 assertions atomiques
- 9 sources de référence / synthèse
- validation JSON Schema + audit de graphe + manifeste SHA-256

## Fichiers principaux

- `knowledge-base/corpus/evolution.kristal-state.json` — état canonique v6
- `knowledge-base/corpus/evolution.referent-registry.json` — identités stables
- `knowledge-base/corpus/evolutionary-process-model.json` — mécanismes fondamentaux
- `knowledge-base/corpus/selection-model.json` — sémantique de sélection et fitness
- `knowledge-base/corpus/divergence-model.json` — isolement, divergence et spéciation
- `knowledge-base/corpus/lineage-model.json` — ascendance et représentations phylogénétiques
- `knowledge-base/corpus/domain-coverage.json` — couverture et exclusions
- `knowledge-base/sources/source-catalog.json` — provenance documentaire

## Invariants critiques

1. **Évolution ≠ sélection naturelle.** Dérive, flux génique et mutation peuvent modifier les populations sans constituer de sélection adaptative.
2. **Individu ≠ population.** Un changement au cours de la vie d’un individu n’est pas, à lui seul, une évolution de population.
3. **Variation phénotypique ≠ variation héréditaire.** La plasticité et l’environnement peuvent produire des différences non transmissibles.
4. **Fitness ≠ force, santé ou perfection.** Elle exprime une contribution reproductive dans un contexte défini.
5. **Pression de sélection ≠ intention.** L’environnement ne vise aucun état futur.
6. **Fixation ≠ adaptation.** Une variante peut se fixer par dérive.
7. **Adaptation ≠ progrès universel.** Elle est locale au contexte et comporte souvent des compromis.
8. **Divergence ≠ spéciation automatique.** Des populations peuvent diverger sans franchir un critère d’espèce.
9. **Arbre phylogénétique ≠ histoire directement observée.** C’est une représentation d’une hypothèse sur les relations.
10. **Lignée contemporaine A ≠ ancêtre de lignée contemporaine B** simplement parce qu’elles occupent des positions différentes dans un arbre.
11. **Héritabilité ≠ déterminisme génétique individuel.** C’est une statistique de population dépendante du contexte.
12. **Similarité ≠ homologie.** Une convergence peut produire des caractères semblables sans origine directe commune du caractère.

## Validation

```bash
cd knowledge-base
python tools/validate.py
python tools/audit_graph.py
python tools/query.py --topic divergence
```
