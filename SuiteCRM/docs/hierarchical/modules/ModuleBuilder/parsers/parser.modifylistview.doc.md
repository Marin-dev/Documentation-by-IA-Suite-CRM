# parser.modifylistview.php

**Chemin :** `modules/ModuleBuilder/parsers/parser.modifylistview.php`
**Type :** PHP (model / parser)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Parser de layout pour les vues en liste (ListView). Gère les colonnes par défaut, additionnelles et cachées. Charge depuis `modules/{Module}/metadata/listviewdefs.php` et sauvegarde dans `custom/modules/{Module}/metadata/listviewdefs.php`.

## Type
model

## Dépendances clés
- `ModuleBuilderParser` (classe parente)
- `TemplateHandler` (`include/TemplateHandler/`) — invalidation cache
- `$beanList`, `$beanFiles` (globals) — chargement du bean

## Exports/Symboles principaux
- `ParserModifyListView` — classe (hérite de `ModuleBuilderParser`)
  - `init($module_name, $submodule)` — chargement des listviewdefs (base + custom)
  - `getDefaultFields()` — colonnes affichées par défaut
  - `getAdditionalFields()` — colonnes disponibles mais non affichées
  - `getAvailableFields()` — champs du bean non inclus dans la listview
  - `handleSave()` — reconstruit depuis `$_REQUEST` et sauvegarde
  - `isValidField($key, $def)` — filtre les champs éligibles (exclut ID, deleted, _name)
  - `addRelateData($fieldname, $listfielddef)` — enrichit les champs relate avec module/id/link
  - `fixKeys(&$defs)` — normalise les clés (lowercase, nom = clé)

## Interactions
- **Appelé par :** vues de liste ModuleBuilder ; héritée par `ParserModifySubPanel`
- **Appelle :** `TemplateHandler::clearCache()`, `ModuleBuilderParser::_loadFromFile()`

## Notes
- `$reserved` contient les champs avec `studio => false/non-true` — ils sont préservés dans le layout mais non éditables. Ligne 163.
- Les colonnes `group_0` (défaut) et `group_1` (additionnel) sont lues depuis `$_POST` lors du save. Ligne 313.
- Les types `html`, `enum`, `text` dans les champs custom ont `sortable = false` automatiquement. Ligne 340.
