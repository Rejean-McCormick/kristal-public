# Kristal-Metrology v0.1.0

Corpus statique et versionné de référence sur la chaîne **grandeur → unité → instrument/système → mesure → incertitude → traçabilité**.

## Noyau conceptuel

`mesurande + unité + conditions → système/procédure → indication → modèle/corrections → résultat ± incertitude → chaîne de traçabilité`

## Garde-fous

- valeur mesurée ≠ valeur vraie ;
- erreur ≠ incertitude ;
- fidélité/précision ≠ exactitude ;
- résolution ≠ exactitude ;
- étalonnage ≠ ajustage ;
- Type A / Type B = méthodes d’évaluation de l’incertitude, pas types d’erreurs ;
- un certificat d’étalonnage ne rend pas automatiquement tous les résultats « traçables » ;
- la traçabilité métrologique est une propriété du **résultat de mesure** ;
- chaque maillon d’une chaîne de traçabilité contribue à l’incertitude ;
- une incertitude élargie doit publier son facteur d’élargissement et son contexte ;
- un mesurande doit être spécifié suffisamment pour savoir ce qui est réellement visé.

## Seed

Sept grandeurs/unités SI de base, plusieurs grandeurs et unités dérivées, propriétés d’instruments, résultats de mesure, étalonnage, étalons, incertitudes Type A/Type B, incertitude composée/élargie, bilans et chaînes de traçabilité. Les exemples numériques sont **synthétiques** et servent uniquement à éprouver le modèle.

## Validation

Exécuter : `python knowledge-base/tools/validate.py`
