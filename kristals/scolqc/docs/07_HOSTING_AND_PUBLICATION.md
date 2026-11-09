# Hosting, publication et activation

La normalisation locale n'effectue aucune publication et aucune activation.

Les responsabilités restent séparées :

`KNOWLEDGE != BUILD != MATERIALIZATION != BACKUP != HOSTING != PUBLICATION != ACTIVATION`

`build-v9` crée un candidat local. `publish-v9` publie un snapshot immuable précis. `activate-v9` déplace explicitement un canal vers un état déjà publié.

L'hébergement GitHub v10, s'il est ajouté plus tard, doit rester une enveloppe de transport et de cycle de vie. Il ne doit ni modifier les Logical Commitments, ni absorber les octets du Source Store dans l'état logique, ni devenir nécessaire pour lire le Kristal localement.

La capsule IA portable est désactivée dans ce workspace tant qu'elle n'est pas demandée et qualifiée séparément.
