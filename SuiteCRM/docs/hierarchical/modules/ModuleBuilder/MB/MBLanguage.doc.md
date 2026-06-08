# MBLanguage.php

**Chemin :** `modules/ModuleBuilder/MB/MBLanguage.php`
**Type :** PHP (model)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Gère les fichiers de langue (mod_strings et app_list_strings) pour un module ModuleBuilder non-deployé. Charge les strings depuis les templates SugarObjects, les fusionne avec les chaînes du module, génère les required labels, et sauvegarde les fichiers de langue.

## Type
model

## Dépendances clés
- Constantes `MB_TEMPLATES` et `MB_IMPLEMENTS` (définies dans `MBModule.php`)
- Fonctions globales : `return_module_language()`, `write_array_to_file()`, `override_value_to_string_recursive2()`, `sugarLangArrayMerge()`

## Exports/Symboles principaux
- `MBLanguage` — classe
  - `load()` — charge mod_strings et app_list_strings depuis templates + répertoire du module
  - `save($key_name, $duplicate, $rename)` — sauvegarde les fichiers langue + app_list_strings avec injection des labels requis (LBL_MODULE_NAME, LBL_LIST_FORM_TITLE, etc.)
  - `build($path)` — copie les fichiers langue vers le répertoire de build
  - `getModStrings($language)` — retourne les mod_strings fusionnées pour une langue
  - `getAppListStrings($language)` — retourne les app_list_strings fusionnées
  - `generateModStrings()` / `generateAppStrings()` — régénère depuis templates
  - `translate($label, $language)` — traduit un label depuis les strings chargées
  - `reload()` — réinitialise et recharge (appelé quand la config change)

## Interactions
- **Appelé par :** `MBModule` (à la construction et lors de `save()`)
- **Appelle :** fonctions globales Sugar lang

## Notes
- `save()` injecte automatiquement les labels requis (`LBL_MODULE_NAME`, `LNK_NEW_RECORD`, etc.) uniquement si absents ou si le label du module a changé. Ligne 178.
- `getGlobalAppListStringsForMB()` gère un cas spécial : lors de la création d'un champ enum en MB, copie le dropdown depuis `$app_list_strings` global si absent localement. Ligne 255.
- Sauvegarde en format `override_value_to_string_recursive2` (format Extension), pas en tableau PHP classique.
