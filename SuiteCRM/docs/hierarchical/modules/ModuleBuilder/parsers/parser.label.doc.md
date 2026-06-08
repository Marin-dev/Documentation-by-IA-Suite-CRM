# parser.label.php

**Chemin :** `modules/ModuleBuilder/parsers/parser.label.php`
**Type :** PHP (model / parser)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Parser pour la sauvegarde et la suppression des labels de modules (mod_strings). Gère les labels des modules déployés (Studio, format Extension) et non-déployés (MB). Gère aussi les labels de relations (écriture dans le répertoire `custom/Extension/modules/relationships/language`).

## Type
model

## Dépendances clés
- `ModuleBuilderParser` (référencée dans require_once)
- `LoggerManager`
- Fonctions : `write_array_to_file()`, `write_override_label_to_file()`, `sugar_cache_clear()`, `LanguageManager::clearLanguageCache()`, `SugarCache::cleanOpcodes()`

## Exports/Symboles principaux
- `ParserLabel` — classe
  - `handleSave($params, $language)` — sauvegarde les labels depuis les params POST (`label_{KEY}` => valeur)
  - `handleSaveRelationshipLabels($metadata, $language)` — sauvegarde les labels d'une relation
  - `addLabels($language, $labels, $moduleName, $basepath, $forRelationshipLabel)` (statique) — écrit les labels dans le fichier de langue approprié
  - `removeLabel($language, $label, $labelvalue, $moduleName, $basepath, $forRelationshipLabel)` (statique) — supprime un label du fichier de langue
  - `addLabelsToAllLanguages($labels)` — applique les labels à toutes les langues disponibles

## Interactions
- **Appelé par :** `ModuleBuilderController` (`action_saveLabels`, `action_SaveLabel`, `action_saveProperty`, `action_SaveRelationshipLabel`, `DeleteLabel`), `ParserDropDown`
- **Appelle :** fonctions globales Sugar lang

## Notes
- Pour les modules déployés, les labels sont écrits dans `custom/Extension/modules/{Module}/Ext/Language/_override_{lang}.lang.php`. Ligne 215.
- Pour les labels de relations (`$forRelationshipLabel`), écriture supplémentaire dans `custom/Extension/modules/{Module}/Ext/Language/{lang}.custom{relName}.php` ET dans `custom/Extension/modules/relationships/language/{lhsModule}.php` (fix bug #51). Lignes 280-368.
- `SugarCleaner::cleanHtml()` appliqué aux valeurs de labels (XSS protection). Ligne 107.
