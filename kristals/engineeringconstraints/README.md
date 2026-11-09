# Kristal EngineeringConstraints 1.0.0

Kristal EngineeringConstraints est un corpus statique de **raisonnement de conception et d’ingénierie système**. Son axe principal est :

**besoin → exigences → architecture → compromis → vérification**

Le corpus formalise la transformation d’un problème ou besoin en exigences traçables, la structuration d’une solution, l’exploration de compromis et l’établissement de preuves de conformité.

## Périmètre

Cinq axes canoniques : **besoin, exigences, architecture, compromis, vérification**.

La **validation** est incluse comme concept frontière uniquement pour la distinguer de la vérification : vérifier porte sur la satisfaction d’exigences spécifiées; valider porte sur l’adéquation au besoin et à l’usage prévu.

Ce Kristal n’est pas un code de construction, un guide de dimensionnement, un catalogue de composants, un solveur d’optimisation ni un référentiel réglementaire. Les disciplines spécialisées peuvent l’utiliser comme grammaire commune sans lui céder leur contenu métier.

## État

- Kristal Standard **v6** (`kristal_state`)
- corpus **1.0.0**
- 185 référents
- 474 assertions atomiques
- 5 sources de référence / synthèse
- validation JSON Schema + audit de graphe + manifeste SHA-256

## Fichiers principaux

- `knowledge-base/corpus/engineeringconstraints.kristal-state.json` — état canonique v6
- `knowledge-base/corpus/engineeringconstraints.referent-registry.json` — identités stables
- `knowledge-base/corpus/traceability-model.json` — chaîne besoin→preuve et règles de traçabilité
- `knowledge-base/corpus/tradeoff-model.json` — structure d’une étude de compromis
- `knowledge-base/corpus/verification-model.json` — méthodes, cas et statuts de vérification
- `knowledge-base/corpus/domain-coverage.json` — couverture et exclusions
- `knowledge-base/sources/source-catalog.json` — provenance documentaire
- `knowledge-base/tools/validate.py` — validation complète
- `knowledge-base/tools/query.py` — requête locale simple

## Invariants critiques

1. **Besoin ≠ exigence.** Un besoin motive; une exigence formalise une obligation vérifiable.
2. **Exigence ≠ décision de conception.** Le « quoi » et le « moyen retenu » restent distingués, sauf contrainte de conception explicite.
3. **Architecture ≠ description d’architecture.** Le système et l’artefact qui le décrit ne sont pas confondus.
4. **Contrainte dure ≠ préférence pondérée.** Une contrainte obligatoire ne devient pas compensable par simple pondération.
5. **Score ≠ décision.** Les hypothèses, critères, incertitudes et règles de sélection demeurent visibles.
6. **Test ≠ vérification.** Inspection, analyse, démonstration et test sont des méthodes possibles selon l’exigence.
7. **Vérification ≠ validation.** La première établit la conformité aux exigences; la seconde évalue l’adéquation au besoin / usage prévu.
8. **Pass ≠ preuve.** Une conclusion de conformité doit référencer une preuve objective et des critères.
9. **Changement ⇒ analyse d’impact.** Une modification peut invalider architecture, exigences ou preuves antérieures.

## Validation

```bash
cd knowledge-base
python tools/validate.py
python tools/audit_graph.py
python tools/query.py --topic tradeoff
```
