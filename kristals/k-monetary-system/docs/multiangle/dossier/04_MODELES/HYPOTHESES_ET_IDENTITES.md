# Hypothèses du prototype illustratif

Le fichier `prototype_comptable.py` montre uniquement la cohérence **comptable** d'une hypothèse de monnaie de paiement rachetable 1 CAD par K_M. Il n'émet aucune monnaie, ne se connecte à aucun service et ne prouve ni la liquidité sous panique ni la légalité du modèle. L'exemple M1 est un choix pédagogique, **pas une décision sur le régime de K_M**.

## Identités retenues
1. Émission : débit réserve CAD / crédit dette K_M égaux; une hausse de monnaie en circulation exige une contrepartie. Seule une forme simple d'actif est simulée.
2. Transfert : les soldes des usagers s'échangent; les obligations totales de l'émetteur ne changent pas.
3. Rachat : débit dette / crédit réserve égaux; circulation et réserve baissent du même montant.
4. Ristourne : `direct + collectif = enveloppe` déjà approuvable selon un scénario fictif; aucun lien imposé avec les montants réels des caisses.
5. Dette publique : `fin = début + intérêts + solde primaire déficitaire − économies nettes + ajustement stock/flux`. Ne remplace pas normes comptables.
6. Prime lingot : un coût de vente et une décote illustrative de 100 % de la prime correspondent à un choc possible, pas un taux recommandé.
7. Double affectation : une même ID d'actif ne peut être à la fois immobilisée en réserve K_M et librement détenue pour K_C. Les fractions juridiquement documentées seraient modélisées autrement.

## Chocs supplémentaires à intégrer dans un futur modèle multi-agents
Ruée simultanée, fraude et gel de réserves, prix métal, prime artistique, salaire et emploi, demande et offre de produits, impayés, coûts fiscaux, clientèle à revenus modestes et préférences non uniformes. **Le prototype actuel n'est pas un modèle d'équilibre général.**
