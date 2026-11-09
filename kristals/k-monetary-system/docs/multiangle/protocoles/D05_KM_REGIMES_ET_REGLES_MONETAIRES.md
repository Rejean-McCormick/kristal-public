# D05 — Spécification de K_M : choisir un régime avant l'émission
**Sources : canon monetary-constitution.json et monetary-policy.json, S01, S10, C01; droit W06–W10, W12–W14, W19, W22.**

## Problème de définition
Le K_M actuel est un « candidat de monnaie / règlement »; il n'indique pas encore clairement qui est débiteur, quelle valeur un détenteur peut exiger, quand, auprès de qui, ni si les émissions sont couvertes.

## Options MUTUELLEMENT DISTINCTES
| Option | Promesse contractuelle | Contrepartie minimale | Effet probable de qualification | Difficulté déterminante |
|---|---|---|---|---|
| M0 points fermés sans rachat | échange de services limités, non monétaire général | obligations commerciales et consommation | analyse de portée nécessaire | pas monnaie générale |
| M1 créance CAD 1:1 | remboursement de 1 CAD par unité | réserves admissibles et ségrégation | stablecoin fiat et/ou PSP, autres règles | rachat, liquidité, gouvernance |
| M2 panier multi-actifs | prix cible d'indice, droits spécifiés | actif correspondant et marché | pas automatiquement stablecoin CAD; titres possible | risque de change / rachat |
| M3 flottant sans rachat | valeur de marché seulement | aucun rachat promis | actifs/monnaie virtuelle + PSP selon usage | volatilité |
| M4 unité de compte / compensation | règles de règlement et crédit mutuel | contreparties, garanties, défauts | crédit et paiement, dépend dispositif | solvabilité des émetteurs |

**M1** doit anticiper la loi et le projet de règlement sur les stablecoins [W07,W08] tout en notant leur entrée en vigueur non encore achevée au 01-11-2026. **M2/M3** ne constituent pas une échappatoire automatique aux régulateurs. **M4** nécessite la qualification du risque de crédit et du dépôt. Ne pas appeler K_M « monnaie légale », « garanti par l'État » ni « dépôt assuré » sans fondement.

## Contrat minimal d'émission (exemple de structure, non décision)
`issuer_id`, `legal_form`, `currency_reference`, `claim_type`, `redeemability`, `redemption_deadline`, `fees`, `liquidity_policy`, `reserve_asset_universe`, `custodian`, `redemption_priority`, `proof_of_reserves`, `auditor`, `governance`, `recovery`, `winding_down`, `privacy`, `complaints`, `tax_reporting`, `jurisdiction`, `consumer_warning`.

## Conditions de conservation / règlement
- Pour un **portefeuille interne sans émission**, transfert de 10 unités : `solde_A' = solde_A − 10`, `solde_B' = solde_B + 10`; total circulation invariant hors émission et destruction.
- Pour **créance rachetable M1**, `K_M_circulant × 1 CAD = dette_de_rachat`, dont les réserves doivent supporter la liquidité au pair et exigences légales. La disponibilité d'un lingot brandé n'équivaut pas à une liquidité CAD.
- Autorité de monnaie, dépositaire, auditeur et médiateur sont des rôles séparés dans l'architecture cible.

## Tests bloquants
Refuser l'émission si le régime M? n'est pas choisi, l'identité du débiteur non déclarée, le mécanisme de résolution absent ou le périmètre de licences non qualifié. Stress-test de ruée, fraude, cyberattaque, arbitrage, dépeg, catastrophe opérationnelle et clôture ordonnée. Critères BIS : unité, élasticité et intégrité [W19], sans prétendre reproduire la puissance d'une banque centrale.
