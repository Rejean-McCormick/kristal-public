# Kristal-Internet v1.0.0

**Domaine :** Internet — couches, adressage, routage, protocoles et services  
**Statut :** `working`  
**Snapshot éditorial :** 2026-10-02  
**Langue principale :** français

## Axe canonique

`couches + adressage + routage + protocoles + services`

Ces cinq termes sont des **axes** et non une chaîne causale unique. Le corpus décrit comment ils se relient tout en empêchant les confusions fréquentes entre nom, adresse, préfixe, route, numéro de port, protocole et service.

## Principes de modélisation

- Une **couche** situe une fonction de communication.
- L’**adressage** désigne les mécanismes d’identification/localisation nécessaires à la livraison, principalement MAC/IP selon la portée.
- Le **routage** sélectionne et propage des chemins vers des préfixes; il dépend de politiques et d’un état courant.
- Un **protocole** définit des formats, états et comportements d’échange.
- Un **service** est une capacité offerte à d’autres systèmes ou utilisateurs; il peut dépendre de plusieurs protocoles.
- Les **noms**, **ports**, **propriétés de sécurité** et **défaillances** sont modélisés comme axes auxiliaires.

## Garde-fous

`nom DNS ≠ adresse IP ≠ préfixe ≠ route ≠ port ≠ protocole ≠ service`

Une adresse valide n’implique pas qu’elle soit joignable. Une entrée de port IANA n’implique pas que le service réellement exécuté soit celui historiquement associé au port. Une annonce BGP n’est pas, à elle seule, une preuve d’autorisation d’origine.

Pour TLS 1.3, ce snapshot utilise **RFC 9846 (juillet 2026)** comme spécification de base courante; RFC 9846 a obsolété RFC 8446 tout en conservant TLS 1.3.

## Contenu

Voir `knowledge-base/corpus/index.json` pour les comptes calculés, `corpus/internet.kristal-state.json` pour l’état Kristal v6 et `sources/source_catalog.json` pour les références normatives.

## Validation

```bash
cd knowledge-base
python tools/build.py
python tools/validate.py
python -m unittest tests/test_model.py
```

Le build est déterministe à partir des fichiers `sources/*.json`.
