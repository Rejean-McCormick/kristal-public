# Kristal-HomeCare

**Kristal-HomeCare 2.0.0** est un Kristal longitudinal, fonctionnel et diagnostique de la maison réelle. Il combine un graphe physique, des fonctions, des chemins de transfert, des modes de panne génériques, un ledger temporel append-only, des preuves sourcées et des projections reconstruisibles.

## Primitives fortes

`Asset + Component + Interface + Function + FunctionalPath + FailureMode + Observation + Evidence + Event + Requirement`

```text
OBJECT / ASSET
   │ performs
   ▼
FUNCTION
   │ realized by
   ▼
FUNCTIONAL PATH ──► components / interfaces / flows
   │
   ├─ can be affected by ──► FAILURE MODES
   │                            │
   │                            └─ may produce ──► OBSERVABLE PHENOMENA
   │
   └─ can be discriminated by ─► TEST DEFINITIONS / MEASUREMENTS
                                      │
                                      └─ safety / qualification gates
```

## Densité v2

Le corpus comprend des taxonomies enrichies de systèmes, actifs, composants, fonctions, flux, modes de panne, phénomènes observables, mesures, tests, actions d’entretien, dangers, qualifications, documents, spatialité et packs métier.

Les éléments génériques non issus d’une source externe sont explicitement marqués `editorial_seed` ou `editorial_seed_requires_source`. Ils servent à structurer le raisonnement; ils ne constituent pas des périodicités universelles, exigences réglementaires, statistiques de panne ni procédures de travail.

## Outils

```bash
cd knowledge-base
python tools/build.py
python tools/validate.py
python tools/selftest.py
python tools/catalog.py --stats
python tools/catalog.py --asset sump_pump
python tools/reason.py --phenomenon no_function --asset-type sump_pump
python tools/query.py --demo --overview
python tools/package.py
python tools/validate.py --verify-manifest
```

`examples/demo-home/` est entièrement synthétique.
