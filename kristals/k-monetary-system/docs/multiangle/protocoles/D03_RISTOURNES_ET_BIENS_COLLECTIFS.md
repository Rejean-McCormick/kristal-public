# D03 — Allocation des excédents : ristournes individuelles vs fonds commun
**Sources : S06, C01; droit W01–W05, W20.**

## Problème précis
La ristourne de Desjardins a une composante fixe « produits » (jusqu'à 75 $) et une composante variable selon produits et volumes (comptes, crédits, assurances, investissements); ce n'est pas uniquement un dividende proportionnel à la fortune. [W03] Les bénéfices d'un parc, d'une bibliothèque ou d'un centre communautaire sont répartis selon les usages réels, et ne bénéficient pas automatiquement davantage aux plus démunis. Il faut mesurer l'incidence nette.

## Formule de simulation (non formule officielle de Desjardins)
Avec `E` = enveloppe *légalement* distribuable après réserves/ajustements, `a` = fraction des excédents allant au FADM (`0 ≤ a ≤ 1`), `I = (1−a)*E` et `C = a*E`, seulement si le vote et les normes permettent cette variation.

Pour le décile `d`: `net_d = cash_direct_d − contributions_perdues_d + accès_monétisé_justifié_d − coûts_indirects_d`. **Important :** l'accès à un service public ne crée pas de revenu monétaire et une valorisation monétaire doit expliciter ses hypothèses, demander une enquête et éviter de compter à la fois valeur de l'actif et usage.

## Exemples mathématiques sans prévision
Enveloppe fictive `E = 1 000 000 $` :
| Fraction communautaire a | Direct I | Collectif C | Observabilité |
|---:|---:|---:|---|
| 0,10 | 900 000 $ | 100 000 $ | baseline |
| 0,25 | 750 000 $ | 250 000 $ | variations du service |
| 0,50 | 500 000 $ | 500 000 $ | conséquences de la perte directe |
| 0,75 | 250 000 $ | 750 000 $ | accès, maintenance, équité |

La caisse de Québec a publié en avril 2026 une ristourne totale de 6,2 M$, dont 5 397 688 $ individuellement et 794 007 $ FADM [W05]; cet exemple **ne** peut pas être extrapolé mécaniquement à toutes les caisses.

## Choix des projets
Audit de besoins local, exposition des options, devise de référence et coût total de possession (construction, terrain, entretien pluriannuel, fonctionnement, assurances, taxes, risques). Déclaration des conflits d'intérêts des organismes demandeurs. Critères d'accès : gratuité / prix, accessibilité handicap, transport, qualité réelle et financement des années futures.

## Indicateurs incontournables
1. Montants réellement reçus par ménage et décile de revenu ET patrimoine (sans collecter plus de données que nécessaire).
2. Taux de fréquentation des projets par zone et revenu (anonymisé), bénéfices qualitatifs.
3. Coût par visite/utilisateur unique, coût récurrent, pérennité à 5 ans.
4. Effets redistributifs nets avec contrefactuel et intervalle d'incertitude.
5. Conséquences pour les personnes qui utilisent la ristourne pour des dépenses essentielles.

## Condition d'arrêt
Un projet collectif ne peut recevoir des fonds s'il n'a pas de gestionnaire d'entretien, de mandat légal, de calendrier réalisable et de budget complet.
