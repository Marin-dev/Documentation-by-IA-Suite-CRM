# SubpanelMetaDataParser.php

**Chemin :** `modules/ModuleBuilder/parsers/views/SubpanelMetaDataParser.php`
**Type :** PHP (model / parser)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Parser pour les subpanels (panels de liste dans les vues détail). Hérite de `ListLayoutMetaDataParser` et adapte pour le format subpanel (colonnes `LBL_DEFAULT` et `LBL_HIDDEN` seulement, identifiant de label = `vname`).

## Type
model

## Dépendances clés
- `ListLayoutMetaDataParser` (classe parente)
- `DeployedSubpanelImplementation` / `UndeployedSubpanelImplementation` (selon contexte)
- `constants.php`

## Exports/Symboles principaux
- `SubpanelMetaDataParser` — classe
  - `$columns` — `LBL_DEFAULT`, `LBL_HIDDEN`
  - `$labelIdentifier` — `'vname'` (au lieu de `'label'`)
  - `$_invisibleFields` — champs masqués

## Interactions
- **Créé par :** `ParserFactory::getParser()` pour MB_LISTVIEW avec `$subpanelName` non null
