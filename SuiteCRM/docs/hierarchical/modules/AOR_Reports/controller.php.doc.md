# Fichier controller.php

**Chemin :** `modules/AOR_Reports/controller.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Contrôleur AJAX et d'actions du module AOR_Reports. Gère les requêtes dynamiques de l'interface de configuration des rapports (champs disponibles, opérateurs, types de valeurs) ainsi que les actions d'export (CSV, PDF) et de navigation dans les résultats paginés.

## Type
controller

---

## Dépendances clés
- `SugarController` (classe parente)
- `modules/AOW_WorkFlow/aow_utils.php` — utilitaires partagés
- `modules/AOR_Reports/aor_utils.php` — helpers rapports
- `SuiteCRM\PDF\PDFWrapper` — moteur PDF
- `SuiteCRM\PDF\Exceptions\PDFException`
- `BeanFactory`, `ACLController`
- `include/export_utils.php` — utilitaires export

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOR_ReportsController` | classe | Contrôleur du module AOR_Reports |
| `action_getModuleFields()` | méthode | AJAX : retourne le HTML des champs d'un module |
| `action_getVarDefs()` | méthode | AJAX : retourne les vardefs JSON d'un champ |
| `action_getModuleTreeData()` | méthode | AJAX : retourne l'arbre de modules/relations |
| `action_getModuleRelationships()` | méthode | AJAX : liste les relations d'un module |
| `action_changeReportPage()` | méthode | AJAX : pagination d'un rapport groupé |
| `action_getParametersForReport()` | méthode | AJAX : retourne les conditions paramétrables (JSON) |
| `action_getChartsForReport()` | méthode | AJAX : liste les graphiques d'un rapport (JSON) |
| `action_addToProspectList()` | méthode | Ajoute les résultats du rapport à une liste de prospects |
| `action_chartReport()` | méthode | Rendu graphique ChartJS |
| `action_export()` | méthode | Export CSV (vérifie ACL Export) |
| `action_downloadPDF()` | méthode | Génère et télécharge le PDF du rapport avec graphiques |
| `action_getModuleFunctionField()` | méthode | AJAX : sélecteur de fonction SQL (COUNT, SUM...) |
| `action_getModuleOperatorField()` | méthode | AJAX : sélecteur d'opérateur de condition selon le type de champ |
| `action_getFieldTypeOptions()` | méthode | AJAX : options de type de valeur (Value, Field, Date, Period...) |
| `action_getModuleFieldType()` | méthode | AJAX : widget de saisie selon le type de valeur sélectionné |

## Interactions
- **Appelé par :** Vue EditView AOR_Reports (appels AJAX JavaScript)
- **Appelle :** `AOR_Report::build_group_report()`, `AOR_Report::build_report_csv()`, `PDFWrapper`, `aor_utils.php`
- **Position dans le flux :** Point d'entrée HTTP pour toutes les interactions dynamiques de l'interface de configuration de rapport

## Notes
- `action_downloadPDF()` utilise `PDFWrapper::getPDFEngine()` et gère les exceptions `PDFException`.
- Le PDF inclut les graphiques base64 passés dans `$_POST["graphsForPDF"]`.
- Plusieurs actions retournent du HTML brut via `echo` + `die` (pattern AJAX classique SugarCRM).
- `action_getActionFieldTypeOptions()` gère les types spéciaux Round_Robin, Least_Busy, Random pour les champs utilisateur (partagé avec le module AOW).
