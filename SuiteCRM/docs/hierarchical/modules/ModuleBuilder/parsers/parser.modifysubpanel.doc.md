# parser.modifysubpanel.php

**Chemin :** `modules/ModuleBuilder/parsers/parser.modifysubpanel.php`
**Type :** PHP (model / parser)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Parser pour la modification des subpanels dans Studio. Hérite de `ParserModifyListView` et adapte la logique pour charger les définitions depuis `SubPanelDefinitions` et sauvegarder via le mécanisme d'override de `SubPanel`.

## Type
model

## Dépendances clés
- `ParserModifyListView` (`parsers/parser.modifylistview.php`) — classe parente
- `SubPanelDefinitions` (`include/SubPanel/SubPanelDefinitions.php`)
- `SubPanel` (`include/SubPanel/SubPanel.php`)

## Exports/Symboles principaux
- `ParserModifySubPanel` — classe (hérite de `ParserModifyListView`)
  - `init($module_name, $subPanelName)` — charge les définitions du subpanel via `SubPanelDefinitions`
  - `getDefaultFields()` — champs visibles du subpanel (exclut `usage=query_only`)
  - `getAvailableFields()` — champs du module parent non inclus dans le subpanel
  - `getField($fieldName)` — cherche dans listViewDefs, originalListViewDefs, puis field_defs du template
  - `handleSave()` — reconstruit les champs depuis `$_REQUEST['group_0']` et sauvegarde via `SubPanel::saveSubPanelDefOverride()`

## Interactions
- **Appelé par :** vues de subpanel ModuleBuilder
- **Appelle :** `SubPanelDefinitions`, `SubPanel::saveSubPanelDefOverride()`

## Notes
- `$columns` réduit à seulement `LBL_DEFAULT` et `LBL_HIDDEN` (pas de colonne "disponible" comme dans listview). Ligne 64.
- `handleSave()` utilise `SubPanel::saveSubPanelDefOverride()` — mécanisme d'override spécifique aux subpanels, différent de la sauvegarde classique de listview. Ligne 230.
