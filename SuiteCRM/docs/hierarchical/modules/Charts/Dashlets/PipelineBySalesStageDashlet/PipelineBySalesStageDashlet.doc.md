# PipelineBySalesStageDashlet.php

**Chemin :** `modules/Charts/Dashlets/PipelineBySalesStageDashlet/PipelineBySalesStageDashlet.php`
**Type :** PHP - Dashlet graphique
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Dashlet affichant le pipeline commercial par étape de vente (horizontal bar chart RGraph). Filtre par plage de dates et étapes sélectionnées. Les montants sont convertis selon la devise de l'utilisateur courant.

## Type
view / dashlet

## Dépendances clés
- `include/Dashlets/DashletGenericChart.php` — classe parente
- `BeanFactory` (Currencies, Opportunities)
- `DBManagerFactory` — conversion dates SQL
- `$app_list_strings['sales_stage_dom']`

## Exports / Symboles principaux
- `PipelineBySalesStageDashlet` (classe) — étend `DashletGenericChart`
  - `display()` — rendu canvas RGraph HBar
  - `displayOptions()` — formulaire filtre étapes
  - `constructQuery()` — SQL groupé par sales_stage avec conversion devise
  - `getChartData($query)` — exécute et réordonne selon `sales_stage_dom`
  - `prepareChartData($data, ...)` — formate pour RGraph
  - `resizeLabel($label)` — tronque les libellés longs (>18 car)

## Interactions
- **Appelé par :** `modules/Home/index.php`
- **Appelle :** `BeanFactory` (Currencies), `DBManagerFactory`

## Notes
- Par défaut : date début = aujourd'hui, date fin = +6 mois.
- Commentaire "TODO" ligne 143 : `canvasId` avec `uniqid()`.
