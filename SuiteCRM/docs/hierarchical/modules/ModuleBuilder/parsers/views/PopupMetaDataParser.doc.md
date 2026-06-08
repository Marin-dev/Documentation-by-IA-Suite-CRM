# PopupMetaDataParser.php

**Chemin :** `modules/ModuleBuilder/parsers/views/PopupMetaDataParser.php`
**Type :** PHP (model / parser)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Parser pour les vues popup (popuplist, popupsearch). Hérite de `ListLayoutMetaDataParser` et préserve les propriétés réservées du popup (moduleMain, varName, orderBy, whereClauses, etc.) lors de la sauvegarde.

## Type
model

## Dépendances clés
- `ListLayoutMetaDataParser` (classe parente)
- `SearchViewMetaDataParser`
- `constants.php`

## Exports/Symboles principaux
- `PopupMetaDataParser` — classe
  - `$columns` — `LBL_DEFAULT`, `LBL_AVAILABLE`, `LBL_HIDDEN`
  - `$reserveProperties` — propriétés du popup à préserver (moduleMain, varName, orderBy, whereClauses, etc.)

## Interactions
- **Créé par :** `ParserFactory::getParser()` pour MB_POPUPLIST et MB_POPUPSEARCH
- **Appelé par :** `ModuleBuilderController::action_popupSave()`

## Notes
`action_popupSave()` appelle `RepairAndClear::clearTpls()` après sauvegarde pour invalider les templates popup. Contrôleur ligne 779.
