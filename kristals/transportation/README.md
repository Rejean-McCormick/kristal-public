# Kristal-Transportation v0.1.0

Corpus statique et versionné de référence sur la chaîne **origine → réseau → véhicule/service → destination**, avec **capacité, coût, temps et flux**.

## Noyau conceptuel

`origine + destination + fenêtre temporelle → demande O-D → chemin/réseau → mode/véhicule/service → flux observé → temps/coût/performance`

Le Kristal représente aussi les transferts multimodaux, les capacités de lien/véhicule/terminal, les temps composés d’un itinéraire et la distinction entre service planifié et réalisé.

## Garde-fous

- débit de véhicules ≠ débit de personnes ;
- débit observé ≠ demande latente ;
- capacité ≠ débit ;
- embarquement ≠ voyage origine-destination ;
- temps moyen ≠ fiabilité du temps de parcours ;
- valeur du fret ≠ coût du transport ;
- flux affecté par un modèle ≠ comptage observé ;
- service planifié ≠ service réellement opéré ;
- coût généralisé = construction de modèle avec paramètres explicites ;
- un itinéraire multimodal doit rendre ses transferts explicites.

## Seed

Réseaux routier, ferroviaire, collectif, piéton, cyclable, aérien et maritime; véhicules; matrices O-D voyageurs et fret; débits; passager-distance, tonne-distance et véhicule-distance; capacité, volume/capacité, goulots; temps d’accès, attente, bord, correspondance, sortie et fiabilité; tarifs, péages et coût généralisé; scénarios routier, collectif et fret intermodal.

## Validation

Exécuter : `python knowledge-base/tools/validate.py`
