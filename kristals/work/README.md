# Kristal-Work v0.1.0

Corpus statique et versionné de référence sur la chaîne **activité → compétence → rôle → métier → environnement → résultat**.

## Noyau conceptuel

`poste/contexte → tâches & activités → compétences mobilisées → rôle(s) → occupation/métier → environnement → résultat direct`

## Garde-fous

- poste/job ≠ métier/occupation ;
- rôle ≠ métier ;
- activité ≠ compétence ;
- compétence ≠ diplôme, licence ou titre ;
- profil d’un métier ≠ attribut automatique d’une personne ;
- environnement de travail = contexte variable, pas propriété universelle du métier ;
- danger/exposition ≠ dommage ;
- résultat direct du travail ≠ effet aval multicausal ;
- compétences et métiers forment des relations plusieurs-à-plusieurs ;
- toute classification externe doit conserver sa version.

## Seed

Le seed contient des activités transversales, compétences, rôles, métiers illustratifs couvrant plusieurs familles ISCO, environnements physiques/sociaux/organisationnels, exigences et résultats directs. Les scénarios sont **synthétiques** et servent à éprouver le modèle, pas à décrire des personnes ou employeurs réels.

## Validation

Exécuter : `python knowledge-base/tools/validate.py`
