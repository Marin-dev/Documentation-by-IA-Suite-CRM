# ChartsDashlet.php

**Chemin :** `modules/Home/Dashlets/ChartsDashlet/ChartsDashlet.php`
**Type :** PHP - Dashlet (composant tableau de bord)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Dashlet affichant le graphique d'un rapport sauvegardé (SavedReport). Récupère le rapport par ID, exécute ses requêtes graphiques et affiche le rendu chart. Configurable via icône d'édition pointant vers le rapport source.

## Type
view / dashlet

## Dépendances clés
- `include/Dashlets/Dashlet.php` — classe parente `Dashlet`
- `modules/Reports/Report.php` — classes `SavedReport`, `Report`
- `modules/Reports/templates/templates_chart.php` — fonction `template_chart`
- `include/SugarCharts/SugarChartFactory.php` — `SugarChartFactory::getInstance()`
- `Sugar_Smarty`

## Exports / Symboles principaux
- `ChartsDashlet` (classe) — étend `Dashlet`
  - `display()` — rendu HTML du graphique
  - `displayScript()` — rendu JS pour le graphique
  - `setConfigureIcon()` — lien vers le rapport source
  - `setRefreshIcon()` — bouton refresh AJAX

## Interactions
- **Appelé par :** `modules/Home/index.php` (instanciation dynamique)
- **Appelle :** `SavedReport`, `Report`, `SugarChartFactory`

## Notes
- `display()` appelle `parent::display()` deux fois (lignes 109 et 117) — doublon apparent, bug potentiel.
- Le report_id est passé au constructeur (pas en `$def['options']` comme d'autres dashlets).
