# Kristal Robotics v1.0.0

Kristal v6 statique de référence sur la boucle **percevoir → estimer → décider → agir → rétroagir** en robotique.

## Noyau

`perception → estimation d’état → décision / planification → actionnement → rétroaction`

Le corpus sépare explicitement **le monde réel**, **les mesures**, **l’état estimé**, **la décision**, **la commande** et **le résultat physique**.

## Garde-fous sémantiques principaux

- mesure ≠ état réel ;
- perception ≠ capteur ;
- localisation ≠ cartographie ;
- estimation ≠ vérité terrain ;
- incertitude ≠ erreur observée ;
- pose ≠ position ;
- chemin ≠ trajectoire ;
- plan ≠ résultat garanti ;
- commande ≠ résultat physique ;
- actionneur ≠ contrôleur ;
- cinématique ≠ dynamique ;
- boucle fermée ≠ stabilité garantie ;
- autonomie ≠ apprentissage automatique ;
- autonomie ≠ absence d’humain ;
- performance ≠ sécurité.

## Frontière

Inclus : perception robotique fondamentale, capteurs comme abstractions, estimation d’état, fusion, localisation/cartographie/SLAM, planification de mouvement, actionnement, cinématique/dynamique au niveau conceptuel, commande et rétroaction, autonomie contextuelle, notions de sécurité.

Exclus : conception mécanique détaillée, électronique de puissance, vision/ML avancés, théorie exhaustive de commande, robotique médicale, certification ou analyse de risque spécifique à une installation.

## Contenu

- `corpus/robotics.kristal-state.json` — état canonique v6
- `corpus/referents.json` — registre conceptuel FR/EN
- `sources/` — catalogue et registre d’évidence
- `profiles/` — profil de navigation
- `documentation/` — architecture, frontière et garde-fous
- `tools/validate.py` — validation locale

Les sources externes établissent la provenance des assertions; leur contenu n’est pas incorporé textuellement dans le corpus.
