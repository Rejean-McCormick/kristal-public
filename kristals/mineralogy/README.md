# Kristal-Mineralogy v1.0.0

**Composition + structure cristalline → propriétés → occurrence.**

Kristal-Mineralogy décrit des espèces minérales comme des objets définis conjointement par leur composition chimique et leur organisation cristalline, puis relie cette identité à des propriétés observables et à des contextes géologiques d’occurrence.

## Noyau conceptuel

```text
Composition chimique ─┐
                      ├──> Espèce minérale ──> Propriétés ──> Occurrences / associations
Structure cristalline ┘
```

Le modèle distingue explicitement :

- **composition nominale** et **identité minérale**;
- **système cristallin**, **réseau de Bravais** et **motif/structure**;
- **polymorphisme** et **solution solide**;
- **propriété diagnostique** et **preuve d’identité**;
- **occurrence géologique** et **définition de l’espèce**.

## Portée v1

- 7 systèmes cristallins et 14 réseaux de Bravais (référence IUCr);
- grandes classes compositionnelles;
- motifs structuraux utiles aux minéraux communs;
- propriétés macroscopiques et structurales;
- contextes d’occurrence;
- sous-ensemble représentatif de minéraux communs et géologiquement importants;
- polymorphes et séries de solution solide exemplaires;
- contexte nomenclatural figé sur la liste IMA-CNMNC de septembre 2026.

## Hors portée volontaire

Ce Kristal n'est pas une copie exhaustive de la master list IMA, un atlas de localités, une base de gisements économiques, une pétrologie exhaustive, ni une base complète de groupes d’espace/diffraction. Ces couches peuvent être ajoutées sans modifier le noyau.

## Reproductibilité

```bash
python knowledge-base/tools/build.py
python knowledge-base/tools/validate.py
python knowledge-base/tools/query.py --concept calcite
```

Les sources distantes sont cataloguées par métadonnées. Les artefacts canoniques sont reconstruits déterministiquement et couverts par SHA-256.
