# OpportunitiesByLeadSourceByOutcomeDashlet.php

**Chemin :** `modules/Charts/Dashlets/OpportunitiesByLeadSourceByOutcomeDashlet/OpportunitiesByLeadSourceByOutcomeDashlet.php`
**Type :** PHP - Dashlet (graphique)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Dashlet affichant un graphique de barres horizontales empilées représentant les opportunités regroupées par source de lead (lead_source) et résultat de vente (sales_stage). Permet à l'utilisateur de filtrer par sources de lead et utilisateurs assignés.

## Type
dashlet

## Dépendances clés
- `include/Dashlets/DashletGenericChart.php` — classe parente
- `BeanFactory::newBean('Currencies')` — conversion de devise
- `RGraph.HBar` (JavaScript) — rendu du graphique canvas
- Table `opportunities` — source de données SQL
- `$app_list_strings['lead_source_dom']` — liste des sources de lead

## Exports / Symboles principaux
- `OpportunitiesByLeadSourceByOutcomeDashlet` (classe, étend `DashletGenericChart`)
  - `displayOptions()` — options de filtrage (lead sources, utilisateurs)
  - `display()` — génère le HTML + JS RGraph (canvas `hBarF`)
  - `constructQuery()` — requête SQL `GROUP BY sales_stage,lead_source`
  - `prepareChartData()` — transforme les données SQL en structure JSON pour RGraph

## Interactions
- **Appelé par :** framework Dashlets (tableau de bord Home)
- **Appelle :** `DashletGenericChart::getChartData()`, `sortData()`, `$this->processAutoRefresh()`

## Notes
- L'ancien code basé sur `SugarChartFactory` est commenté (ligne 94-121) — la version actuelle utilise directement RGraph.
- Couleurs codées en dur dans un tableau de 12 couleurs hex (ligne 165).
- Requête SQL directe sans ORM (ligne 256-270) — filtre sur `deleted=0`.
