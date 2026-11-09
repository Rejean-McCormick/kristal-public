# Modèle natif — Kristal-ElectricalEngineering

Le modèle déclaré par `.kristal/v9/domain-profile.json` est : **three-plane electrical knowledge graph**.

Axe canonique historique : `source → circuit → load, crossed by voltage/current/power/signal`.

## Distinctions à préserver

- physical plane
- circuit abstraction
- information/signal plane

## Supports locaux du modèle

Aucun fichier de support listé explicitement dans le profil v9.

L'unique artefact logique v9 importé possède le contrat `kristal.portable-epistemic-state/6.0` et porte le payload du portable state v6 original. La nouvelle structure n'aplatit pas les primitives du domaine.
