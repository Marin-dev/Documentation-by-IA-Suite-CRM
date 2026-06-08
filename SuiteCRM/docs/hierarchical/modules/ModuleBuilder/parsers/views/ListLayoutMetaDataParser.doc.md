# ListLayoutMetaDataParser.php

**Chemin :** `modules/ModuleBuilder/parsers/views/ListLayoutMetaDataParser.php`
**Type :** PHP (model / parser)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Parser pour les vues en liste (ListView). Gère les colonnes défaut/disponibles/cachées via le pattern Bridge (déployé ou non-déployé). Classe de base pour `SearchViewMetaDataParser`, `DashletMetaDataParser`, `SubpanelMetaDataParser`, `PopupMetaDataParser`.

## Type
model

## Dépendances clés
- `AbstractMetaDataParser` (classe parente)
- `MetaDataParserInterface`
- `DeployedMetaDataImplementation` / `UndeployedMetaDataImplementation`

## Exports/Symboles principaux
- `ListLayoutMetaDataParser` — classe
  - `$columns` — tableau `['LBL_DEFAULT' => 'getDefaultFields', 'LBL_AVAILABLE' => 'getAdditionalFields', 'LBL_HIDDEN' => 'getAvailableFields']`
  - `handleSave()` — sauvegarde via implementation
  - `getDefaultFields()` / `getAdditionalFields()` / `getAvailableFields()` — partitionnement des champs
  - `removeField($fieldName)` — retire un champ du layout

## Interactions
- **Créé par :** `ParserFactory::getParser()` pour MB_LISTVIEW (sans subpanel)
- **Héritée par :** `SearchViewMetaDataParser`, `DashletMetaDataParser`, `SubpanelMetaDataParser`, `PopupMetaDataParser`

## Notes
`$columns` est surchargé par les sous-classes qui réduisent ou modifient les catégories de champs disponibles.
