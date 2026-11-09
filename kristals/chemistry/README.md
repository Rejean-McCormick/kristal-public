# Kristal-Chemistry — paquet consolidé

Kristal-Chemistry représente la chimie comme un **graphe épistémique multi-échelle d’entités, d’états, d’interactions et de transformations**.

Le canon utilise **Kristal Standard 6.0 `kristal_state`** pour les assertions. L’identité des référents reste dans un registre séparé. Les classifications — tableau périodique, familles chimiques, familles de réactions — sont des **facettes/projections**, jamais des substituts à l’identité.

```text
Kristal-Chemistry/
├── knowledge-base/
│   ├── corpus/          # canon construit + projections dérivées
│   ├── documentation/   # architecture, invariants, modèles
│   ├── examples/
│   ├── integration/
│   ├── profiles/
│   ├── schemas/
│   ├── sources/         # sources éditables de vérité
│   └── tools/           # build / validate / query / package / selftest
└── external-source-library/
```

Principe central :

```text
ENTITY ↔ STATE ↔ PROCESS
          │
          ├─ conditions
          ├─ thermodynamics
          ├─ kinetics
          └─ observations
```

Les réactions sont des processus réifiés avec participants stœchiométriques : le corpus peut représenter des transformations n-aires, réversibles et cycliques sans imposer un DAG.

## v0.2.0

La v0.2 élargit le noyau aux ponts structurants de la chimie générale :

- particules subatomiques minimales (électron, proton, neutron) ;
- facettes des 118 éléments : blocs `s/p/d/f` et grandes familles périodiques ;
- espèces et substances courantes ;
- familles organiques et groupes fonctionnels ;
- acide–base et couples conjugués ;
- oxydoréduction avec demi-réactions et électron explicite ;
- équilibres, cinétique, activation et catalyse comme concepts distincts ;
- réactions de combustion, synthèse, décomposition, précipitation, substitution, estérification et hydrogénation ;
- changements de phase séparés des réactions chimiques ;
- techniques analytiques et grandeurs mesurées ;
- seconde occurrence expérimentale synthétique pour exercer `technique ≠ propriété ≠ mesure`.
