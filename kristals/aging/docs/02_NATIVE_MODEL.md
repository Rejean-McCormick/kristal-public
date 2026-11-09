# Modèle natif — Kristal-Aging

Type : `temporal_trajectory_graph`.

Orientation / structure : **Mécanismes → réserve → stress → résilience → fonction → compensation → trajectoire observée**.

Il faut respecter la structure historisée : ne pas transformer une trajectoire, un graphe multiplexe, un ledger ou une série de mesures contextualisées en une table générique non typée.

Le builder 3.2.2 travaille avec les payloads existants sous `canon/domain/` et conserve les Logical Contracts existants des membres State v9 :

- `aging.canonical-knowledge-state/1.0` — `urn:kristal:aging:artifact:canonical-state`
- `aging.identity-registry/1.0` — `urn:kristal:aging:artifact:identity-registry`
