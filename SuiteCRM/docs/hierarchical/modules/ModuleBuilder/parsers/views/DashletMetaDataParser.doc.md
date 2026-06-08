# DashletMetaDataParser.php

**Chemin :** `modules/ModuleBuilder/parsers/views/DashletMetaDataParser.php`
**Type :** PHP (model / parser)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Parser pour les vues Dashlet (dashlet list et dashlet search). Hérite de `ListLayoutMetaDataParser` avec les trois colonnes (default, available, hidden).

## Type
model

## Dépendances clés
- `ListLayoutMetaDataParser` (classe parente)
- `SearchViewMetaDataParser`
- `constants.php`

## Exports/Symboles principaux
- `DashletMetaDataParser` — classe
  - `$columns` — `LBL_DEFAULT`, `LBL_AVAILABLE`, `LBL_HIDDEN`
  - `$_view` — type de vue (MB_DASHLET ou MB_DASHLETSEARCH)
  - `$search` — booléen, true si vue de recherche dashlet

## Interactions
- **Créé par :** `ParserFactory::getParser()` pour MB_DASHLET et MB_DASHLETSEARCH
- **Appelé par :** `ModuleBuilderController::action_dashletSave()`
