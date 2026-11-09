# Modèle épistémique

## Régimes d’information

Le corpus distingue actuellement 219 assertions `sourced`, 313 `claimed` et 6 `reviewed`. Les niveaux de certitude déclarés sont 141 `high` et 397 `medium`. Ces niveaux ne représentent pas des seuils juridiques.

## Validation et reconnaissance

Le `validation_summary` natif indique `validation_status=not_evaluated` et `recognition_status=under_review`. La réussite des validateurs structurels ne change pas ces statuts.

## Provenance et autorité

Une source et une provenance documentent d’où vient une information; elles ne suffisent pas à lui conférer une autorité normative. Les canaux d’autorité sont conservés lorsqu’ils existent, et leur absence reste explicite.

## Conflits / inconnus

La baseline déclare notamment `disagreement_preserved`. Les absences de source, d’autorité ou de représentation physique ne doivent pas être transformées en `false` ni en assertions inventées.

## Provenance de build

Les `.kristal/v8`, `.kristal/v9` et `build/v9` décrivent des transformations ou matérialisations techniques distinctes de la provenance épistémique des assertions.

## Sorties IA

Toute sortie IA est `proposal_only` jusqu’à acceptation explicite par le processus d’autorité approprié.
