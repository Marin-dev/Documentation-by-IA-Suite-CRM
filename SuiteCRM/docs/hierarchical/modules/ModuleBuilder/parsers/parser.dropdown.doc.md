# parser.dropdown.php

**Chemin :** `modules/ModuleBuilder/parsers/parser.dropdown.php`
**Type :** PHP (model / parser)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Parser pour la sauvegarde et la synchronisation des dropdowns (listes déroulantes). Gère la persistance dans `custom/include/language/{lang}.lang.php` (Studio) ou dans les fichiers de langue du package MB. Synchronise les clés du dropdown sur toutes les langues disponibles.

## Type
model

## Dépendances clés
- `ModuleBuilderParser` (classe parente)
- `ModuleBuilder` (`MB/ModuleBuilder.php`) — pour les dropdowns MB
- Fonctions globales : `return_custom_app_list_strings_file_contents()`, `save_custom_app_list_strings_contents()`, `get_languages()`, `return_app_list_strings_language()`

## Exports/Symboles principaux
- `ParserDropDown` — classe (hérite de `ModuleBuilderParser`)
  - `saveDropDown($params)` — sauvegarde un dropdown (Studio ou MB), synchronise toutes les langues
  - `synchDropDown($name, $dropdown, $selected_lang, $saveLoc)` — synchronise les clés sur toutes les langues (Studio)
  - `synchMBDropDown($name, $dropdown, $selected_lang, $module)` — synchronise les clés en MB
  - `getNewCustomContents($name, $dropdown, $lang)` — génère le contenu PHP pour `$app_list_strings`
  - `getPatternMatch($name)` / `getPatternMatchGlobal($name)` — regex de remplacement

## Interactions
- **Appelé par :** `ModuleBuilderController::action_SaveDropDown()`
- **Appelle :** `ModuleBuilder`, fonctions globales de langue Sugar

## Notes
- Mode `use_push` (ligne 113) : pour `moduleList` et similaires, n'écrase pas les clés existantes mais les met à jour individuellement via regex.
- La synchronisation des clés entre langues assure que l'ajout/suppression d'une option dans une langue est répercuté dans toutes (avec la valeur de la langue sélectionnée pour les nouvelles clés). Ligne 154.
- Parsing JSON pour la réception des valeurs (format tableau de paires `[key, value]`). Ligne 72.
