# OpportunitiesByLeadSourceDashlet.php

**Chemin :** `modules/Charts/Dashlets/OpportunitiesByLeadSourceDashlet/OpportunitiesByLeadSourceDashlet.php`
**Type :** PHP - Dashlet graphique
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Dashlet affichant le pipeline commercial par source de prospect (pie/bar chart RGraph). Filtre par sources de prospects sélectionnées et par utilisateurs assignés. Module seed : Opportunities.

## Type
view / dashlet

## Dépendances clés
- `include/Dashlets/DashletGenericChart.php` — classe parente
- `$app_list_strings['lead_source_dom']`

## Exports / Symboles principaux
- `OpportunitiesByLeadSourceDashlet` (classe) — étend `DashletGenericChart`
  - `display()` — rendu graphique
  - `displayOptions()` — formulaire filtre sources + utilisateurs
  - `constructQuery()` — SQL groupé par lead_source

## Interactions
- **Appelé par :** `modules/Home/index.php`
