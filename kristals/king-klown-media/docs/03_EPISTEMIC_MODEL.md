# Modèle épistémique

## Régimes d'information

Le paquet distingue les connaissances canoniques, les déclarations explicites mais non gouvernantes, les propositions et les informations provenant du catalogue média. L'absence d'une donnée n'implique pas qu'elle soit fausse.

## Provenance épistémique

La provenance est conservée dans le noyau épistémique, les sources emballées, les pins de catalogues externes et les clarifications du créateur. Une source et une autorité ne sont pas synonymes.

## Autorité

Ordre explicitement conservé par la reader policy : `current explicit creator clarification > DECISIONS > CANON > current canonical source > source branch > media catalog > interpretation`. UCKK Médiathèque est l'autorité primaire pour l'inventaire brut média/URL ; King Klown possède les relations sémantiques emballées ici.

## Incertitude / conflits / inconnus

Les contradictions sont conservées dans un artefact distinct. Les cas partiels ou manquants restent partiels/manquants ; ils ne sont pas complétés par inférence silencieuse.

## Provenance de build

La derivation informatique historique reste sous `.kristal/v9/derivations/`. La normalisation 3.2.2 ajoute une enveloppe d'authoring et copie byte-identiquement les artefacts canoniques vers `canon/artifacts/`; elle ne constitue pas une nouvelle preuve épistémique.

## Politique des sorties IA

Les sorties IA sont `proposal_only` jusqu'à validation explicite et ne sont jamais autorité par elles-mêmes.
