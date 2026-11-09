# Kristal-Time v0.1.0

Corpus statique et versionné de référence sur **instant / intervalle / durée / ordre / récurrence / calendrier / référentiel temporel**.

## Noyau conceptuel

`événement/chose → entité temporelle → position + durée → ordre → représentation (calendrier/horloge/zone) → référentiel temporel`

## Distinctions structurantes

- instant ≠ timestamp ;
- intervalle ≠ durée ;
- durée physique fixe ≠ durée calendaire ;
- antériorité ≠ causalité ;
- offset UTC ≠ zone horaire ;
- heure locale ≠ instant ;
- UTC ≠ TAI ≠ UT1 ;
- précision de représentation ≠ exactitude ;
- règle de récurrence ≠ occurrences matérialisées ;
- date approximative ≠ date exacte.

## Seed

OWL-Time/relations d’intervalle, SI seconde, échelles TAI/UTC/UTCr/UTC(k)/UT1/TT, calendriers, IANA tzdb 2026e, timestamps ISO/RFC, récurrences iCalendar, secondes intercalaires, granularité et incertitude temporelle.

Les exemples sont explicitement **illustratifs** sauf l’état daté `UTC−TAI = −37 s` issu du Bulletin C 72 de l’IERS.

## Validation

Exécuter : `python knowledge-base/tools/validate.py`
