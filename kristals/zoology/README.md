# Kristal-Zoology v1.0.0

**Plans corporels + lignées + adaptations**

Corpus statique et reconstruisible décrivant la diversité animale sur trois axes complémentaires :

`lignée ↔ plan corporel ↔ adaptation`

avec des taxons exemplaires, contextes d'habitat, convergences et incertitudes explicites.

## Contenu

- **66** lignées zoologiques majeures
- **52** caractères de plans corporels
- **64** adaptations fonctionnelles
- **37** taxons exemplaires
- **619** relations structurées
- **3** groupes de convergence
- **3** dossiers d'incertitude phylogénétique/interprétative

## Principe éditorial

Un taxon n'est pas défini par une liste rigide de caractères. Chaque association de plan corporel est qualifiée; les pertes secondaires, convergences et exceptions restent représentables.

Le snapshot taxonomique nominal est fixé au **Catalogue of Life 2026-09-25 XR**. Le corpus ne se met jamais à jour silencieusement.

## Validation

```bash
cd knowledge-base
python tools/validate.py
python -m unittest discover -s tests -v
```

Statut : `working` — validation structurelle et éditoriale, sans prétention de reconnaissance externe.
