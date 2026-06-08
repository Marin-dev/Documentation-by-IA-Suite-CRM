# Chart_my_pipeline_by_sales_stage.php

**Chemin :** `modules/Charts/code/Chart_my_pipeline_by_sales_stage.php`
**Type :** PHP - Helper (script legacy procédural)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Script legacy qui instancie `Chart_pipeline_by_sales_stage` pour l'utilisateur courant uniquement et déclenche l'affichage du graphique "My Pipeline by Sales Stage". Filtre les données sur `current_user->id`.

## Type
helper (legacy, procédural)

## Dépendances clés
- `include/charts/Charts.php`
- `modules/Charts/code/Chart_pipeline_by_sales_stage.php` — classe parente instanciée
- `$current_user`, `$timedate` (globaux)

## Exports / Symboles principaux
Aucune classe ni fonction exportée. Script procédural.

## Interactions
- **Appelé par :** `modules/Charts/code/predefined_charts.php`
- **Appelle :** `Chart_pipeline_by_sales_stage::draw()`

## Notes
- Variante personnelle de `Chart_pipeline_by_sales_stage` — filtre uniquement sur l'utilisateur courant.
- Script procédural pur (pas de classe propre).
