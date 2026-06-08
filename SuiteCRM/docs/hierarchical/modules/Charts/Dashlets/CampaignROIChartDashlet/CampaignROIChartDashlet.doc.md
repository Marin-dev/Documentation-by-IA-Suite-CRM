# CampaignROIChartDashlet.php

**Chemin :** `modules/Charts/Dashlets/CampaignROIChartDashlet/CampaignROIChartDashlet.php`
**Type :** PHP - Dashlet graphique
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Dashlet affichant un graphique ROI (Retour sur investissement) pour une campagne sélectionnée. Calcule et présente les données : valeur totale des opportunités en prospection, revenus générés (Closed Won), investissement réel, budget et revenu attendu. Rendu via RGraph (canvas HTML5).

## Type
view / dashlet

## Dépendances clés
- `include/Dashlets/DashletGenericChart.php` — classe parente `DashletGenericChart`
- `BeanFactory` (Campaigns, Currencies)
- `DBManagerFactory` — requêtes SQL
- `$app_list_strings['roi_type_dom']`

## Exports / Symboles principaux
- `CampaignROIChartDashlet` (classe) — étend `DashletGenericChart`
  - `display()` — rendu canvas RGraph bar chart ROI
  - `displayOptions()` — liste de sélection des campagnes disponibles
  - `constructQuery($datay, $targets, $campaign_id, ...)` — exécute les requêtes SQL et retourne les données brutes
  - `prepareChartData($data, $currency_symbol, $thousands_symbol)` — formate pour RGraph

## Interactions
- **Appelé par :** `modules/Home/index.php`
- **Appelle :** `BeanFactory` (Campaigns, Currencies, Opportunities), `DBManagerFactory`

## Notes
- La méthode `constructQuery` retourne un tableau PHP (pas une string SQL) — contrairement aux autres dashlets.
- Présence de code commenté avec d'anciennes approches (lignes 209-225, 317-323) — dette technique.
