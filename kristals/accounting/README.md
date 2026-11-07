# Kristal-Accounting v1.0.0

Corpus statique de référence en comptabilité, centré sur le modèle :

**événement économique → écriture → compte → période → état financier**

Le noyau ajoute reconnaissance, mesure, débit/crédit, grand livre, ajustements de clôture, devise, référentiel et piste d’audit.

## Taille
- 581 assertions Kristal v6
- 289 référents
- 9 sources externes + 1 modèle éditorial local
- 28 types d’événements économiques
- 20 comptes génériques
- 9 bases de mesure
- 11 types d’ajustement
- 15 types de pièces justificatives

## Principe de lecture

Le Kristal conserve séparément le fait économique, sa preuve, sa reconnaissance, l’écriture qui le représente, les comptes touchés, les dates pertinentes, la période et le reporting final.

Les quatre distinctions obligatoires sont :

1. `economic_event != source_document != journal_entry`;
2. `journal_entry != cash_flow`;
3. `debit != universal_increase` et `credit != universal_decrease`;
4. `ledger_account != financial_statement_line_item`.

## Référentiels

Le noyau est juridiction-neutre. IFRS sert de jeu de références pour tester éléments, reconnaissance, mesure, présentation, période, devise et revenu. IFRS 18 est marqué comme **émis mais obligatoire à compter des périodes annuelles ouvertes le 1er janvier 2027 ou après**.

## Validation
```bash
python knowledge-base/tools/validate.py
```

## Frontières

La v1 n’embarque aucun solde réel, aucune déclaration fiscale, aucun plan comptable légal local et aucune règle de comptabilisation spécifique à une entreprise. Les archétypes d’écritures servent à la sémantique, pas à autoriser des écritures réelles.

## Standardisation structurelle du 17 octobre 2026

L'enveloppe a été actualisée pour le **Kristal Authoring Kit v4.0.0-draft.2**, avec inventaire de migration vers le Framework v11. **Le contenu métier reste en v6 et le State v9 garde son engagement historique.** Il ne s'agit pas d'une conversion automatique de ses 581 assertions en KQ/KP/KA/KS.

- Voir [`docs/08_V11_STANDARDIZATION.md`](docs/08_V11_STANDARDIZATION.md) pour les invariants, le plan de migration et ses points bloqués.
- Voir [`derived/v11/readiness.json`](derived/v11/readiness.json) et [`derived/v11/lexical-inventory.json`](derived/v11/lexical-inventory.json) pour les référents et leurs libellés distincts.
- Vérification : `python tools/validate-standardization.py` ; reconstruction v9 sans publication : `python tools/build-preserving-v9.py`. Les caches de découverte sont à reconstruire à la demande avec `python tools/kristal.py build-discovery .` (non inclus dans le ZIP).
