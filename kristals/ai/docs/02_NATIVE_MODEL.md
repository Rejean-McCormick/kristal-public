# Modèle natif — Kristal-AI

Type : `ai_lifecycle_multi_axis_graph`.

Orientation / structure : **Données → représentation → modèle → apprentissage → inférence → évaluation**.

Il faut respecter la structure historisée : ne pas transformer une trajectoire, un graphe multiplexe, un ledger ou une série de mesures contextualisées en une table générique non typée.

Le builder 3.2.2 travaille avec les payloads existants sous `canon/domain/` et conserve les Logical Contracts existants des membres State v9 :

- `ai.canonical-knowledge-state/1.0` — `urn:kristal:ai:artifact:canonical-state`
- `ai.identity-registry/1.0` — `urn:kristal:ai:artifact:identity-registry`
