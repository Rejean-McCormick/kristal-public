# Kristal-Logic v1.0.0

**Proposition → forme → inférence → validité.**

Kristal-Logic décrit la logique formelle comme une architecture à trois couches : syntaxe, sémantique et métalogique. Son cadre primaire est la logique classique propositionnelle et du premier ordre; les logiques non classiques sont référencées comme cadres distincts afin d'empêcher l'exportation automatique de règles classiques.

## Noyau conceptuel

```text
Proposition / formule
        │
        ▼
   forme logique
        │
        ▼
 règles d'inférence ──> dérivation (⊢)
        │
        ▼
 validité / conséquence sémantique (⊨)
        │
        ├── contre-modèle => invalidité
        └── validité + prémisses vraies => solidité
```

## Distinctions obligatoires

- vérité ≠ validité;
- formule ≠ proposition;
- syntaxe ≠ sémantique;
- implication matérielle `→` ≠ conséquence logique `⊨`;
- dérivabilité `⊢` ≠ conséquence sémantique `⊨`;
- validité ≠ solidité (`soundness` d'un argument);
- satisfiabilité ≠ validité;
- équivalence logique ≠ identité syntaxique;
- contre-exemple / contre-modèle ≠ simple désaccord avec la conclusion;
- induction et abduction ≠ validité déductive;
- règle valide en logique classique ≠ règle universelle pour toute logique.

## Portée v1

- logique propositionnelle classique;
- connecteurs, tables de vérité et formes normales CNF/DNF/NNF;
- logique du premier ordre : prédicats, termes, variables, quantificateurs, identité;
- modèles, satisfaction, satisfiabilité, conséquence sémantique et contre-modèles;
- déduction naturelle et principales règles d'inférence;
- preuve, dérivation, conséquence syntaxique, correction et complétude;
- validité, invalidité, solidité, cohérence et décidabilité;
- erreurs formelles représentatives;
- repères explicites pour logiques intuitionniste, modale, multivaluée, paraconsistante et de pertinence.

## Frontière volontaire

Kristal-Logic n'est pas un traité exhaustif de philosophie du langage, une base de rhétorique/fallacies informelles, un solveur SAT, un assistant de preuve, une bibliothèque de théorèmes mathématiques, ni une implémentation d'un calcul symbolique. Ces domaines peuvent être développés dans `Language`, `Argumentation`, `Computing`, `Math` ou des Kristals spécialisés sans modifier ce noyau.

## Reproductibilité

```bash
python knowledge-base/tools/build.py
python knowledge-base/tools/validate.py
python knowledge-base/tools/query.py --concept validité
```

Les artefacts canoniques sont statiques, hashés et reconstruits déterministiquement.
