# Frontière de sécurité Spek → Wiki

Le paquet `spek.private-editorial-handoff/1.0` contient des empreintes et des
identifiants d'assertions privés, utiles à l'audit seulement.
`wiki_deploy.py` refuse désormais ses marqueurs internes s'ils apparaissent
dans les pages Wiki candidates. Aucun document privé ne devient publiable
parce qu'un script a pu le rendre en HTML ou Markdown.

La voie de publication exige toujours les reçus exacts de qualification et
les vérifications signées indépendantes C1/C2/C3 du Manager.
