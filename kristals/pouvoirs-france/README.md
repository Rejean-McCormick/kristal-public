# Kristal — Pouvoirs France v0.1.0

Kristal de référence pour la série **« Qui décide quoi ? » — France**.

Le paquet modélise les mécanismes de pouvoir de l'ordre juridique **interne français** : Constitution, Président, Gouvernement, Parlement, loi/règlement/ordonnances, contrôle constitutionnel, dualité juridictionnelle, collectivités territoriales, administration déconcentrée et éducation.

## Frontière supranationale

Ce Kristal **n'embarque pas** le droit international ou de l'Union européenne substantiel. Il conserve seulement l'interface française nécessaire pour expliquer qui peut négocier/ratifier, quand une autorisation législative est requise, le rang interne prévu par l'article 55, et les mécanismes constitutionnels français liés à l'UE.

Le contenu matériel des traités, coutumes, jus cogens, obligations erga omnes, droit humanitaire, droits humains internationaux, droit de la mer, commerce international, responsabilité internationale et droit matériel de l'UE doit vivre dans le Kristal supranational/international.

## Canonique

`knowledge-base/corpus/pouvoirs-france.kristal-state.json` — 89 assertions, 21 sources officielles indexées, état au **2026-10-02**.

## Validation

```bash
cd knowledge-base
python tools/validate.py
```

## Recherche

```bash
python tools/query.py --actor president
python tools/query.py --level Commune
python tools/query.py --text "ne peut pas"
python tools/query.py --source SRC-FR-CONST
```
