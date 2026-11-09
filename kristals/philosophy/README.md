# Kristal-Philosophy

**Édition 1.0.0 — Kristal v6 natif**

Kristal-Philosophy décrit la philosophie comme **espace de problèmes et de positions**, organisé par une chaîne dialectique explicite :

```text
question
   ↓
thèse
   ↓ soutenue par
argument
   ↓ contesté par
objection
   ↓ traitée par
réponse
   ↓ située historiquement dans / près de
tradition
```

La structure ne choisit pas automatiquement un « gagnant ». Elle conserve les désaccords et rend les relations entre positions interrogeables.

## Couverture

- **16 problèmes canoniques**;
- **176 référents** bilingues FR/EN;
- **373 assertions atomiques**;
- **21 sources de référence**.

Domaines couverts : épistémologie, métaphysique, philosophie de l'esprit, éthique, métaéthique, philosophie des sciences, philosophie du langage, philosophie de la religion, esthétique et philosophie du sens.

## Fichiers principaux

- `corpus/philosophy.kristal-state.json` — état canonique v6;
- `corpus/dialectics.json` — vue directe `question → thèse → argument → objection → réponse → tradition`;
- `corpus/referents.json` — vocabulaire bilingue;
- `corpus/invariants.json` — règles empêchant l'aplatissement des controverses;
- `corpus/boundaries.json` — frontières avec History, Logic/Math, Religion, Psychology, Science et PoliticalPhilosophy;
- `sources/source-catalog.json` — ancrages savants;
- `validation/validation-report.json` — validation structurelle, référentielle, de preuve et dialectique;
- `manifest.sha256.json` — intégrité de l'édition.

## Principe éditorial

Le fait qu'une position soit célèbre, ancienne ou associée à une tradition ne lui confère aucun statut de vérité automatique. Le corpus encode **qui répond à quelle question, avec quels arguments, quelles objections et quelles réponses**, puis situe cette dialectique dans des traditions sans transformer celles-ci en blocs doctrinaux homogènes.
