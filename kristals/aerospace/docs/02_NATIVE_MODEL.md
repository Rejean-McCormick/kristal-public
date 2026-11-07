# Modèle natif — Kristal-Aerospace

Type : `mission_system_relational_graph`.

Orientation / structure : **Mission → phase → configuration véhicule → environnement → trajectoire → systèmes → opérations**.

Il faut respecter la structure historisée : ne pas transformer une trajectoire, un graphe multiplexe, un ledger ou une série de mesures contextualisées en une table générique non typée.

Le builder 3.2.2 travaille avec les payloads existants sous `canon/domain/` et conserve les Logical Contracts existants des membres State v9 :

- `aerospace.canonical-knowledge-state/1.0` — `urn:kristal:aerospace:artifact:canonical-state`
- `aerospace.identity-registry/1.0` — `urn:kristal:aerospace:artifact:identity-registry`
