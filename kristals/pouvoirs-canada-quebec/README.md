# Kristal — Pouvoirs publics Canada / Québec

Version **0.2.0** — référence **2026-10-02**.

Ce Kristal décrit les mécanismes juridiques internes du pouvoir au Canada et au Québec : **qui décide, au nom de quelle autorité, dans quel domaine, sous quelles limites, qui doit rendre des comptes et qui peut contrôler la décision**.

## Nettoyage v0.2

Le droit international a été **retiré** de ce paquet. Il appartient désormais à `Kristal-Droit-International-Global`. Ce Kristal ne conserve que les règles internes nécessaires pour déterminer les compétences canadiennes et québécoises.

La refonte sépare désormais cinq concepts :

1. `legal_authority` — pouvoir juridiquement attribué;
2. `political_responsibility` — obligation politique de répondre devant une assemblée ou le public;
3. `administrative_delegation` — pouvoir exercé par un fonctionnaire ou organisme en vertu d’une attribution/délégation;
4. `political_influence` — capacité de persuasion ou de direction politique sans effet juridique automatique;
5. `review_control` — mécanisme permettant de réviser, invalider, renverser ou demander des comptes.

## Portée

- Constitution et fédéralisme;
- Parlement, Chambre des communes, Sénat, Couronne;
- premier ministre, Cabinet, ministres, députés, sénateurs, sous-ministres;
- règlements et délégations;
- poursuites fédérales et québécoises;
- tribunaux et contrôle judiciaire;
- Parlement, gouvernement et administration du Québec;
- Charte canadienne et Charte québécoise;
- municipalités, maires, conseillers, MRC;
- gouvernance scolaire, CSS francophones et commissions scolaires anglophones;
- article 35 et place constitutionnelle des droits ancestraux et issus de traités.

## Dépendance externe

Pour les traités, coutume internationale, jus cogens, ONU, CIJ, CPI, droit humanitaire, etc., utiliser le Kristal séparé **Droit international global**.

## Invariants

`OFFICE != TITULAIRE`  
`ÉLECTION != POUVOIR ILLIMITÉ`  
`RESPONSABILITÉ POLITIQUE != COMPÉTENCE DÉCISIONNELLE`  
`INFLUENCE POLITIQUE != AUTORITÉ JURIDIQUE`  
`LOI != RÈGLEMENT != DÉCRET != RÉSOLUTION != DIRECTIVE`  
`FÉDÉRAL != AUTOMATIQUEMENT SUPÉRIEUR AU PROVINCIAL`  
`MUNICIPAL != SOUVERAIN`

Le paquet est une base de référence structurée, pas un avis juridique. Les états procéduraux et configurations institutionnelles marqués `current_as_of_2026-10-02` doivent être revalidés ultérieurement.
