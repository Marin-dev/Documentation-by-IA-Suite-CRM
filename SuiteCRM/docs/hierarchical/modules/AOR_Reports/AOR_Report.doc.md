# AOR_Report.php

**Chemin :** `modules/AOR_Reports/AOR_Report.php`
**Type :** PHP - Modele (Model)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele principal du moteur de rapports AOR (Advanced OpenReports). Permet de definir, executer et afficher des rapports configurables sur n'importe quel module SuiteCRM. Gere la generation HTML, CSV et PDF des resultats, ainsi que les graphiques associes.

## Role technique
Etend la classe `Basic` de SugarCRM. Contient toute la logique de construction de requetes SQL dynamiques (SELECT, JOIN, WHERE, GROUP BY, ORDER BY) en fonction des champs, conditions et graphiques lies. Gere la pagination des resultats et le calcul de totaux (SUM, AVG, COUNT).

---

## Dependances / Imports
- `Basic` (classe parente SugarCRM)
- `SuiteCRM\CleanCSV` — echappement CSV securise
- `modules/AOW_WorkFlow/aow_utils.php` — utilitaires workflow partages
- `modules/AOR_Reports/aor_utils.php` — utilitaires rapports (fonctions SQL, periodes)
- `modules/AOR_Fields/AOR_Field.php` — champs du rapport
- `modules/AOR_Conditions/AOR_Condition.php` — conditions du rapport
- `modules/AOR_Charts/AOR_Chart.php` — graphiques du rapport
- `SuiteCRM\PDF\PDFWrapper` (utilise dans controller)
- `BeanFactory`, `ACLController` (framework SugarCRM)

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `AOR_Report` | Classe | Modele principal du rapport |
| `save()` | Methode | Sauvegarde rapport + lignes champs/conditions/graphiques |
| `build_report_query()` | Methode | Construit la requete SQL complete |
| `build_report_html()` | Methode | Genere le HTML de la table de resultats avec pagination |
| `build_report_csv()` | Methode | Genere et envoie le fichier CSV |
| `build_report_chart()` | Methode | Genere le HTML des graphiques |
| `build_group_report()` | Methode | Genere le rapport avec groupement |
| `buildMultiGroupReport()` | Methode | Rapport multi-niveaux de groupement |
| `getTotalHTML()` | Methode | Genere la ligne de totaux (SUM/AVG/COUNT) |
| `calculateTotal()` | Methode | Calcule SUM, COUNT ou AVG |
| `CHART_TYPE_PCHART` | Constante | Type graphique pChart |
| `CHART_TYPE_CHARTJS` | Constante | Type graphique Chart.js |
| `CHART_TYPE_RGRAPH` | Constante | Type graphique RGraph |

**Consommateurs identifies :**
- `modules/AOR_Reports/controller.php` — utilise toutes les methodes de generation
- `modules/AOR_Scheduled_Reports/AOR_Scheduled_Reports.php` — appelle les methodes de rapport pour l'envoi planifie

## Relations cles
- **Appele par :** `AOR_ReportsController`, scheduler planifie, dashlet `AORReportsDashlet`
- **Appelle :** `AOR_Field`, `AOR_Condition`, `AOR_Chart`, `ACLController`, `BeanFactory`
- **Table DB :** `aor_reports`
- **Relations 1-N :** vers `aor_fields`, `aor_conditions`, `aor_charts`, `aor_scheduled_reports`

---

## Points d'attention
- Le champ `module_path` dans `aor_fields`/`aor_conditions` est stocke en `base64(serialize(array))` — deserialisation avec `['allowed_classes' => false]` (securite).
- La methode `build_report_query_join` distingue les jointures `custom` (tables `_cstm`) des jointures `relationship`.
- Protection ACL : verifie l'acces au module cible via `ACLController::checkAccess()` avant toute requete.
- La methode `queryWhereRepair` nettoie les parentheses vides generees par des conditions supprimees (boucle avec limite a 100 iterations).
- `$doNotRunInSaveLogic` n'est pas present ici mais dans `AOW_WorkFlow` — pas de risque de recursion directe.
- La variable `user_parameters` (conditions parametrables) est injectee depuis le controller avant appel.
