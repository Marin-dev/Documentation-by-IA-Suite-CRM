# controller.php (AOR_Reports)

**Chemin :** `modules/AOR_Reports/controller.php`
**Type :** PHP - Controleur (Controller)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Controleur HTTP du module AOR_Reports. Gere les actions AJAX et les actions de vue (export CSV, telechargement PDF, changement de page, generation de graphiques). Sert de point d'entree pour les interactions dynamiques de l'interface de creation/visualisation de rapports.

## Role technique
Etend `SugarController`. Chaque methode `action_*` repond a une action HTTP specifique. Les actions AJAX retournent du HTML ou JSON et terminent avec `die`. Utilise `AOR_Report` (via `$this->bean`) pour la generation de contenu.

---

## Dependances / Imports
- `SugarController` (classe parente SugarCRM)
- `SuiteCRM\PDF\PDFWrapper` — generation PDF
- `SuiteCRM\PDF\Exceptions\PDFException`
- `modules/AOW_WorkFlow/aow_utils.php`
- `modules/AOR_Reports/aor_utils.php`
- `BeanFactory`, `SugarApplication`, `SugarThemeRegistry` (framework)

## Actions exposees
| Action | Role |
|---|---|
| `action_getModuleFields` | Retourne les champs disponibles d'un module (HTML select) |
| `action_getVarDefs` | Retourne les vardefs JSON d'un champ de module |
| `action_getModuleTreeData` | Retourne l'arbre de navigation des relations |
| `action_getModuleRelationships` | Retourne les relations d'un module |
| `action_changeReportPage` | Pagination AJAX du rapport |
| `action_getParametersForReport` | Retourne les conditions parametrables JSON |
| `action_getChartsForReport` | Retourne la liste des graphiques JSON |
| `action_addToProspectList` | Ajoute les resultats du rapport a une liste de prospects |
| `action_chartReport` | Genere un graphique Chart.js |
| `action_export` | Exporte le rapport en CSV |
| `action_downloadPDF` | Telecharge le rapport en PDF (via mPDF) |
| `action_getModuleFunctionField` | Retourne le champ de fonction (COUNT, SUM, etc.) |
| `action_getModuleOperatorField` | Retourne le champ d'operateur de condition |
| `action_getFieldTypeOptions` | Retourne les types de valeurs pour une condition |
| `action_getActionFieldTypeOptions` | Retourne les types de valeurs pour une action workflow |
| `action_getModuleFieldType` | Retourne le widget d'input pour un type de valeur |
| `action_getModuleField` | Retourne le widget de saisie d'un champ |
| `action_getRelFieldTypeSet` | Retourne les options de champ pour relations |
| `action_getRelActionFieldTypeOptions` | Retourne les options d'action sur champ de relation |

## Relations cles
- **Appele par :** Framework SugarCRM via routing HTTP
- **Appelle :** `AOR_Report->build_report_csv()`, `build_group_report()`, `build_report_chart()`, `PDFWrapper`
- **Position dans le flux :** Point d'entree HTTP → delegue a `AOR_Report` pour la logique metier

---

## Points d'attention
- `action_downloadPDF` utilise `PDFWrapper::getPDFEngine()` avec mPDF ; capture `PDFException`.
- `action_addToProspectList` necessite une relation entre le module cible et `ProspectLists`.
- Plusieurs actions retournent du HTML inline via `echo` + `die` (pattern AJAX SugarCRM).
- Le CSS PDF est charge depuis `modules/AOR_Reports/pdf/pdf.css` avec support du fichier custom.
