# Kristal-Physics v0.2.0

Kristal-Physics est un **graphe épistémique multiplexe, multi-échelle et centré sur l’état physique**, construit sur Kristal Standard v6.

Son invariant architectural central est :

```text
PhysicalSystem != PhysicalState

PhysicalSystem
    │ has_state
    ▼
PhysicalState(t0)
    │ evolves_under / undergoes_process
    ▼
PhysicalState(t1)
```

La mesure reste un plan distinct :

```text
PhysicalState → MeasurementProcess → Observation/Result
                         │
                         └─ conditions + unit/reference + uncertainty + provenance
```

Et le formalisme reste distinct du monde physique :

```text
PhysicalLaw / PhysicalModel != Equation / MathematicalRepresentation
MathematicalDerivation != EmpiricalEvidence
Prediction != Observation
```

## v0.2.0 — noyau de référence massivement enrichi

La v0.2.0 étend la fondation à plus de trois mille assertions canoniques couvrant : mécanique et gravitation, fluides et milieux continus, oscillations/ondes/acoustique, thermodynamique et statistique, électromagnétisme, optique, relativité, quantique et atomique, matière condensée et plasmas, nucléaire et particules, astrophysique et cosmologie.

Le corpus éditorial comprend désormais des catalogues séparés pour les grandeurs/unités, les lois et modèles, les entités partagées, les relations transversales et les expériences de référence. Les branches disciplinaires restent des **projections non exclusives**, jamais des racines ontologiques.

## Démarrage

```bash
cd knowledge-base
python tools/build.py
python tools/build_manifest.py
python tools/validate.py
python tools/query.py --predicate physics:has_mathematical_representation
```

Les fichiers sous `sources/` sont les sources éditoriales du paquet. Les fichiers sous `corpus/` sont reconstruisibles.
