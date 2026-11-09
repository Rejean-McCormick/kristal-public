# Kristal — Pouvoirs Pays-Bas v0.1.0

Kristal de référence pour la série **« Qui décide quoi ? » — Pays-Bas**.

Le paquet modélise les mécanismes de pouvoir de l'ordre juridique **interne néerlandais** : Statuut/Grondwet, Roi et responsabilité ministérielle, Gouvernement et Conseil des ministres, États généraux, loi et réglementation, Conseil d'État, justice judiciaire et administrative, provinces, communes, waterschappen et gouvernance scolaire.

## Frontière supranationale

Ce Kristal **n'embarque pas** le droit international ou de l'Union européenne substantiel. Il conserve uniquement l'interface néerlandaise nécessaire pour expliquer l'approbation des traités, le transfert de compétences prévu par la Constitution, l'effet interne des articles 93-94 et les limites du contrôle juridictionnel.

Le contenu matériel des traités, coutumes, jus cogens, obligations erga omnes, droit humanitaire, droits humains internationaux, droit de la mer, commerce international, responsabilité internationale et droit matériel de l'UE doit vivre dans le Kristal supranational/international.

## Distinction Royaume / Pays-Bas

Le **Statuut voor het Koninkrijk der Nederlanden** est conservé comme interface constitutionnelle indispensable parce que la Constitution lui est subordonnée. Le corpus ne modélise toutefois pas en détail Aruba, Curaçao ou Sint Maarten. Les organes propres à Bonaire, Saint-Eustache et Saba sont également laissés à une extension ultérieure.

## Canonique

`knowledge-base/corpus/pouvoirs-pays-bas.kristal-state.json` — **116 assertions**, **32 sources officielles indexées**, état au **2026-10-02**.

## Validation

```bash
cd knowledge-base
python tools/validate.py
```

## Recherche

```bash
python tools/query.py --actor tweede-kamer
python tools/query.py --level Municipal
python tools/query.py --text "ne peut pas"
python tools/query.py --source SRC-NL-CONST-2023
```
