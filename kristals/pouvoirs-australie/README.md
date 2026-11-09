# Kristal — Qui décide quoi? — Australie

Version **0.1.0** — état juridique de référence **au 2 octobre 2026**.

Ce Kristal répond aux questions: qui décide, qui peut agir, qui ne peut pas agir seul, qui bloque, qui contrôle et quelle norme prévaut.

## Portée

Le modèle couvre l'ordre juridique **australien national et fédéral** : Constitution; Parlement du Commonwealth; Gouverneur général; Premier ministre, Cabinet et ministres; pouvoirs du Commonwealth et pouvoirs résiduels des États; territoires autonomes; gouvernements locaux; tribunaux et High Court; contrôle administratif et juridictionnel; audit et ombudsman; éducation; et **interface nationale** avec les traités.

Il **n'encode pas le droit international substantiel**. Les traités comme normes internationales, la coutume, le jus cogens, l'ONU, le droit humanitaire, les droits humains internationaux, le droit de la mer, le commerce international et la responsabilité internationale relèvent du Kristal supranational/international distinct. Ici, seules les règles australiennes expliquant **qui négocie, qui approuve, comment le Parlement contrôle et comment le droit interne est modifié** sont conservées.

Il n'encode pas les titulaires actuels des fonctions politiques.

## Invariants

- `OFFICE != TITULAIRE`
- `ÉLECTION != POUVOIR ILLIMITÉ`
- `COMMONWEALTH != ÉTATS`
- `ÉTAT != TERRITOIRE`
- `GOUVERNEMENT LOCAL != ÉTAT FÉDÉRÉ`
- `INFLUENCE POLITIQUE != AUTORITÉ JURIDIQUE`
- `POLITIQUE GOUVERNEMENTALE != LOI`
- `INSTRUMENT DÉLÉGUÉ != LOI PRIMAIRE`
- `CONTRÔLE AU FOND != CONTRÔLE JURIDICTIONNEL`
- `INTERFACE INTERNATIONALE != CORPUS INTERNATIONAL`
- `DROIT AUSTRALIEN != POLITIQUE COMMERCIALE KRISTAL FARMS`

## Particularités australiennes

Le Commonwealth possède des compétences constitutionnelles attribuées; les États conservent les pouvoirs résiduels. Les territoires autonomes tirent leur autonomie de lois fédérales prises dans le cadre constitutionnel. Les conseils locaux tirent leurs pouvoirs des États ou du Northern Territory. La responsabilité opérationnelle de l'enseignement scolaire appartient principalement aux États et territoires, tandis que le Commonwealth joue un rôle majeur de financement et de politique nationale.

## Fichiers principaux

- `knowledge-base/corpus/pouvoirs-australie.kristal-state.json`
- `knowledge-base/sources/legal_power_matrix.json`
- `knowledge-base/sources/source_catalog.json`
- `knowledge-base/documentation/QUICK_MAP.md`
- `knowledge-base/documentation/DOMAIN_MODEL.md`
- `knowledge-base/documentation/INVARIANTS.md`
- `knowledge-base/documentation/COVERAGE.md`

## Statut

Base structurée de référence, non avis juridique. Pour une question dépendant d'un État ou territoire particulier, revalider la Constitution, la loi ou le règlement de cette juridiction.
