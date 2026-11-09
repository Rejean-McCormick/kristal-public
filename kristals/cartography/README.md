# Kristal-Cartography

**Kristal-Cartography 1.0.0** est un corpus statique Kristal v6 centré sur la chaîne :

**territoire → référentiel → projection → couche → symbole → carte**

Les flèches indiquent une chaîne conceptuelle de référencement, transformation, structuration et représentation. Elles ne supposent pas qu’un logiciel ou une carte matérialise chaque étape dans un fichier distinct.

Le corpus distingue explicitement le système de référence de coordonnées (CRS/SCR), le datum, les opérations de coordonnées et la projection cartographique. Il couvre aussi les couches vectorielles et raster, les géométries, les métadonnées, les systèmes de tuiles, la symbolisation, les variables visuelles, l’échelle, la généralisation et la composition de carte.

Les normes ISO/TC 211, OGC et le registre EPSG servent d’ancrages de provenance. Le paquet n’est ni un service SIG temps réel, ni un registre cadastral légal, ni un moteur de transformation géodésique de précision.

État canonique : `knowledge-base/corpus/cartography.kristal-state.json`

Validation : `python knowledge-base/tools/validate.py`
