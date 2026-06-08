# OutcomeByMonthDashlet.php

**Chemin :** `modules/Charts/Dashlets/OutcomeByMonthDashlet/OutcomeByMonthDashlet.php`
**Type :** PHP - Dashlet graphique
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Dashlet affichant l'évolution des résultats commerciaux par mois (stacked bar chart RGraph). Filtre par plage de dates et par utilisateurs assignés. Module seed : Opportunities.

## Type
view / dashlet

## Dépendances clés
- `include/Dashlets/DashletGenericChart.php` — classe parente
- `DBManagerFactory` — conversion dates SQL
- `BeanFactory` (Currencies, Opportunities)

## Exports / Symboles principaux
- `OutcomeByMonthDashlet` (classe) — étend `DashletGenericChart`
  - `display()` — rendu canvas RGraph
  - `displayOptions()` — formulaire filtre
  - `constructQuery()` — SQL groupé par sales_stage et mois

## Interactions
- **Appelé par :** `modules/Home/index.php`

## Notes
- Par défaut : date début = aujourd'hui, date fin = +6 mois.
