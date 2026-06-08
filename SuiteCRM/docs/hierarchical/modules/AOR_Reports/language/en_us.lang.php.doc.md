# Fichier en_us.lang.php — AOR_Reports

**Chemin :** `modules/AOR_Reports/language/en_us.lang.php`
**Type :** PHP — configuration
**Dernière mise à jour doc :** 2026-05-31

## Rôle fonctionnel
Fichier de traduction anglaise du module AOR_Reports. Contient `$mod_strings` (labels des champs, boutons, messages du module) et `$app_list_strings` (listes de valeurs : opérateurs, fonctions, types de conditions, etc.).

## Type
config

## Notes
Les `$app_list_strings` de ce fichier définissent notamment : `aor_operator_list`, `aor_function_list`, `aor_sort_operator`, `aor_condition_type_list`, `aor_date_operator`, `date_time_period_list`, `aor_format_options`, `aor_total_options`. Ces listes sont utilisées par `getAorAllowedFieldFunctions()` et `getAorAllowedSortDirections()` dans `aor_utils.php`.
