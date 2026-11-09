# Kristal-VehiculeDiag

**Kristal-VehiculeDiag v2.0.1** est un Kristal causal, probabiliste et testable de diagnostic automobile. Son objet canonique n’est pas une table `symptôme → pièce`, mais le **véhicule comme réseau multiplexe de chemins fonctionnels observables**.

Le graphe descend à la granularité `composant → port/borne → arête → port/borne`. Une même pièce peut participer simultanément aux couches électrique, masse, signal, contrôle, réseau, fluide, hydraulique, air, mécanique, thermique et fonctionnelle.


## Kristal v9

Le repo expose maintenant une couche **Kristal v9 Semantic State Architecture** sous `.kristal/v9/`. La migration ne transforme pas le modèle automobile en liste universelle d’assertions : le **modèle causal multiplexe natif** reste la forme métier, tandis que l’état portable v6 devient un overlay épistémique/interopérable.

Frontières v9 :

- `knowledge-base/sources/**` — sources éditoriales autoritaires du modèle natif;
- `.kristal/v9/logical/reference-model.logical-artifact.json` — snapshot logique normalisé du modèle multiplexe;
- `.kristal/v9/logical/epistemic-overlay.logical-artifact.json` — overlay épistémique compatible v6;
- `knowledge-base/corpus/graph.json`, `index.json`, projections diagnostiques et indexes v8 — **Runtime / Read Models reconstruisibles**;
- `.kristal/v9/states/current.state-snapshot.json` — composition logique immuable active.

```text
DOMAIN-NATIVE SHAPE != PORTABLE PROJECTION
READ MODEL != CANONICAL STATE
INDEX != SOURCE OF TRUTH
```

Reconstruction :

```bash
cd knowledge-base
python tools/build.py
python tools/build_v9.py
python tools/validate_v9.py
```

Voir `knowledge-base/documentation/KRISTAL_V9_ARCHITECTURE.md`.

## Ce que v2.0 ajoute

- 9 circuits démonstrateurs couvrant éclairage, demande de couple, démarrage, charge, allumage, refroidissement, CAN, freinage et HVAC;
- 81 composants, 161 ports, 152 connexions, 26 chemins fonctionnels et 71 points de test;
- 59 modes de panne instanciés + 30 archétypes génériques de panne;
- 51 archétypes de composants et 33 archétypes de systèmes;
- 63 symptômes hiérarchisés, sémantique DTC générique et règles de sécurité;
- mesures catégorielles et numériques conditionnées par état opératoire;
- pannes comme perturbations bloquantes ou dégradées du graphe;
- mise à jour bayésienne approximative et optimisation `gain d’information / coût pratique`;
- coût des tests incluant temps, accès, outils, invasivité, risque, dangers et setups mutualisés;
- planification à profondeur 2;
- moteur de **diagnostic closure** qui cherche automatiquement les pannes non observables, les paires indiscernables et les chemins sans test;
- outils de simulation d’une panne, comparaison de chemins, explication d’un test et génération de candidats;
- pipeline de cas terrain et apprentissage de priors en projection seulement.

## Invariants

- `DTC != diagnostic`
- `symptôme != cause`
- `mesure != vérité cachée`
- `réparation réussie != preuve suffisante de cause racine`
- `test optimal != panne la plus probable`
- `absence de DTC != absence de panne`
- `topologie de référence != fréquence terrain`
- une connexion peut être une cible de panne de premier ordre;
- un cas réel ne modifie jamais automatiquement le graphe de référence;
- toute assertion spécifique à un véhicule doit porter applicabilité et provenance;
- un test dangereux ne devient pas acceptable parce qu’il a un fort gain d’information.

## Démonstrateurs

Les données incluses sont **illustratives** et ne correspondent à aucun véhicule réel. Elles servent à tester l’architecture, pas à fournir une procédure de réparation.

Systèmes inclus :

1. feux gauche/droit;
2. accélérateur → ECU → injection → moteur → transmission → roue;
3. démarrage / lancement;
4. charge alternateur;
5. allumage / combustion;
6. refroidissement moteur;
7. réseau CAN simplifié;
8. freinage hydraulique;
9. soufflerie HVAC.

## Démarrage

```bash
cd knowledge-base
python tools/build.py
python tools/coverage.py
python tools/validate.py
python -m unittest discover -s tests -v
python tools/run_examples.py
```

Exemples utiles :

```bash
python tools/diagnose.py examples/demo_no_crank.case.json
python tools/trace_path.py starter_power_path --state starter_cranking
python tools/compare_paths.py lamp_left_power_return lamp_right_power_return
python tools/simulate_failure.py fm_starter_ground_high_resistance --state starter_cranking
python tools/explain_test.py examples/demo_no_crank.case.json tp_starter_ground_drop
python tools/suggest_candidates.py --symptom no_crank --path starter_power_path
python tools/coverage.py
```

Le rapport de fermeture diagnostique est généré dans `corpus/quality/coverage-report.md`.

## Local Kristal 3.2.2

Cette copie est enveloppée selon `kristal.local-workspace/3.2.0` (Authoring Kit 3.2.2). Le modèle métier et les Logical Commitments v9 historiques sont conservés.

- `kristal.workspace.json` — identité, frontières, lifecycle et baseline v10;
- `canon/state.index.json` — enregistrement des deux Logical Artifacts v9;
- `canon/domain/reference-model.json` — payload canonique du modèle métier;
- `canon/epistemic/epistemic-overlay.json` — payload canonique de l’overlay épistémique;
- `sources/source-catalog.json` — catalogue de sources au format Local Kristal 2.0;
- `docs/00_*` à `docs/07_*` — documentation normative de la frontière, du modèle, de l’autorité, des dérivés et du lifecycle.

La normalisation ne configure pas GitHub, ne publie pas et n’active pas d’état.

