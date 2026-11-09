# K Monetary System — Socio-Monetary Transition Model

**Status:** `building`  
**Workspace:** `kristal.authoring-workspace/3.0.0`  
**Semantic state:** Kristal v9  
**Hosted network:** Kristal v10

This Kristal is a **hypothetical executable socio-monetary transition model**, not a forecast, political program, legal opinion, or claim that the modeled transition will occur.

Its native form is deliberately hybrid:

```text
multiplex domain model
+ monetary constitution
+ transition statechart
+ causal hypothesis graph
+ append-only event memory
+ executable policy contracts
+ epistemic research memory
```

The Kristal owns the K-system design. It **references but does not own** Konnaxion Smart Vote / EkoH.

## Core distinction

```text
K_M = K-Money: payment / settlement / candidate unit of account
K_C = K-Capital: broad capital-ownership / social-dividend layer
```

The separation avoids forcing one instrument to be simultaneously stable money and a speculative appreciating capital asset.

## Canon

- `canon/domain/` — what the modeled system is
- `canon/operations/` — how the modeled system may operate
- `canon/epistemic/` — what is assumed, hypothesized, evidenced, disputed or unresolved
- `canon/state.index.json` — registered Logical Artifacts

Derived simulation output belongs outside canon unless explicitly promoted through review.

## Local validation/build

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
python runtime/kms_simulator.py --years 10
```

```text
MODEL OUTPUT != AUTHORITY
REFERENCE != OWNERSHIP
BUILD != PUBLISH != ACTIVATE
```

## Dépôt consolidé (2 novembre 2026)

Cette distribution est un **dépôt complet**, pas un overlay. Les 36 artefacts
logiques sont déjà enregistrés dans `canon/state.index.json` : 17 artefacts
initiaux et 19 artefacts multiangles (14 propositions D01–D14 et 5 registres).
Les 14 protocoles demeurent **candidats** sans autorité d'exécution ni validation
économique ou juridique implicite.

- `docs/multiangle/protocoles/` : lecture humaine des protocoles D01–D14.
- `canon/*/multiangle/` : artefacts natifs et traçabilité.
- `sources/multiangle/` : registre de 12 identités documentaires (11 fichiers
  distincts, S12 étant une copie identique de S06) et références publiques.
- `validation/CONTROLES_REPO_2026-11-02.md` : résultats des tests du dépôt nettoyé.
- `REINSTALLATION_ET_NETTOYAGE.md` : instruction simple pour repartir proprement.

Le répertoire `build/v9` inclus dans cette **distribution ZIP** est dérivé,
recalculé et vérifié. Il reste ignoré par Git selon `.gitignore` et peut être
reconstruit plus tard avec `python tools/kristal.py build-v9 .`. Aucune commande
n'est requise pour simplement décompresser et consulter cette distribution.

**Aucune publication ni activation réseau n'a été effectuée.**
