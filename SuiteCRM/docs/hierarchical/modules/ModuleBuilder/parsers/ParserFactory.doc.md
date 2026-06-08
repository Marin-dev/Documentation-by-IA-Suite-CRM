# ParserFactory.php

**Chemin :** `modules/ModuleBuilder/parsers/ParserFactory.php`
**Type :** PHP (helper / factory)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Factory centrale pour instancier le bon parser de layout selon le type de vue. Supporte les overrides de parsers par module via convention de nommage de fichiers (`parser.{view}.php`).

## Type
helper (factory)

## Dépendances clés
- `constants.php` (`parsers/constants.php`)
- `StudioModuleFactory` (`Module/StudioModuleFactory.php`) — pour les overrides Studio
- Parsers de vues : `GridLayoutMetaDataParser`, `ListLayoutMetaDataParser`, `SearchViewMetaDataParser`, `SubpanelMetaDataParser`, `DashletMetaDataParser`, `PopupMetaDataParser`, `ParserLabel`

## Exports/Symboles principaux
- `ParserFactory` — classe (méthodes statiques)
  - `getParser($view, $moduleName, $packageName, $subpanelName)` — retourne le parser approprié
  - `checkForParserClass($view, $moduleName, $packageName, $nameOverride)` — cherche un parser custom dans `custom/modules/{Module}/parsers/` ou `modules/ModuleBuilder/parsers/`
  - `checkForStudioParserOverride($view, $moduleName, $packageName)` — vérifie les overrides déclarés dans `StudioModule::sources`

## Interactions
- **Appelé par :** `ModuleBuilderController` (toutes les actions save*), `StudioModule::removeFieldFromLayouts()`, `MBModule::removeFieldFromLayouts()`
- **Appelle :** tous les parsers de vues listés ci-dessus

## Notes
- Logique de sélection : si `$packageName` est vide ou 'studio' -> parsers Studio (deployed) ; sinon -> parsers MB (undeployed).
- `checkForParserClass()` cherche dans l'ordre : `custom/modules/{Module}/parsers/`, `modules/{Module}/parsers/`, `custom/modules/ModuleBuilder/parsers/`, `modules/ModuleBuilder/parsers/`. Ligne 132.
- Le type `MB_LISTVIEW` avec `$subpanelName` non null instancie `SubpanelMetaDataParser`. Ligne 94.
