# Kristal-Manufacturing v1.0.0

Corpus statique de référence pour la fabrication, centré sur la chaîne **matière brute → procédé → géométrie → tolérance → pièce → contrôle qualité**.

Dimensions transversales : **état matière**, **capabilité du procédé**, **métrologie**, **règle de décision** et **traçabilité**.

## Contenu

- 877 assertions Kristal v6
- 447 référents
- 59 procédés de fabrication
- 29 paramètres de procédé
- 16 types d’entités géométriques
- 21 concepts de tolérance/GPS
- 21 méthodes de mesure/inspection
- 35 concepts de contrôle qualité
- 17 sources externes référencées

## Principe de lecture

Une pièce n’est pas décrite uniquement par sa forme finale. Le Kristal conserve la chaîne qui relie **matière et lot**, **état matière**, **opérations et paramètres**, **définition nominale**, **tolérances**, **mesures**, **incertitude**, **règle de décision** et **preuve de conformité**.

Trois séparations sont obligatoires :

1. `nominal_geometry != actual_geometry != measurement_result`;
2. `tolerance != measurement_uncertainty`;
3. `nonconformance != defect != fitness_for_use`.

## Validation

```bash
python knowledge-base/tools/validate.py
```

## Frontières

La v1.0.0 n’embarque ni tables machines/fournisseurs, ni paramètres de coupe recommandés, ni texte propriétaire des normes ISO/ASME. Les exigences sectorielles et les données MES/QMS vivantes doivent être versionnées séparément.
