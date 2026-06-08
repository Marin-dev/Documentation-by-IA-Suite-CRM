# Fichier AORReportsDashlet.php

**Chemin :** `modules/AOR_Reports/Dashlets/AORReportsDashlet/AORReportsDashlet.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Dashlet du module AOR_Reports. Permet d'afficher le résultat d'un rapport AOR dans le tableau de bord SuiteCRM. L'utilisateur sélectionne un rapport à afficher dans le dashlet.

## Type
autre (dashlet)

---

## Notes
Hérite de la classe Dashlet SuiteCRM. Affiche le rapport sélectionné via `AOR_Report::build_report_html()` ou `buildMultiGroupReport()`. Configuration : sélection du rapport à afficher.
