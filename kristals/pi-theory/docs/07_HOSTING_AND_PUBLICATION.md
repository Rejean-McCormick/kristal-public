# Hosting, publication et activation

La normalisation 3.2.2 n'ajoute aucune configuration d'hébergement v10 et n'effectue aucune publication ni activation.

L'ancien `.kristal/v9/activation.json` est conservé comme artefact de la couche de compatibilité antérieure ; il ne constitue pas une nouvelle activation effectuée par le workflow 3.2.2.

Pour une publication future, conserver les séparations suivantes :

`KNOWLEDGE != BUILD != MATERIALIZATION != BACKUP != HOSTING != PUBLICATION != ACTIVATION`.

Toute publication réseau doit être qualifiée sur un commit exact, puis activée seulement sur demande explicite.
