# Chart_lead_source_by_outcome.php

**Chemin :** `modules/Charts/code/Chart_lead_source_by_outcome.php`
**Type :** PHP - Helper (générateur de graphique legacy)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe legacy de génération du graphique "Lead Source by Outcome" (opportunités par source de lead et résultat). Génère un fichier XML de données pour le rendu via l'ancien moteur de graphiques SugarCRM (`hBarF`). Contient également une méthode de formulaire HTML pour les filtres.

## Type
helper (legacy)

## Dépendances clés
- `include/charts/Charts.php` — fonctions `create_chart()`, `save_xml_file()`, `generate_graphcolor()`
- `BeanFactory::newBean('Opportunities')` — accès aux données
- `BeanFactory::newBean('Currencies')` — conversion de devise
- `$current_user->getPreference()` / `setPreference()` — filtres persistants
- `$app_list_strings['lead_source_dom']`, `$app_list_strings['sales_stage_dom']`

## Exports / Symboles principaux
- `Chart_lead_source_by_outcome` (classe)
  - `draw($extra_tools)` — affiche le formulaire de filtre et le graphique
  - `gen_xml($datay, $user_id, $cache_file_name, $refresh, $current_module_strings)` — génère le XML et crée le graphique via `create_chart('hBarF', ...)`
  - `constructQuery()` — construit la requête SQL pour les dashlets
  - `constructGroupBy()` — retourne `['lead_source', 'sales_stage']`

## Interactions
- **Appelé par :** `modules/Charts/code/predefined_charts.php`, dashlets Charts legacy
- **Appelle :** `Charts.php`, `BeanFactory`, `$current_user`

## Notes
- Code legacy : utilise des fichiers XML de cache dans `sugar_cached('xml/')`.
- Contient des appels `$GLOBALS['log']->fatal()` pour le débogage (ligne 79, 84) — dette technique.
- Le cache XML est invalidé uniquement si `$refresh == true` ou si le fichier n'existe pas.
