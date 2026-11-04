@echo off
setlocal EnableExtensions DisableDelayedExpansion
REM BLOCKED: kristal-public est un dépôt de publication soumis aux contrôles C1/C2/C3.
REM Le script GitSink générique n'a aucune autorité de qualification ou publication.
REM Utiliser le processus de revue et de validation signé dans Kristal-Manager.
>&2 echo BLOCKED: GitSink generique desactive sur kristal-public.
>&2 echo Verification C1/C2/C3 et revue du contenu exact requises via Kristal-Manager.
exit /b 41
