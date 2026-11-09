# Modèle natif — Kristal-Agriculture

Type : `agroecosystem_interface_graph`.

Orientation / structure : **Sol → organisme cultivé → intrants → pratiques → rendement**.

Il faut respecter la structure historisée : ne pas transformer une trajectoire, un graphe multiplexe, un ledger ou une série de mesures contextualisées en une table générique non typée.

Le builder 3.2.2 travaille avec les payloads existants sous `canon/domain/` et conserve les Logical Contracts existants des membres State v9 :

- `agriculture.canonical-knowledge-state/1.0` — `urn:kristal:agriculture:artifact:canonical-state`
- `agriculture.identity-registry/1.0` — `urn:kristal:agriculture:artifact:identity-registry`
