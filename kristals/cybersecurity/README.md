# Kristal-Cybersecurity v1.0.0

Corpus statique de référence en cybersécurité, centré sur le modèle :

**actif × menace × vulnérabilité × contrôle × impact**

Le noyau ajoute exposition, scénario, vraisemblance, preuve, état/efficacité des contrôles et risque inhérent/résiduel.

## Taille
- 888 assertions Kristal v6
- 420 référents
- 11 sources externes/éditoriales
- 32 classes d’actifs
- 19 événements de menace
- 24 familles de faiblesses
- 46 contrôles défensifs
- 14 dimensions d’impact

## Principe de raisonnement
Une vulnérabilité ou un score de sévérité n’est pas un risque en soi. Le risque est contextualisé par l’actif, l’exposition, la menace, les contrôles, les conséquences, l’horizon temporel, les preuves et l’incertitude.

## Sources mouvantes
ATT&CK, CVE, CWE et KEV restent des catalogues externes versionnables. Cette édition stocke leur sémantique et quelques identifiants structurants, mais pas une copie massive d’un flux vivant.

## Limite de sécurité
Corpus défensif et encyclopédique : aucune procédure d’exploitation, charge utile, persistance, credential abuse ou action destructive n’est incluse.

## Validation
```bash
python knowledge-base/tools/validate.py
```
