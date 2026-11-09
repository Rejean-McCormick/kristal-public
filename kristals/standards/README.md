# Kristal-Standards v1.0.0

Corpus statique et validé décrivant la grammaire **objet normalisé → exigence → méthode → conformité → organisme/version**.

## Noyau conceptuel

- **Objet normalisé** : produit, processus, service, système, interface, protocole, format, compétence, organisation.
- **Exigence** : obligation normative, performance, sécurité, interface, documentation, tolérance, critère d’acceptation et applicabilité.
- **Méthode** : essai, inspection, mesure, étalonnage, échantillonnage, audit, calcul, simulation, validation/vérification de méthode.
- **Conformité** : sélection, détermination, revue, décision, attestation, certification, accréditation, surveillance et statut.
- **Organisme** : organisme de normalisation, comité, groupe de travail, laboratoire, organisme de certification, organisme d’accréditation et autorité réglementaire.
- **Version** : identifiant, édition, révision, amendement, corrigendum, projet, publication, confirmation, remplacement et retrait.

## Invariant central

Une conclusion de conformité n’est pas une propriété absolue de l’objet. Elle doit être interprétée par rapport à un **objet**, un **périmètre**, un **référentiel versionné**, des **exigences applicables**, des **méthodes**, des **résultats**, une **règle de décision** et, lorsque pertinent, une **période de validité**.

## Garde-fous majeurs

- norme ≠ règlement technique ;
- conformité à une norme ≠ conformité réglementaire ;
- essai ≠ certification ;
- certification ≠ accréditation ;
- preuve ≠ décision ;
- certificat ≠ propriété éternelle de l’objet ;
- clause informative ≠ exigence normative ;
- recommandation ≠ obligation ;
- projet ≠ publication finale ;
- méthode normalisée ≠ méthode automatiquement valide pour tout usage ;
- amendement ≠ révision ≠ corrigendum ;
- référence datée ≠ référence non datée ;
- organisme de normalisation ≠ autorité réglementaire.

## Taille

- Référents : **251**
- Assertions atomiques : **863**
- Sources : **10**

## Organisation

Le fichier canonique est `knowledge-base/corpus/standards.kristal-state.json`. Des modèles spécialisés décrivent la chaîne normative, le couplage exigence-méthode, l’évaluation de conformité, le cycle documentaire et les rôles institutionnels.

## Statut

Référence statique v1.0.0. Le corpus ne contient ni texte intégral de normes propriétaires, ni statut dynamique d’un certificat réel, ni avis juridique.
