# Kristal Disasters v1.0.0

Kristal v6 statique de référence sur la chaîne **événement → dommages → besoins → réponse → récupération**.

## Noyau

`aléa → événement dangereux × exposition × vulnérabilité / capacité → impacts`

`impacts → dommages / pertes / besoins → priorisation → réponse`

`réponse ↔ relèvement précoce → récupération → réhabilitation / reconstruction → réduction du risque futur`

La chaîne est descriptive, non strictement linéaire : la réponse peut commencer avant le pic d’un événement, la récupération peut commencer pendant la réponse, et les évaluations doivent être révisées quand l’information change.

## Garde-fous sémantiques principaux

- Aléa ≠ catastrophe : un phénomène potentiellement dommageable ne constitue pas à lui seul une catastrophe.
- Événement dangereux ≠ catastrophe : les effets dépendent de l’exposition, de la vulnérabilité et des capacités.
- Risque ≠ aléa : le risque inclut les conséquences potentielles et les conditions d’exposition et de vulnérabilité.
- Exposition ≠ vulnérabilité : être présent dans une zone dangereuse et être susceptible d’en subir des effets ne sont pas le même concept.
- Magnitude ≠ intensité : une mesure globale de l’événement ne se confond pas avec la sévérité locale de ses effets.
- Dommage ≠ perte : le dommage concerne principalement l’atteinte physique aux actifs; la perte peut concerner les flux, revenus, production ou services.
- Impact ≠ besoin : une conséquence observée n’indique pas automatiquement quelle intervention est requise.
- Besoin ≠ demande exprimée : une évaluation peut identifier des besoins non formulés, et toute demande n’a pas nécessairement la même priorité.
- Évaluation rapide ≠ état définitif : elle est réalisée sous information incomplète et doit être actualisée.
- Gravité ≠ priorité : la priorité dépend aussi de l’urgence, des populations concernées, des capacités, de l’accès et des ressources.
- Préparation ≠ réponse : la préparation précède et soutient l’action sans être l’action elle-même.
- Alerte ≠ prévision : une prévision décrit un futur possible; une alerte communique un danger et vise une action.
- Alerte reçue ≠ action garantie : compréhension, confiance, capacité d’agir et contraintes matérielles interviennent.
- Réponse ≠ secours seulement : la réponse inclut coordination, sécurité, information et services en plus des distributions matérielles.
- Réponse ≠ récupération : leurs objectifs dominants diffèrent, même si elles se chevauchent dans le temps.
- Récupération ≠ reconstruction : reconstruire des actifs n’épuise pas la récupération des moyens d’existence, services, santé et fonctions sociales.
- Récupération ≠ retour exact au point de départ : elle peut restaurer, améliorer, adapter ou transformer.
- « Build Back Better » ≠ reconstruire à l’identique plus vite : le principe vise l’intégration de réduction du risque et de résilience.
- Résilience ≠ absence de dommages : un système peut subir des dommages et conserver ou retrouver ses fonctions.
- Résilience ≠ invulnérabilité : des risques résiduels demeurent même avec de fortes capacités.
- Indicateur ≠ résultat : l’indicateur mesure ou représente un aspect du résultat; il n’est pas le résultat lui-même.
- Ressource disponible ≠ accès effectif : une ressource peut exister sans pouvoir atteindre les personnes qui en ont besoin.
- Coordination ≠ commandement unique : plusieurs modèles institutionnels peuvent coordonner des acteurs sans structure identique.
- Population affectée ≠ bénéficiaire passif : les personnes affectées sont aussi sources d’information, acteurs de réponse et agents de récupération.
- Aide ≠ absence de risque secondaire : une intervention peut avoir des effets non intentionnels et doit intégrer protection et principe de ne pas nuire.

## Frontière

Inclus : aléas et événements dangereux, exposition, vulnérabilité, capacité, risque, préparation, dommages, pertes, impacts humains, évaluations rapides et détaillées, besoins, priorisation, réponse humanitaire générale, coordination, logistique, protection, récupération, réhabilitation, reconstruction, résilience, suivi et résultats.

Exclus : protocoles opérationnels propres à une juridiction, plans d’évacuation propres à un bâtiment ou territoire, prévisions spécialisées d’un aléa, calculs d’ingénierie structurelle, prescriptions médicales et triage clinique détaillé, conduite militaire, droit des conflits armés et instructions individuelles de survie en temps réel.

## Positionnement

Ce Kristal décrit **comment une catastrophe devient observable et actionnable comme système de besoins et de récupération**. Il est compatible avec de futurs Kristals spécialisés sur les aléas (séismes, inondations, incendies), les infrastructures, l’humanitaire ou la résilience, sans absorber leurs détails.

## Contenu

- `corpus/disasters.kristal-state.json` — état canonique v6
- `corpus/referents.json` — registre conceptuel FR/EN
- `sources/` — catalogue et registre d’évidence
- `profiles/` — profil de navigation
- `documentation/` — architecture, frontière et garde-fous
- `tools/validate.py` — validation locale

Les sources externes servent de provenance conceptuelle; aucun texte source substantiel n’est incorporé au corpus.
