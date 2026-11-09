# Kristal-Recipes 2.1.0 — atlas culinaire computationnel

Kristal-Recipes représente les recettes comme des **programmes de transformation de matière** plutôt que comme des fiches texte.

Le noyau canonique sépare :

1. `RecipeFamily` — identité culinaire conceptuelle;
2. `RecipeVariant` — formulation versionnée;
3. `RecipeSourceInstance` — occurrence documentaire importée;
4. `PreparationEvent` — exécution réelle ou synthétique d'une variante.

Chaque variante contient un **DAG procédural** : ingrédients → états → opérations → états → sorties. Les opérations peuvent porter mécanismes, conditions, critères de fin et points de contrôle. Les projections reconstruisibles ajoutent classification facettée, fingerprints multi-axes, espaces de variantes, transitions, rôles fonctionnels, substitutions contextuelles, dépannage, profils sensoriels et agrégats d'exécution.

## Frontière épistémique

Le seed fourni sert à tester la structure et n'est pas une autorité culinaire. Une similarité n'est pas une identité; une substitution n'est pas une équivalence; une cause d'échec est une hypothèse; une observation de préparation n'écrase jamais la recette canonique. Les propriétés de sécurité alimentaire ne sont pas déduites depuis des métadonnées non sourcées.

## Commandes

```bash
python knowledge-base/tools/build.py
python knowledge-base/tools/validate.py
python knowledge-base/tools/query.py --stats
python knowledge-base/tools/query.py --family generic_yeast_bread
python knowledge-base/tools/query.py --similar generic_yeast_bread.v1
python knowledge-base/tools/query.py --substitutions butter
python knowledge-base/tools/query.py --troubleshoot generic_emulsified_sauce
python knowledge-base/tools/query.py --ingredients wheat_flour,water --techniques ferment,bake
```


## Acquisition externe v2.1

Le paquet inclut maintenant `source-manager/`, `knowledge-base/sources/source-catalog/` et une `external-source-library/` sidecar sur le même modèle que les autres Kristals. `python source-manager/source_store.py fetch-dataset forkrecipe` capture le corpus ForkRecipe sans modifier le canon.


## Contrat canonique / portable v6

Le canon métier de Kristal-Recipes est **domain-native** et est verrouillé par `knowledge-base/canonical-payload.manifest.json`. Le fichier `.kristal/v8/portable-state.kristal-state.json` est une **enveloppe/projection portable dérivée** : il transporte les frontières, identités et assertions transversales nécessaires à l’interopérabilité, mais ne prétend pas remplacer le `RecipeVariant` ni son `procedure` DAG comme source métier. Toute reconstruction doit repartir du payload canonique déclaré et vérifié par hash.
