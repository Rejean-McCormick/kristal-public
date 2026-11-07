# Modèle natif — Kristal-Accounting

Type : `accounting_event_ledger_graph`.

Orientation / structure : **Événement économique → reconnaissance/mesure → écriture → compte/livre → période → état financier**.

Il faut respecter la structure historisée : ne pas transformer une trajectoire, un graphe multiplexe, un ledger ou une série de mesures contextualisées en une table générique non typée.

Le builder 3.2.2 travaille avec les payloads existants sous `canon/domain/` et conserve les Logical Contracts existants des membres State v9 :

- `accounting.canonical-knowledge-state/1.0` — `urn:kristal:accounting:artifact:canonical-state`
- `accounting.identity-registry/1.0` — `urn:kristal:accounting:artifact:identity-registry`
