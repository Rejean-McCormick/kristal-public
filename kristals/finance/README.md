# Kristal-Finance v1.0.0

**Actif × temps × risque × flux monétaire × valorisation.**

Kristal-Finance décrit les claims financiers comme des droits et obligations sur des flux monétaires situés dans le temps, exposés à des risques et mesurés selon une définition de valeur et une méthode explicites.

## Noyau conceptuel

```text
Actif / claim
    │
    ├── termes contractuels ──> flux monétaires datés
    │                              │
    │                         temps / taux
    │                              │
    ├── expositions ───────────> risques
    │                              │
    └────────── définition + méthode de valorisation
                                   │
                                valeur
```

## Distinctions obligatoires

- prix ≠ valeur;
- prix de transaction ≠ nécessairement juste valeur;
- valeur de marché ≠ valeur comptable ≠ valeur nominale;
- rendement attendu ≠ rendement réalisé;
- coupon ≠ yield;
- échéance ≠ duration;
- risque ≠ volatilité;
- liquidité ≠ solvabilité;
- mesure risque-neutre ≠ distribution réelle des résultats;
- diversification ⇏ disparition de tout risque;
- sortie d’un modèle = résultat conditionnel aux hypothèses, pas fait observé.

## Portée v1

- actifs, passifs, claims, positions et portefeuilles;
- dette, capitaux propres, fonds, liquidités et dérivés au niveau conceptuel;
- temps financier, actualisation, capitalisation, échéance et courbe de taux;
- flux contractuels, attendus et contingents;
- prix, rendements et yields;
- risques de marché, crédit, contrepartie, liquidité, taux, inflation, change, modèle et concentration;
- mesures de sensibilité et de dispersion;
- valorisation par marché, revenus/DCF, coût, comparables, réplication et absence d’arbitrage;
- bases de mesure IFRS 9/IFRS 13 comme références de sémantique, sans faire de ce Kristal un corpus comptable.

## Frontière volontaire

Kristal-Finance n’est pas un terminal de marché, un conseiller financier, un moteur de trading, un pricer calibré, un portefeuille recommandé, un corpus fiscal ou juridique, ni une base de données de prix. Aucun prix courant, prévision, signal d’achat/vente, paramètre de trading ou recommandation personnelle n’est inclus.

## Reproductibilité

```bash
python knowledge-base/tools/build.py
python knowledge-base/tools/validate.py
python knowledge-base/tools/query.py --concept present-value
```

Les références externes sont cataloguées par URL et autorité. Les artefacts canoniques sont statiques, hashés et reconstruits déterministiquement.

## Kristal v9

Ce repo est migré vers **Kristal 9.0.0-draft.1 — Semantic State Architecture** sans supprimer les surfaces v6/v8 existantes.

- canon v9 : le state v6 canonique `knowledge-base/corpus/finance.kristal-state.json`;
- snapshot logique immuable : `.kristal/v9/state-snapshot.json`;
- matérialisation(s) : `.kristal/v9/materialization.*.json`;
- projection portable v6 : conservée sous `.kristal/v8/portable-state.kristal-state.json` et explicitement dérivée;
- indexes/read models v8 : restent dérivés et reconstruisibles;
- identité logique v9 : séparée des digests physiques des fichiers.

Voir `.kristal/v9/README.md` et `V9-MIGRATION.md`.
