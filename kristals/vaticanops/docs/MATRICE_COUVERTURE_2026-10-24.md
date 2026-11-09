# VaticanOps — matrice de couverture documentaire

Date de référence : 24 octobre 2026. Tous les chiffres proviennent des fichiers présents, pas d’une hypothèse sur ce que le Vatican aurait publié.

## Couverture de la copie hors ligne

| Ensemble capturé | Unités de texte intégral, SHA-256 vérifiées |
|---|---:|
| `curie-reglement-2025` | 52 |
| `cic-1983` | 1721 |
| `praedicate-evangelium-2022` | 250 |
| `vademecum-ddf-2022` | 165 |
| `universi-dominici-gregis-1996` | 91 |
| `missel-general` | 399 |

**Total : 2678 unités, 57 graphes de procédures éditoriaux, 78 notices externes sans texte capturé.**

## Registre des références externes

Un enregistrement est une page officielle de document précis ou un index de collection. Un index ne prouve pas l’exhaustivité de ses sous-documents.
Le fichier CSV `validation/REGISTRE_71_REFERENCES.csv` fournit le détail des 71 entrées. Toutes restent non acquises dans ce paquet.

## Points de vigilance temporelle
- **P0 — LOI-2026** : La loi fondamentale du 31 juillet 2026 est recensée dans la collection officielle mais son PDF n’est pas copié localement. (VO-N009)
- **P0 — CCEO** : Le code oriental de 1990 et les modifications du 29 août 2026 sont seulement référencés, sans version consolidée locale. (VO-N007, VO-N008)
- **P0 — PERSONNEL** : Le règlement du personnel entré en vigueur le 1er janvier 2026 est référencé mais non copié. (VO-N001)
- **P0 — VELM** : Le Vademecum DDF 2022 (capturé) renvoie historiquement à Vos estis lux mundi 2019. Le texte VELM 2023 est référencé, non fusionné. (VO-N004)
- **P0 — JUDICIAIRE** : Les réformes 2015 de la nullité matrimoniale et la Lex propria 2024 ne sont pas dans le corpus local original. (VO-N011, VO-N012, VO-N013)
- **P0 — DDF-2021** : Les normes des délits réservés 2021 restent hors des six œuvres capturées. (VO-N003)
- **P1 — CONCLAVE** : Universi Dominici Gregis local mentionne sa consolidation de 2013; vérifier tout changement ultérieur dans les AAS. (VO-N010)
- **P1 — CIC-COLLISION** : Collision textuelle de canon dans l’inventaire initial: 230 (CIC-230)
- **P1 — CIC-COLLISION** : Collision textuelle de canon dans l’inventaire initial: 604 (CIC-604)
- **P1 — CIC-COLLISION** : Collision textuelle de canon dans l’inventaire initial: 686 (CIC-686)
- **P1 — CIC-COLLISION** : Collision textuelle de canon dans l’inventaire initial: 688 (CIC-688)
- **P1 — CIC-COLLISION** : Collision textuelle de canon dans l’inventaire initial: 695 (CIC-695)
- **P1 — CIC-COLLISION** : Collision textuelle de canon dans l’inventaire initial: 700 (CIC-700)
- **P1 — CIC-COLLISION** : Collision textuelle de canon dans l’inventaire initial: 775 (CIC-775)

## Frontières non franchies

- Le corpus original ne contient pas les actes propres à chaque dicastère, tous les statuts, les lois du Gouvernorat, les concordats et toutes les AAS.
- Il ne contient pas nécessairement les manuels de sécurité, procédures diplomatiques réservées ni les `Ordo servandus` non publics.
- Des textes trouvés sur le Web peuvent être obsolètes. Une date de publication ne détermine pas à elle seule la version en vigueur.
- Une détection lexicale n’est pas une étape canonique. Aucun graphe ajouté automatiquement n’est approuvé.
- Une procédure juridiquement exacte exige un lecteur qualifié et une détermination contextualisée des autorités et du champ.

## Travail restant pour une exhaustivité vérifiable

1. Acquérir et hacher tous les textes visés par les 71 entrées; dépouiller les index officiels.
2. Vérifier les publications officielles, entrées en vigueur, abrogations, dérogations, textes propres et versions linguistiques.
3. Transformer les dispositions en graphes conditionnels sourcés, puis qualifier chaque branche, compétence et exception.
4. Construire une matrice de couverture article par article avec auteur de revue, date et preuve de validation.
5. Réexécuter la collecte à chaque publication; documenter les collections et normes indisponibles ou non publiques.
