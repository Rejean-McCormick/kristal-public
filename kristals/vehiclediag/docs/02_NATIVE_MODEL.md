# Modèle natif

## Primitives du domaine

Composants, ports/bornes, connexions, couches, chemins fonctionnels, états opératoires, dependency sets, points de test, mesures, symptômes, DTC, modes de panne et archétypes.

## Relations / transformations

Les connexions relient des ports; les chemins ordonnent des segments fonctionnels; les états opératoires activent ou désactivent des comportements; les modes de panne perturbent le graphe; les tests produisent des observations permettant de mettre à jour les hypothèses diagnostiques.

## Dimensions internes

Le modèle couvre notamment les couches électrique, masse, signal, contrôle, réseau, fluide, hydraulique, air, mécanique, thermique et fonctionnelle.

## Forme native retenue

`multiplex_causal_diagnostic_model` — graphe causal multiplexe exécutable à granularité composant/port/arête.

## Logical Contracts v9

- `vehiclediag.reference-model/3.0` : modèle métier natif normalisé.
- `kristal_state.hash_target/6.0` : overlay épistémique portable v6, dépendant du modèle de référence.

## Pourquoi cette forme ne perd pas d'information essentielle

Une réduction à une table symptôme/cause ou à une liste générique d’assertions perdrait la topologie, la granularité des ports, l’ordre des chemins, les états opératoires, les dépendances et la distinction entre couches.

## Alternatives rejetées

Le portable v6 et les indexes v8 restent des projections d’interopérabilité/lecture; ils ne remplacent pas le modèle natif.
