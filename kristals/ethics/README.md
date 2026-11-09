# Kristal-Ethics v1.0.0

**Domaine :** éthique — situation → agents → valeurs/devoirs → options → arguments → conséquences  
**Statut :** `working`  
**Snapshot éditorial :** 2026-10-02  
**Langue principale :** français

## Axe canonique

`situation → agents → valeurs/devoirs → options → arguments → conséquences`

L’axe est un **ordre d’analyse**, pas une mécanique produisant automatiquement un verdict. Le Kristal conserve les désaccords entre valeurs, arguments et cadres normatifs.

## Principe central

**Ethics ne choisit pas à la place de l’agent moral.** Il représente les éléments pertinents du raisonnement : qui est affecté, quelles valeurs et obligations sont engagées, quelles options existent, quels arguments les soutiennent ou les contestent, et quelles conséquences sont plausibles.

## Garde-fous

- `fait descriptif ≠ conclusion normative`
- `légalité ≠ moralité`
- `préférence ≠ valeur morale`
- `risque prévu ≠ dommage réalisé`
- `personne affectée ≠ décideur autonome`
- `argument ≠ verdict`
- `désaccord ≠ erreur de données`
- aucune théorie éthique n’est classée ou pondérée globalement
- aucune somme numérique de valeurs ne produit une « bonne réponse »

## Contenu

Voir `knowledge-base/corpus/index.json`, `corpus/ethics.kristal-state.json`, `corpus/ethics-projections.json` et `sources/source_catalog.json`.

## Validation

```bash
cd knowledge-base
python tools/build.py
python tools/validate.py
python -m unittest tests/test_model.py
```

Le corpus est reconstruit de façon déterministe à partir de `sources/*.json`.
