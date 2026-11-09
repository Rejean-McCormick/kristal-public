# Kristal ElectricalEngineering v1.0.0

Kristal v6 statique de référence sur les abstractions fondamentales du génie électrique.

## Noyau

`source → circuit → charge`

avec les grandeurs transversales : **tension, courant, puissance, signal**.

Le corpus sépare trois plans qui sont souvent confondus :

1. **physique** — charge, porteurs, champ, énergie ;
2. **circuit** — source, nœud, branche, maille, résistance, stockage, puissance ;
3. **information** — forme d’onde, signal analogique/numérique, fréquence, bruit, bande passante.

## Garde-fous sémantiques principaux

- charge ≠ courant ;
- courant ≠ puissance ;
- tension = différence de potentiel entre deux points ;
- sens conventionnel du courant ≠ nécessairement sens des électrons ;
- source réelle ≠ source idéale ;
- le courant n’est pas « consommé » par une charge ;
- masse (`ground`) ≠ nécessairement Terre ;
- circuit ouvert ≠ tension nulle ;
- court-circuit ≠ courant réellement infini ;
- loi d’Ohm ≠ loi constitutive universelle de tout composant ;
- signal ≠ énergie ou puissance ;
- AC ≠ signal ; un niveau DC peut porter de l’information ;
- signal numérique ≠ grandeur physique parfaitement discrète ;
- KCL/KVL sont des abstractions de circuit avec domaine de validité.

## Frontière

Inclus : circuits concentrés fondamentaux, sources, tension/courant, réseaux résistifs, puissance, condensateur/inducteur au niveau conceptuel, transitoires, AC de base, signaux et mesure.

Exclus : théorie de champ détaillée, RF/lignes de transmission, physique des semi-conducteurs, électronique analogique/digitale approfondie, machines, réseaux électriques, électronique de puissance, contrôle, normes d’installation et sécurité électrique.

## Contenu

- `corpus/electrical-engineering.kristal-state.json` — état canonique v6
- `corpus/referents.json` — registre conceptuel FR/EN
- `sources/` — catalogue et registre d’évidence
- `profiles/` — profil de navigation
- `documentation/` — architecture, frontière et garde-fous
- `tools/validate.py` — validation locale

Les sources externes servent à établir la provenance des assertions; leur contenu n’est pas incorporé textuellement dans le corpus.
