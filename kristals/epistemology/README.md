# Kristal Epistemology v1.0.0

Kristal v6 statique de référence sur la chaîne **proposition → preuve → source → justification → croyance → connaissance**.

## Noyau

`proposition ← support/attaque ← preuve ← source/provenance`

`preuve + raisons → justification propositionnelle → relation de fondation → croyance justifiée`

`croyance + vérité + conditions épistémiques supplémentaires → connaissance potentielle`

La chaîne n’est pas une recette automatique. Elle sépare ce qui est affirmé, ce qui le supporte, d’où ce support vient, comment il justifie effectivement une croyance, et pourquoi vérité + justification ne suffisent pas nécessairement à produire de la connaissance.

## Garde-fous sémantiques principaux

- Proposition ≠ phrase : une même proposition peut être exprimée par plusieurs formulations.
- Vérité ≠ croyance : croire p ne rend pas p vraie.
- Preuve ≠ source : la source est l’origine ou le canal; la preuve est ce qui supporte ou affaiblit une proposition.
- Provenance ≠ fiabilité : savoir d’où vient une affirmation ne suffit pas à établir qu’elle est correcte.
- Citation ≠ preuve de vérité : une citation permet de remonter à une source mais ne valide pas automatiquement son contenu.
- Autorité ≠ infaillibilité : expertise ou statut n’entraînent pas la vérité de chaque affirmation.
- Consensus ≠ vérité : une convergence peut être informative sans être une garantie logique.
- Corroboration ≠ indépendance : plusieurs sources peuvent répéter la même source primaire.
- Absence de preuve ≠ preuve d’absence : l’absence devient probante seulement si la méthode avait une capacité pertinente de détection.
- Support ≠ implication : un élément peut rendre une proposition plus crédible sans la garantir.
- Justification ≠ vérité : une croyance rationnellement justifiée peut être fausse.
- Justification propositionnelle ≠ justification doxastique : posséder une bonne raison n’implique pas que la croyance soit effectivement fondée sur elle.
- Raison disponible ≠ raison de la croyance : la relation de fondation distingue ces deux cas.
- Défait ≠ fausseté : une raison peut supprimer une justification sans établir la négation de la proposition.
- Défait sapant ≠ réfutation : il attaque le lien de support plutôt que nécessairement la conclusion.
- Croyance vraie justifiée ≠ définition suffisante de la connaissance : les cas de Gettier montrent le rôle possible de la chance épistémique.
- Crédence élevée ≠ connaissance : confiance subjective et statut de connaissance sont distincts.
- Fiabilité ≠ infaillibilité : un processus fiable peut produire des erreurs.
- Données ≠ interprétation : les mêmes données peuvent recevoir des analyses concurrentes.
- Mesure ≠ vérité brute : une mesure dépend d’un instrument, d’une procédure, d’une calibration et d’une interprétation.
- Peer review ≠ certification de vérité : il s’agit d’un mécanisme de contrôle social et méthodologique faillible.
- Désaccord ≠ réfutation automatique : il peut appeler réexamen, pondération des sources ou suspension selon le contexte.
- Scepticisme ≠ simple ignorance : il s’agit d’une position ou d’un argument sur les limites du savoir ou de la justification.
- Internalisme ≠ externalisme : ce sont des familles théoriques concurrentes sur ce qui compte pour la justification ou la connaissance.
- Fondationnalisme, cohérentisme et infinitisme sont des réponses concurrentes au problème de la structure justificative; le Kristal n’en impose aucune.

## Frontière

Inclus : propositions, vérité, croyance, crédence, preuve, raisons, sources, provenance, témoignage, perception, mémoire, inférence, justification, relation de fondation, défaits, fiabilité, Gettier, chance épistémique, scepticisme, révision de croyance et grandes familles de théories de la justification.

Exclus : logique formelle complète, statistiques détaillées, philosophie des sciences spécialisée, psychologie cognitive expérimentale, vérification factuelle de cas particuliers et théorie métaphysique générale de la vérité.

## Positionnement

Le corpus est **pluraliste** : il représente internalisme, externalisme, évidentialisme, fiabilisme, fondationnalisme, cohérentisme, infinitisme, approches bayésiennes et vertus épistémiques comme positions ou cadres, sans déclarer l’un d’eux vrai par défaut.

## Contenu

- `corpus/epistemology.kristal-state.json` — état canonique v6
- `corpus/referents.json` — registre conceptuel FR/EN
- `sources/` — catalogue et registre d’évidence
- `profiles/` — profil de navigation
- `documentation/` — architecture, frontière et garde-fous
- `tools/validate.py` — validation locale

Les sources externes servent de provenance conceptuelle; aucun texte source substantiel n’est incorporé au corpus.
