# Modèle natif

- **Kind** : `controlled_source_catalog`
- **Description** : Registre contrôlé des fournisseurs, sources de référence et règles explicites d’acquisition.
- **Axes et coordonnées** : Fournisseurs, références et règles d’acquisition (trois membres distincts).
- **Invariant** : Un fournisseur ou une source ne devient pas une vérité nutritionnelle par son inscription au catalogue.

## Canal canonique de migration

Le Logical Artifact `urn:kristal:foodbrands:canonical` possède le contrat `foodbrands.source-catalog/1.0`. Son payload authoring se trouve dans `canon/domain/foodbrands.logical-payload.json` et est recalculé sans commitment `precomputed`.

Les modèles métier historiques sont dans `knowledge-base/` : leur forme native demeure autoritaire pour l'interprétation ; la seule enveloppe 3.2.2 ne redéfinit pas les sémantiques.
