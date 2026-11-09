# Modèle natif — Kristal-Astronomy

Type : `measurement_contextualized_object_graph`.

Orientation / structure : **Type → masse → distance → mouvement → rayonnement → formation → évolution → observation**.

Il faut respecter la structure historisée : ne pas transformer une trajectoire, un graphe multiplexe, un ledger ou une série de mesures contextualisées en une table générique non typée.

Le builder 3.2.2 travaille avec les payloads existants sous `canon/domain/` et conserve les Logical Contracts existants des membres State v9 :

- `astronomy.canonical-knowledge-state/1.0` — `urn:kristal:astronomy:artifact:canonical-state`
- `astronomy.identity-registry/1.0` — `urn:kristal:astronomy:artifact:identity-registry`
