# GridLayoutMetaDataParser.php

**Chemin :** `modules/ModuleBuilder/parsers/views/GridLayoutMetaDataParser.php`
**Type :** PHP (model / parser)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Parser pour les vues en grille (EditView, DetailView, QuickCreate). Gère les panneaux de champs organisés en lignes/colonnes, la synchronisation edit-detail, et la persistance via Bridge pattern (déployé ou non-déployé).

## Type
model

## Dépendances clés
- `AbstractMetaDataParser` (classe parente)
- `MetaDataParserInterface`
- `constants.php`
- `DeployedMetaDataImplementation` / `UndeployedMetaDataImplementation` (selon contexte)

## Exports/Symboles principaux
- `GridLayoutMetaDataParser` — classe
  - `$variableMap` — mapping MB_EDITVIEW/MB_DETAILVIEW/MB_QUICKCREATE -> noms de vue
  - `handleSave()` — sauvegarde (publie) le layout
  - `writeWorkingFile()` — sauvegarde en brouillon
  - `getAvailableFields()` — champs disponibles mais non placés
  - `getLayout()` / `getLayoutPanels()` — retourne la structure des panneaux
  - `removeField($fieldName)` — retire un champ de tous les panneaux
  - `getUseTabs()` / `setUseTabs()` — gestion des onglets

## Interactions
- **Créé par :** `ParserFactory::getParser()` pour MB_EDITVIEW, MB_DETAILVIEW, MB_QUICKCREATE
- **Appelle :** `DeployedMetaDataImplementation` ou `UndeployedMetaDataImplementation`

## Notes
- La synchronisation edit/detail (action_saveLayout avec `sync_detail_and_edit`) crée un second parser pour MB_DETAILVIEW avec les mêmes paramètres de tabs. Contrôleur ligne 719.
