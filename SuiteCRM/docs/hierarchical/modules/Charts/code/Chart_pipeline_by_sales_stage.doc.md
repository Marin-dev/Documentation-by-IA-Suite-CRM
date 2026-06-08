# Chart_pipeline_by_sales_stage.php

**Chemin :** `modules/Charts/code/Chart_pipeline_by_sales_stage.php`
**Type :** PHP - Helper (générateur de graphique legacy)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe legacy de génération du graphique "Pipeline by Sales Stage" (pipeline d'opportunités par étape de vente, histogramme horizontal groupé). Génère un fichier XML de données pour le rendu via l'ancien moteur de graphiques SugarCRM. Sert aussi de classe parente pour `Chart_my_pipeline_by_sales_stage`.

## Type
helper (legacy)

## Dépendances clés
- `include/charts/Charts.php` — fonctions `create_chart()`, `save_xml_file()`
- Table `opportunities` — source SQL
- `$app_list_strings['sales_stage_dom']`

## Exports / Symboles principaux
- `Chart_pipeline_by_sales_stage` (classe)
  - `draw($extra_tools)` — affiche le formulaire de filtre (date, etapes, utilisateurs) et le graphique
  - `$order`, `$modules`

## Interactions
- **Appelé par :** `Chart_my_pipeline_by_sales_stage.php` (héritage), `predefined_charts.php`
- **Appelle :** `Charts.php`

## Notes
- Code legacy utilisant fichiers XML de cache dans `sugar_cached('xml/')`.
- Étendu par `Chart_my_pipeline_by_sales_stage` pour filtrer sur l'utilisateur courant uniquement.
