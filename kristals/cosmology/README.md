# Kristal-Cosmology v1.0.0

**Univers à grande échelle**

Corpus statique et reconstruisible organisé par cinq axes :

`contenu → géométrie → expansion → structure → époque cosmique`

Cette flèche est une **projection de navigation**, pas une causalité universelle. En relativité générale, contenu, géométrie et expansion sont couplés; les structures croissent dans cet arrière-plan et sont observées à différentes époques.

## Architecture épistémique

Le corpus ajoute quatre axes auxiliaires indispensables : `modèle`, `observable`, `paramètre`, `incertitude`. Une valeur numérique cosmologique ne peut donc apparaître sans **source + jeu de données + modèle**.

Le modèle de référence ΛCDM est représenté comme un **baseline scientifique**, non comme une ontologie ultime. La matière noire et l’énergie sombre restent des composantes inférées dont la microphysique n’est pas établie. Inflation et réchauffement sont explicitement marqués comme scénarios/cadres candidats. Les résultats DESI récents sur une possible évolution de l’énergie sombre sont encodés comme **indices dépendants des combinaisons de données**, pas comme découverte.

## Validation

```bash
cd knowledge-base
python tools/build.py
python tools/validate.py
python -m unittest discover -s tests -v
```

Statut : `working` — corpus scientifique sourcé et validé structurellement; les contraintes observationnelles restent dépendantes des modèles et snapshots de données.
