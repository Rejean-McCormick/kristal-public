# Instructions IA locales — Kristal-PiTheory / Local Kristal 3.2.2

Ce dépôt conserve un corpus Pi Theory déjà formalisé. Toute modification doit préserver la séparation entre mécanique, structure, interprétation ontologique, limites épistémiques, résonances, historique et validation.

## Règles impératives

1. Ne jamais réécrire silencieusement `knowledge-base/corpus/pi-theory.kristal-state.json` ni les autres ressources canoniques historiques.
2. `Pi v13 (3).md` est l'ancre éditoriale actuelle pour les limites de revendication; `Pi Theory with maths (1).docx` reste l'ancre du ledger mécanique, selon la politique de sources existante.
3. Une interprétation n'est pas une sortie mécanique; une résonance n'est pas une preuve; une exécution reproductible ex post n'est pas un préenregistrement historique.
4. Les anciennes formulations fortes restent de la provenance historique lorsqu'elles sont déclarées supersédées.
5. Les sorties IA sont des propositions ou dérivés; elles ne créent aucune autorité.
6. Préserver les IDs d'assertions, référents, sources, Logical Artifacts et `state_ref` existants sauf décision canonique explicite.
7. Ne jamais confondre Logical Commitment, Blob Digest, build, materialization, backup, hosting, publication et activation.
8. `.kristal/v8/`, `.kristal/v9/`, `build/`, `views/ai-contexts/` et les rapports/index déclarés dérivés ne deviennent pas canon par simple présence.

## Canon v9 de la couche 3.2.2

`canon/state.index.json` enregistre deux Logical Artifacts v9 préexistants, copiés octet pour octet sous `canon/logical/`. Ils conservent les engagements v9 déjà validés et lient les ressources historiques du corpus sans les réécrire.

## Séquence de travail

```text
modifier le canon seulement avec provenance/autorité explicites
→ exécuter le validateur métier
→ exécuter les tests métier
→ tools/kristal.py check
→ tools/kristal.py build-v9
→ vérifier les Logical Commitments
```

Ne pas publier ni activer implicitement. La capsule IA portable est désactivée dans ce workspace tant qu'elle n'est pas demandée explicitement.
