# Hosting et publication v10

Le canon et ses Logical Commitments restent v9. L'hébergement est une couche v10 séparée.

## État actuel

Aucun host GitHub v10 n'est configuré par cette normalisation. Le paquet historique `.kristal/v9` contient déjà des métadonnées d'activation `production`; elles sont préservées comme état historique et ne sont pas interprétées comme une nouvelle publication du workspace Local 3.2.2.

## Publication future

Une publication doit viser le commit exact contenant l'état exporté. Le chemin recommandé côté nœud de collection est stable et relatif, par exemple `kristals/power-dynamics/state/state-snapshot.json`.

## Qualification

La qualification réseau doit viser exactement le commit à publier. Backup/inventaire, hosting, publication et activation restent séparés du contenu logique.

## Activation

L'activation est optionnelle et explicite. Une release publiée ne devient jamais automatiquement l'état actif d'un channel.
