# Kristal Forestry 1.0.0

Kristal Forestry est un corpus statique de **dynamique des peuplements forestiers et de sylviculture fondamentale**. Son axe principal est :

**peuplement(t) → composition / structure → croissance + recrutement + mortalité → perturbation ou intervention → nouvel état du peuplement**

Le corpus décrit un peuplement comme un système temporel. Une forêt n’est donc pas réduite à une classe d’âge ou à un inventaire instantané : elle est représentée par des états successifs, des flux biologiques, des perturbations, des héritages et des interventions planifiées.

## Périmètre

Neuf axes canoniques : **peuplement, composition, structure, croissance, régénération, perturbation, succession, intervention, suivi**.

La taxonomie complète des arbres, les sols, le climat, la biodiversité, le carbone, le droit, l’économie et la géométrie paysagère sont présents uniquement comme interfaces vers d’autres Kristals.

## État

- Kristal Standard **v6** (`kristal_state`)
- corpus **1.0.0**
- 212 référents
- 596 assertions atomiques
- 9 sources de référence / synthèse
- validation JSON Schema + audit de graphe + manifeste SHA-256

## Fichiers principaux

- `knowledge-base/corpus/forestry.kristal-state.json` — état canonique v6
- `knowledge-base/corpus/forestry.referent-registry.json` — identités stables
- `knowledge-base/corpus/stand-transition-model.json` — états et transitions temporelles
- `knowledge-base/corpus/growth-regeneration-model.json` — stocks, croissance, recrutement et mortalité
- `knowledge-base/corpus/disturbance-model.json` — événement, régime, sévérité, intensité et héritages
- `knowledge-base/corpus/silviculture-model.json` — prescription, traitement et boucle adaptative
- `knowledge-base/corpus/monitoring-model.json` — mesures répétées et suivi
- `knowledge-base/corpus/domain-coverage.json` — couverture et exclusions
- `knowledge-base/sources/source-catalog.json` — provenance documentaire

## Invariants critiques

1. **Peuplement ≠ objet intemporel.** Un peuplement est décrit à une échelle et un moment donnés.
2. **État ≠ trajectoire.** Deux états semblables peuvent résulter d’histoires différentes et évoluer différemment.
3. **Composition ≠ structure.** Les mêmes essences peuvent former des structures très différentes.
4. **Âge du peuplement ≠ âge de chaque arbre.** La convention d’âge doit être explicite.
5. **Dominance ≠ simple présence.** Elle dépend de la métrique choisie.
6. **Densité ≠ stocking/degré de peuplement.** Le second est relatif à une référence.
7. **Surface terrière ≠ volume.** Ce sont des grandeurs différentes.
8. **Perturbation ≠ dégradation.** Une perturbation peut faire partie du fonctionnement normal d’un système forestier.
9. **Intensité ≠ sévérité.** L’une caractérise le phénomène, l’autre ses effets.
10. **Perturbation de remplacement ≠ déboisement.** La régénération peut maintenir l’usage forestier du territoire.
11. **Succession ≠ marche obligatoire vers un climax unique.** Plusieurs trajectoires sont possibles.
12. **Rétablissement ≠ retour exact à l’état antérieur.**
13. **Traitement ≠ effet garanti.** La réponse dépend du site, du peuplement, du climat, des perturbations et de l’exécution.
14. **Après traitement ≠ causé par le traitement.** Le suivi temporel seul ne démontre pas la causalité.
15. **Prescription ≠ recette universelle.** Toute prescription opérationnelle exige un diagnostic et une validation locale.
16. **Vieille forêt ≠ âge universel.** Les critères dépendent du type forestier et du référentiel.
17. **Mesure ≠ vérité sans incertitude.** Les seuils, méthodes, plans d’échantillonnage et erreurs doivent rester attachés aux valeurs.
18. **Télédétection ≠ observation directe de toutes les propriétés.** Elle nécessite interprétation et souvent validation terrain.

## Validation

```bash
cd knowledge-base
python tools/validate.py
python tools/audit_graph.py
python tools/query.py --topic disturbance
```

## Kristal v9

Ce repo est migré vers **Kristal 9.0.0-draft.1 — Semantic State Architecture** sans supprimer les surfaces v6/v8 existantes.

- canon v9 : le state v6 canonique `knowledge-base/corpus/forestry.kristal-state.json`;
- snapshot logique immuable : `.kristal/v9/state-snapshot.json`;
- matérialisation(s) : `.kristal/v9/materialization.*.json`;
- projection portable v6 : conservée sous `.kristal/v8/portable-state.kristal-state.json` et explicitement dérivée;
- indexes/read models v8 : restent dérivés et reconstruisibles;
- identité logique v9 : séparée des digests physiques des fichiers.

Voir `.kristal/v9/README.md` et `V9-MIGRATION.md`.
