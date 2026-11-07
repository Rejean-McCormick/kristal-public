# Kristal-Aerospace v1.0.0

Corpus statique et validé décrivant la grammaire d’une mission aérospatiale autour de la chaîne **mission → véhicule → environnement → trajectoire → systèmes**.

Le corpus couvre à la fois l’aéronautique et le spatial au niveau de leurs abstractions communes, tout en conservant leurs régimes physiques et opérationnels distincts.

## Noyau conceptuel

- **Mission** : objectifs, architecture, concept d’opérations, profil, critères de succès.
- **Phases** : prévol, décollage, croisière, lancement, ascension, orbite, entrée, atterrissage, fin de mission.
- **Véhicule** : aéronef, engin spatial, lanceur, charge utile, configurations et propriétés de masse.
- **Environnement** : atmosphère, vide, gravité, météo, thermique, rayonnement, plasma, débris, vibrations et chocs.
- **Trajectoire** : état, chemin de vol, référence/réel, manœuvres, orbites, fenêtres et enveloppes.
- **Systèmes** : structure, propulsion, puissance, thermique, GN&C, avionique, communications, données, support-vie et charge utile.
- **Opérations/interfaces** : segment sol, contrôle mission, télémesure, procédures, modes nominaux/non nominaux et interfaces physiques/logiques.

## Garde-fous majeurs

- mission ≠ véhicule ;
- objectif ≠ critère de succès ;
- phase ≠ trajectoire ;
- trajectoire de référence ≠ trajectoire réelle ;
- position ≠ état complet ;
- attitude ≠ trajectoire ;
- delta-v ≠ vitesse ;
- guidage ≠ navigation ≠ contrôle ;
- météo ≠ atmosphère ;
- pression dynamique ≠ pression statique ;
- charge utile ≠ plateforme ;
- masse à sec ≠ masse avec ergols ;
- budget de ressource ≠ ressource physique ;
- télémesure ≠ preuve automatique de santé ;
- Aerospace n’absorbe pas la physique détaillée, la certification, le droit, l’ATM, la mécanique orbitale ou l’ingénierie système.

## Taille

- Référents : **241**
- Assertions atomiques : **717**
- Sources : **8**

## Organisation

Le fichier canonique est `knowledge-base/corpus/aerospace.kristal-state.json`. Le registre d’identité est `aerospace.referent-registry.json`. Des modèles spécialisés fournissent des vues mission, véhicule-environnement, trajectoire-phase, systèmes embarqués et opérations/interfaces.

## Statut

Référence statique v1.0.0. Les données dynamiques (météo, NOTAM, éphémérides, objets orbitaux, état d’un véhicule réel) sont explicitement hors corpus.
