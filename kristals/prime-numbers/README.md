# Kristal — Mécanique de la primalité

**Version:** 1.0.0  
**Sujet:** `KQ1001` — Mécanique de la primalité  
**Projection:** v6-compatible, orientée par Kristall v7

## Invariant

`Prime(n)` est traité comme une identité sémantique unique :

```text
Prime(n) ⇔ n>1 et il n'existe pas a,b>1 tels que n=a·b.
```

Le Kristal est polymorphe : les formulations par diviseurs, borne √n, totient, corps résiduel, absence de diviseurs de zéro, Wilson et complément de l'image multiplicative sont encodées comme **caractérisations équivalentes** du même invariant.

Fermat est encodé séparément comme **conséquence nécessaire non suffisante**. Les méthodes (division d'essai, crible, Miller–Rabin, AKS) sont encodées comme **opérationnalisations**, non comme définitions.

## Axes

- **Primaire — `KQ2001` Irréductibilité multiplicative** (`Structural / hierarchical`) : ce qui fait intrinsèquement qu'un entier est premier.
- **Secondaire — `KQ2002` Témoin et certification** (`Epistemic / evidence`) : comment la compositeness ou la primalité est établie.

## Mécanique globale

```text
C = {a·b | a,b∈ℕ, a>1, b>1}
P = ℕ_≥2 \ C
```

Le crible est la projection dynamique de cette mécanique : les premiers déjà cristallisés génèrent des multiples composés; tout entier qui échappe à cette couverture est un nouveau premier et devient à son tour générateur.

## Fichiers

- `manifest.json` — descripteur Kristall v7.
- `formal-core.json` — noyau compact lisible par machine/humain.
- `registries/` — entités, propriétés, assertions, familles, axes, Mesh, KOS, TOC, sources.
- `projection-recipe.json` — recette de projection à deux axes.
- `projection/kristal-primalite-mecanique.v6.json` — Kristal portable v6.
- `records/crystallization.json` — trace de cristallisation.
- `validation-report.json` — validation contre les schémas fournis dans le paquet de référence.
