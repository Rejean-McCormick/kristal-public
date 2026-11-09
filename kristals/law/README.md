# Kristal-Law

**Version:** 1.0.0  
**Édition:** 2026-10-02  
**Format canonique:** Kristal Standard 6.0 (`kristal_state`)

Kristal-Law est un corpus statique, traçable et orienté IA sur la **normativité juridique**.

## Axe conceptuel

`Sujet → règle → droit/obligation → condition → exception → juridiction → décision`

Le modèle ajoute quatre dimensions indispensables : **source**, **temps**, **autorité** et **portée**.

Une règle de droit positif n'est donc jamais stockée comme une phrase isolée. Elle doit pouvoir être reliée à sa source, sa disposition, sa juridiction, son état temporel et les décisions qui l'interprètent ou l'appliquent.

## Distinction structurante

Kristal-Law sépare trois objets que les corpus juridiques confondent souvent :

1. **le texte/source** — ce qui est publié ou adopté;
2. **la norme reconstruite** — sujet + modalité + contenu + conditions + exceptions + portée;
3. **la décision** — ce qu'une autorité décide, avec questions, conclusions, motifs et dispositif.

## Contenu de cette édition

- sujets de droit, autorités, cours, tribunaux et parties;
- obligations, interdictions, permissions, droits, libertés, pouvoirs et immunités;
- conditions, faits générateurs, exceptions, exemptions, défaits, sanctions et recours;
- juridiction et portées territoriale, personnelle, matérielle et temporelle;
- sources : constitution, loi/code, règlement, traité, contrat, jugement, etc.;
- cycle temporel : adoption, entrée en vigueur, modification, abrogation, expiration et suspension;
- décisions : question, holding, motifs, ratio/obiter, dispositif, majorité, concordance, dissidence et relations de précédent;
- exemples positifs datés du Canada et du Québec pour valider la structure du modèle.

## Politique de droit positif

Les lois changent. Les exemples de droit positif de cette édition sont donc des **snapshots datés**, et non une prétention à représenter éternellement le droit en vigueur.

- Charte canadienne : snapshot de la consolidation indiquée comme à jour au **2026-09-21**;
- Code civil du Québec : snapshot de la source PDF indiquée comme à jour au **2025-09-01**.

Toute utilisation pratique doit vérifier le texte officiel et la jurisprudence applicables au moment pertinent.

## Frontière

Kristal-Law n'est pas un service de conseil juridique, un moteur de prédiction judiciaire ni une copie exhaustive des lois. Il fournit la **grammaire stable de la normativité** et des exemples traçables permettant à d'autres Kristals juridiques, par juridiction ou matière, de venir s'y rattacher.

## Fichiers centraux

- `knowledge-base/corpus/law.kristal-state.json` — état canonique v6;
- `knowledge-base/corpus/law.referent-registry.json` — identités stables;
- `knowledge-base/sources/rule_exemplars.json` — règles positives normalisées et datées;
- `knowledge-base/sources/norm_model.json` — forme canonique d'une norme;
- `knowledge-base/sources/decision_model.json` — structure d'une décision;
- `knowledge-base/profiles/law.normative-analysis.json` — ordre d'analyse IA;
- `validation/law-validation-report.json` — contrôles techniques et éditoriaux.
