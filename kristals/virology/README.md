# Kristal-Virology v1.0.0

**Cycle viral** — génome → particule → hôte → entrée → réplication → transmission.

Kristal-Virology décrit les invariants conceptuels du cycle viral sans se transformer en protocole expérimental. Il représente séparément l'information génétique, la particule virale, l'hôte organisme, la cellule hôte, l'entrée cellulaire, la réplication intracellulaire, les états d'infection et la transmission entre hôtes.

## Noyau conceptuel

```text
ViralGenome → Virion → Host/HostCell
                       ↓
               Attachment → Entry → Uncoating
                       ↓
        Gene expression ↔ Genome replication
                       ↓
          Assembly → Maturation → Release
                       ↓
              Between-host transmission
```

## Distinctions non négociables

- **génome ≠ virion ≠ infection ≠ maladie**;
- **hôte organisme ≠ cellule hôte**;
- **susceptibilité ≠ permissivité**;
- **entrée cellulaire ≠ transmission entre hôtes**;
- **classe de Baltimore ≠ taxonomie ICTV**;
- **cycle productif ≠ infection persistante/latente/abortive**.

## Portée v1

- 7 classes de Baltimore comme stratégies d'information/réplication;
- ADN/ARN, simple/double brin, polarité, segmentation/topologie comme propriétés séparables;
- virion, capside, enveloppe, nucléocapside et architectures générales;
- grands groupes d'hôtes cellulaires;
- attachement, entrée, décapsidation, expression, réplication, assemblage, maturation, libération;
- susceptibilité, permissivité, gamme d'hôtes et tropisme;
- états productif, abortif, persistant, latent, lytique et lysogénique;
- grandes voies de transmission et chaîne de transmission;
- métadonnées figées de l'ICTV **Virus Taxonomy: 2025 Release / MSL #41**.

## Hors portée volontaire

Ce Kristal n'embarque **aucun protocole de culture virale, paramètres de laboratoire, séquences, amorces, plans d'ingénierie, optimisation de réplication ou procédures de modification d'hôte/virus**. Il n'est pas non plus une pharmacopée antivirale, un guide clinique, une base de surveillance épidémiologique temps réel ni un miroir exhaustif des 17 554 espèces de l'ICTV 2025.

## Reproductibilité

```bash
python knowledge-base/tools/build.py
python knowledge-base/tools/validate.py
python knowledge-base/tools/query.py --concept virion
```

Les sources distantes sont cataloguées par métadonnées; leur texte intégral n'est pas embarqué. Les artefacts canoniques sont reconstruits de façon déterministe et couverts par SHA-256.
