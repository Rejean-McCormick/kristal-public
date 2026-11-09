# Hosting v10 et publication

L'ajout du target `kristal.hosting/10.0` est une compatibilité d'enveloppe. Aucune cible GitHub / branche / commit / URL de déploiement n'est inventée. Aucun `publish-v9` ni `activate-v9` n'est déclenché.

La présence de `.kristal/v9/activation.json` est un artefact historique **préservé**, pas une nouvelle activation effectuée lors de cette migration.

L'état local est `validated`, non `released`. Toute publication ultérieure doit être qualifiée et viser un commit exact.
