# Fichier aor_utils.php

**Chemin :** `modules/AOR_Reports/aor_utils.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel
Bibliothèque de fonctions utilitaires partagées pour le module AOR_Reports. Fournit des helpers pour la validation des opérateurs SQL, la résolution des dates relatives (périodes, trimestres), la conversion de dates entre formats utilisateur, et la récupération des paramètres de condition depuis la requête HTTP.

## Type
helper

---

## Dépendances clés
- `BeanFactory` — récupération des beans
- `getRelatedModule()` — résolution des relations entre modules
- `getModuleField()`, `getDisplayForField()` — affichage des champs
- `$app_list_strings`, `$sugar_config['aor']['quarters_begin']` — configuration trimestres
- `encodeMultienumValue()`, `unencodeMultienum()` — gestion multi-enum
- `fixUpFormatting()` — normalisation des valeurs de formulaire

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `getAorAllowedFieldFunctions()` | fonction | Retourne la liste des fonctions SQL autorisées (COUNT, SUM, etc.) depuis les app_list_strings |
| `getAorAllowedSortDirections()` | fonction | Retourne les directions de tri autorisées (ASC/DESC) |
| `getDisplayForField()` | fonction | Résout le chemin de module + champ en label lisible (breadcrumb) |
| `requestToUserParameters()` | fonction | Convertit les paramètres HTTP `parameter_*` en tableau structuré pour les conditions paramétrables |
| `getConditionsAsParameters()` | fonction | Retourne les conditions "parameter=1" d'un rapport formatées pour l'affichage formulaire |
| `getPeriodDate()` | fonction | Calcule la date de début d'une période relative (today, this_week, last_quarter, etc.) |
| `getPeriodEndDate()` | fonction | Calcule la date de fin d'une période relative |
| `calculateQuarters()` | fonction | Calcule les bornes des 4 trimestres selon un offset mensuel configurable |
| `convertToDateTime()` | fonction | Convertit une chaîne de date (format utilisateur) en DateTime UTC |

## Interactions
- **Appelé par :** `AOR_Report::build_report_query_where()`, `AOR_ReportsController`, `AOR_Condition::save_lines()`, `AOR_Field::save_lines()`
- **Appelle :** `BeanFactory`, `getRelatedModule()`, `getModuleField()`

## Notes
- `calculateQuarters()` supporte un décalage mensuel via `$sugar_config['aor']['quarters_begin']` permettant des années fiscales décalées.
- `convertToDateTime()` gère de nombreux formats de date utilisateur (Y-m-d, d/m/Y, m.d.Y, etc.) — risque de confusion si le format n'est pas reconnu.
- `getAorAllowedFieldFunctions()` et `getAorAllowedSortDirections()` utilisent `return_app_list_strings_language('en_us')` (langue forcée en_us) — les traductions ne sont pas prises en compte pour la validation.
