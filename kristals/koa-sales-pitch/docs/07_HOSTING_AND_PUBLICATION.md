# Hosting et publication v10

Le canon et les commitments restent v9. L'hébergement est une couche v10 séparée.

## Node / repository

Aucun nœud GitHub n'est configuré par cette normalisation. Le choix du dépôt de collection doit être explicite et peut héberger plusieurs Kristals lorsque permissions et lifecycle sont communs.

## State path

Utiliser un chemin stable et relatif au repo, par exemple `kristals/koa-sales-pitch/state/state-snapshot.json`.

## Qualification

La qualification doit viser le commit exact contenant l'état exporté. Un `check` local ne remplace pas cette qualification réseau.

## Publication

La publication produit un bundle vérifiable et une Release immuable. Elle ne modifie pas le Logical Commitment v9.

## Activation

L'activation reste séparée et optionnelle. Aucun channel ne doit être modifié implicitement lors d'une normalisation, d'un build ou d'une publication.
