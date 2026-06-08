# Fichier AOR_Report.php

**Chemin :** `modules/AOR_Reports/AOR_Report.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Modèle principal du module AOR_Reports. Représente un rapport configurable permettant à l'utilisateur de sélectionner un module cible, des champs à afficher, des conditions de filtrage et des graphiques associés. Supporte l'export CSV, le rendu HTML paginé, et l'export PDF.

## Type
model

---

## Dépendances clés
- `Basic` (classe parente SuiteCRM)
- `modules/AOR_Fields/AOR_Field.php` — champs du rapport
- `modules/AOR_Conditions/AOR_Condition.php` — conditions de filtrage
- `modules/AOR_Charts/AOR_Chart.php` — graphiques associés
- `modules/AOW_WorkFlow/aow_utils.php` — utilitaires partagés (getRelatedModule, etc.)
- `modules/AOR_Reports/aor_utils.php` — fonctions utilitaires (getAorAllowedFieldFunctions, etc.)
- `SuiteCRM\CleanCSV` — échappement CSV sécurisé
- `SuiteCRM\PDF\PDFWrapper` — génération PDF (utilisé via controller)
- `include/SuiteGraphs/RGraphIncludes.php` — bibliothèque graphique RGraph
- `BeanFactory`, `ACLController` — framework SuiteCRM

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AOR_Report` | classe | Modèle principal rapport |
| `save()` | méthode | Sauvegarde le rapport + champs + conditions + graphiques |
| `build_report_query()` | méthode | Construit la requête SQL SELECT du rapport |
| `build_report_html()` | méthode | Génère le HTML du tableau de résultats avec pagination |
| `build_group_report()` | méthode | Génère un rapport groupé (avec panneaux accordéon) |
| `buildMultiGroupReport()` | méthode | Gère les groupements multi-niveaux (jusqu'à 10 niveaux) |
| `build_report_csv()` | méthode | Génère et envoie le fichier CSV |
| `build_report_chart()` | méthode | Délègue le rendu des graphiques à AOR_Chart |
| `build_report_query_select()` | méthode | Construit la partie SELECT de la requête |
| `build_report_query_where()` | méthode | Construit la clause WHERE (conditions + ACL) |
| `build_report_query_join()` | méthode | Construit les JOIN (relations, champs custom) |
| `getTotalHTML()` | méthode | Génère la ligne de totaux (SUM/COUNT/AVG) |
| `calculateTotal()` | méthode | Calcule SUM, COUNT ou AVG sur un tableau de valeurs |
| `ACLAccess()` | méthode | Vérifie l'ACL sur le rapport ET sur le module cible |
| `CHART_TYPE_PCHART` | constante | Rendu graphique via pChart |
| `CHART_TYPE_CHARTJS` | constante | Rendu graphique via Chart.js |
| `CHART_TYPE_RGRAPH` | constante | Rendu graphique via RGraph |

## Interactions
- **Appelé par :** `AOR_ReportsController` (controller.php), `AOR_Scheduled_Reports` (envoi email), dashlets
- **Appelle :** `AOR_Field`, `AOR_Condition`, `AOR_Chart`, `aor_utils.php`, `aow_utils.php`, `CleanCSV`
- **Table BD :** `aor_reports`, relations `aor_fields`, `aor_conditions`, `aor_charts`, `aor_scheduled_reports`

## Notes
- La méthode `save()` force `set_time_limit(3600)` — risque de dépassement mémoire sur gros rapports.
- Les modules `AOR_*` et `AOW_*` sont exclus de la liste de modules sélectionnables (ligne 151).
- Les valeurs `module_path` sont sérialisées en base64 — attention à la désérialisation : `['allowed_classes' => false]` est appliqué.
- `queryWhereRepair()` nettoie les parenthèses vides par regex (boucle sécurisée jusqu'à 100 itérations).
- Groupement multi-niveaux limité à 10 niveaux (ligne 325).
- Champ `user_parameters` utilisé pour les conditions paramétrables dynamiquement.
