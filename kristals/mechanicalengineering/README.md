# Kristal-MechanicalEngineering v0.1.0

Corpus statique et versionné de référence sur la chaîne **efforts → mouvement → mécanismes → puissance → usure/défaillance**.

## Noyau conceptuel

`effort/charge → mouvement → mécanisme → transmission de puissance → contact/tribologie → endommagement → défaillance`

Le Kristal sépare explicitement les grandeurs physiques, les relations cinématiques idéales, les performances réelles et les mécanismes d’endommagement.

## Garde-fous

- force/couple ≠ puissance ; la puissance exige une vitesse ;
- couple ≠ énergie, même si les dimensions SI coïncident ;
- cinématique idéale ≠ capacité réelle d’un composant ;
- usure ≠ défaillance instantanée ;
- fatigue exige un historique de chargement ;
- durée de vie de roulement = grandeur statistique ;
- mode de défaillance observé ≠ cause racine démontrée.

## Contenu seed

Grandeurs et efforts, mouvements, engrenages, leviers, vis, came-suiveur, quadrilatère articulé, roulements, arbres, accouplements, puissance et rendement, régimes de lubrification, usure abrasive/adhésive/fatigue de surface, fatigue, flambement, rupture, pitting, spalling, grippage, surcharge et désalignement.

## Validation

Exécuter : `python knowledge-base/tools/validate.py`
