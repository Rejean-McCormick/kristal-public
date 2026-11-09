# Kristal Software v1.0.0

Kristal v6 statique de référence sur le cycle **intention → spécification → code → exécution → état → défaut**.

## Noyau

`intention → besoins → exigences / spécification → conception → code / build → exécution → état → défaut / erreur → défaillance → diagnostic / correction`

Le corpus sépare explicitement **ce que l’on veut**, **ce qui est spécifié**, **ce qui est écrit**, **ce qui est construit**, **ce qui s’exécute**, **l’état produit** et **ce qui échoue**.

## Garde-fous sémantiques principaux

- intention ≠ exigence ;
- exigence ≠ spécification complète ;
- spécification ≠ implémentation ;
- code source ≠ exécutable ;
- programme ≠ processus ;
- code ≠ exécution ;
- état interne ≠ sortie observable ;
- défaut ≠ état erroné ≠ défaillance ;
- exception ≠ défaillance ;
- vulnérabilité ≠ exploitation ;
- compilation réussie ≠ correction ;
- tests réussis ≠ preuve générale de correction ;
- couverture de test ≠ correction ;
- vérification ≠ validation ;
- concurrence ≠ parallélisme ;
- rollback ≠ rollback sûr.

## Frontière

Inclus : besoins et exigences, spécification, conception/architecture au niveau conceptuel, code source, build, dépendances, exécution, état, concurrence, chaîne défaut→erreur→défaillance, tests, vérification/validation, qualité, sécurité de développement, observabilité, versions, release et maintenance.

Exclus : apprentissage d’un langage particulier, catalogue d’algorithmes, OS/réseaux détaillés, cloud/SRE approfondi, bases de données en profondeur, cryptographie/offensive security et règles métier sectorielles.

## Contenu

- `corpus/software.kristal-state.json` — état canonique v6
- `corpus/referents.json` — registre conceptuel FR/EN
- `sources/` — catalogue et registre d’évidence
- `profiles/` — profil de navigation
- `documentation/` — architecture, frontière et garde-fous
- `tools/validate.py` — validation locale

Les sources externes établissent la provenance des assertions; leur contenu n’est pas incorporé textuellement dans le corpus.
