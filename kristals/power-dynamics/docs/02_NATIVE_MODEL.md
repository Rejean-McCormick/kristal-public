# Modèle natif

## Primitives du domaine

Le modèle combine des référents conceptuels stables avec des assertions séparées (libellés, alias, définitions éditoriales ou sourcées, positions, relations, contextes), ainsi que des objets analytiques Power Dynamics structurés. Les contrats natifs couvrent notamment `PowerRelation`, `AuthorityScope`, conversions, boucles, événements dynamiques, domaines, routages, surfaces, reconnaissance/coordination et profils de système.

## Relations / transformations

Les graphes de taxonomie, relations sémantiques et relations contextuelles sont distingués. Les relations dynamiques Power Dynamics restent attribuées à leurs sources et ne sont pas fusionnées silencieusement avec les relations statiques générales. Le builder déterministe compile ces couches dans l'état structuré.

## Dimensions internes

Le corpus emploie des dimensions typées et à cardinalité explicite. Power Dynamics ajoute des dimensions portant notamment sur l'état ontologique, les processus dynamiques, le routage, les possibilités effectives, la maturité des preuves et les types de claims.

## Forme native retenue

`layered_structured_epistemic_state_with_native_power_dynamics_contracts`

Cette forme est volontairement **layered** : elle conserve simultanément référents, assertions, provenance, graphes, configurations, contrats analytiques et distinctions épistémiques.

## Logical Contract v9

Le membre canonique est :

- Artifact ID : `urn:kristal:power:canonical-state`
- Contract : `structured_epistemic_state/5.0`
- Physical source : `knowledge-base/corpus/power-topology.structured-epistemic-state.json`

Le registre `canon/state.index.json` enveloppe ce contrat sans imposer une nouvelle ontologie universelle.

## Alternatives rejetées

Une simple taxonomie ou un graphe générique unique ferait perdre les distinctions entre document source, définition, objet analytique, assertion compilée, statut épistémique et preuve. Une conversion destructive n'est donc pas retenue.
