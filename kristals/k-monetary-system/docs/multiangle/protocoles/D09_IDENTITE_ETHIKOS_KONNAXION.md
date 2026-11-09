# D09 — Guichets de confiance, Ethikos, Konnaxion : frontières de système
**Sources : S06, S08 et canon Smart Vote external interface. Cadre : W17.**

## Quatre services S06, avec autorités distinctes
(1) authentification haute assurance, (2) examen supervisé et certificat de compétence, (3) actes notariés standards par professionnels habilités, (4) dons à impact mesuré. Les caisses ne deviennent pas automatiquement autorités de certification, notaires ou organismes de bienfaisance. Chacun exige une habilitation et un contrat propres.

## Traitement technique
- La caisse transmet une **attestation bornée** d'identité, non un dossier bancaire ni une identification réutilisable à volonté.
- Biométrie uniquement si nécessaire, libre, limitée et avec option alternative; le seul consentement ne suffit pas [W17].
- Un examen peut prouver la réussite d'une épreuve; l'équivalence professionnelle n'existe que si une autorité compétente la reconnaît.
- Smart Vote/Ethikos est une **interface externe** : `request_id`, `member_verified`, `scope`, `eligible_choices`, `vote_receipt`, `audit_ref`, `appeal_ref`; pas d'appropriation de sa base électorale.

## Modèle de menace
Création de comptes fictifs, membre exclu numériquement, biométrie compromise, vote altéré, client croyant recevoir acte notarié sans notaire, conservation excessive des données bancaires, preuve cryptographique non interprétable.

## Réussite observable
Contrôle externe des identités, audits de sécurité, taux d'accès pour publics non numériques, erreurs corrigées, délai de contestation, absence de couplage abusif entre données de vote et données financières.
