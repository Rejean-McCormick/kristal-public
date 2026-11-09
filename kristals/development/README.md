# Kristal-Development v1.0.0

**Trajectoires développementales**

Corpus statique et reconstruisible décrivant le développement comme un continuum structuré par :

`stade → acquisition → variation → environnement`

avec une couche de **trajectoires** qui empêche de mélanger des stades appartenant à des organismes ou processus différents.

## Contenu

- **11** trajectoires développementales
- **86** stades/repères
- **80** acquisitions ou processus acquis
- **45** formes de variation
- **28** dimensions environnementales
- **462** relations structurées
- **202** chemins stage→acquisition→variation→environnement matérialisés

## Principe éditorial

Un stade est un repère dans un continuum et non une frontière biologique universelle. Une acquisition n'est pas une échéance individuelle. La variation est une propriété normale du développement; les facteurs environnementaux peuvent moduler une trajectoire sans la déterminer mécaniquement.

Le corpus couvre plusieurs échelles : embryogenèse animale et vertébrée, développement humain prénatal et petite enfance, puberté, métamorphoses, poisson-zèbre et développement végétal.

## Validation

```bash
cd knowledge-base
python tools/validate.py
python -m unittest discover -s tests -v
```

Statut : `working` — validation structurelle et éditoriale, sans usage diagnostique individuel.
