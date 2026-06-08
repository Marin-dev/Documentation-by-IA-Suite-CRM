# Chart_pipeline_by_lead_source.php

**Chemin :** `modules/Charts/code/Chart_pipeline_by_lead_source.php`
**Type :** PHP - Helper (générateur de graphique legacy)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe legacy de génération du graphique "Pipeline by Lead Source" (pipeline d'opportunités par source de lead, camembert). Génère un fichier XML de données pour le rendu via l'ancien moteur de graphiques SugarCRM.

## Type
helper (legacy)

## Dépendances clés
- `include/charts/Charts.php` — fonctions de génération de graphique
- Table `opportunities` — source SQL
- `$app_list_strings['lead_source_dom']`

## Exports / Symboles principaux
- `Chart_pipeline_by_lead_source` (classe)
  - `draw($extra_tools)` — affiche le formulaire + graphique
  - `$order`, `$modules`

## Interactions
- **Appelé par :** `modules/Charts/code/predefined_charts.php`
- **Appelle :** `Charts.php`

## Notes
- Code legacy utilisant fichiers XML de cache.
