# Kristal-Data v1.0.0

**Schéma → valeur → transformation → provenance → qualité → requête.**

Kristal-Data décrit les données structurées comme des valeurs interprétées sous un schéma, transformées par des activités traçables, évaluées selon des métriques de qualité explicites et interrogées par des opérations de requête.

## Noyau conceptuel

```text
Schéma ──contraint/décrit──> Instance / Valeur
                                  │
                            Transformation
                                  │
                         Sortie dérivée + provenance
                                  │
                     Qualité = dimension + métrique + mesure
                                  │
                               Requête
```

## Distinctions obligatoires

- schéma ≠ données;
- forme lexicale ≠ valeur;
- `null` ≠ valeur manquante ≠ chaîne vide ≠ `0` ≠ `false`;
- validation de schéma ≠ exactitude du monde réel;
- transformation ≠ provenance de la transformation;
- lignage ≠ provenance complète;
- dimension de qualité ≠ métrique ≠ mesure;
- requête ≠ mutation de la source;
- résultat de requête ≠ jeu de données source.

## Portée v1

- modèles scalaire, record, séquence, table, relationnel, document, graphe, clé-valeur, série temporelle, multidimensionnel et flux;
- schémas, types, champs, cardinalités, clés, références, unités, contraintes et versions;
- formes de valeurs et sémantiques d’absence;
- transformations courantes : parse, cast, filtre, projection, jointure, agrégation, reshape, enrichissement, imputation, etc.;
- provenance alignée conceptuellement sur W3C PROV;
- qualité alignée sur DQV avec dimensions, métriques et mesures séparées;
- opérations de requête inspirées de l’algèbre SPARQL et généralisées aux données structurées;
- profils de lecture `reference`, `lineage` et `query`.

## Frontière volontaire

Kristal-Data n’est pas un moteur SQL, une base de données, un entrepôt, un système distribué, un catalogue de formats de fichiers, un cours d’algorithmes, ni un système de gouvernance ou de confidentialité. Ces couches peuvent être portées par Computing, Databases, Security/Privacy ou Governance sans modifier ce noyau.

## Reproductibilité

```bash
python knowledge-base/tools/build.py
python knowledge-base/tools/validate.py
python knowledge-base/tools/query.py --concept provenance
```

Les sources distantes sont cataloguées par métadonnées. Les artefacts canoniques sont autonomes, statiques, hashés et reconstruits déterministiquement.
