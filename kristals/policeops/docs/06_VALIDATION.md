# Validation du domaine et lifecycle

## Validateurs existants

```bash
python knowledge-base/tools/validate.py
```

Attendu sur ce snapshot : 538 assertions; schéma, hashes de contenu, reader policies et contrat source-resolution valides; baseline de matérialisation : 17 sources utilisables, 1 en quarantaine, 6 ignorées.

## Local Kit 3.2.2

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
```

`check` établit la cohérence structurelle du workspace, pas la vérité juridique ou institutionnelle. Le lifecycle reste `building` tant que le corpus natif déclare `artifact_status=working`, `validation_status=not_evaluated` et `recognition_status=under_review`.

## Critères avant publication

- réexaminer les transitions judiciaires contre des sources versionnées;
- résoudre/documenter les sources sans canal d’autorité;
- disposer du Source Store physique si une vérification byte-level complète est requise;
- qualifier le commit exact avec l’outil de qualification approprié;
- publier sans activer implicitement.
