# chartdefs.php

**Chemin :** `modules/Charts/chartdefs.php`
**Type :** PHP - Configuration
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Définit le tableau de configuration `$chartDefs` des graphiques prédéfinis du module Charts. Chaque entrée spécifie le type, l'identifiant, le label, les critères de regroupement, les URLs de base et les paramètres URL pour les graphiques d'opportunités et de trackers.

## Type
config

## Dépendances clés
- `return_module_language()` — traductions du module Charts
- `custom/Charts/chartDefs.ext.php` — extension custom optionnelle

## Exports / Symboles principaux
- `$chartDefs` (tableau) — 5 graphiques définis :
  - `pipeline_by_sales_stage` — histogramme horizontal groupé (Opportunities)
  - `lead_source_by_outcome` — histogramme horizontal groupé (Opportunities)
  - `outcome_by_month` — histogramme empilé groupé (Opportunities)
  - `pipeline_by_lead_source` — camembert (Opportunities)
  - `my_modules_used_last_30_days` — histogramme horizontal (Trackers)

## Interactions
- **Appelé par :** `modules/Charts/PredefinedChart.php`, dashlets Charts
- **Appelle :** rien (données statiques)

## Notes
- Supporte l'extension via `custom/Charts/chartDefs.ext.php` (include_once à la fin du fichier).
