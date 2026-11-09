# D12 — De la monnaie aux banques : crédit, liquidité et gestion de crise
**Sources : R01, S01, S09, S10. Ancrages W09, W18, W19.**

## Pourquoi cette couche est nécessaire
Un portefeuille de paiements et un réseau de crédit sont différents. L'octroi de prêts en K_M augmente les engagements de paiement; la liquidité instantanée, les risques de défaut, les dépôts et la protection des créanciers exigent un schéma explicite. Un « smart contract » seul ne rend pas un emprunteur solvable.

## Architecture candidate de crédit
(1) Créanciers autorisés, (2) scoring non discriminatoire soumis à examen, (3) limites de concentration, (4) capital et coussins de liquidité, (5) portefeuille de défauts et recouvrements, (6) service d'assistance aux surendettés, (7) auditeur, (8) mécanisme de redressement, (9) confidentialité et recours.

## Test micro
Le prêteur avance 100 K_M : soit il détient déjà les 100 unités, soit il crée une créance compensée par un passif défini; en aucun cas le récit « la confiance crée l'actif » ne remplace la comptabilité. Au remboursement, distinguer principal et intérêts; au défaut, constater une perte d'actif pour la personne/institution qui l'a financé.

## Stress
Vague de retraits 40 %, défaillances corrélées 15 %, liquidité bloquée pendant 7 jours, choc sur collatéral, attaque cyber et baisse des prix. Sous ces scénarios, déterminer qui paie les pertes avant d'accorder un financement réel.

## Indicateurs
Ratio de liquidité, actifs libres, exposition concentration, retard paiement, créances douteuses, capacité de recapitalisation, taux de plainte résolu, coûts effectifs de crédit.
