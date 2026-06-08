# SearchViewMetaDataParser.php

**Chemin :** `modules/ModuleBuilder/parsers/views/SearchViewMetaDataParser.php`
**Type :** PHP (model / parser)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Parser pour les vues de recherche (basic_search, advanced_search). Hérite de `ListLayoutMetaDataParser` et adapte la logique pour les formulaires de recherche. Gère également `SearchFields.php` via `ParserSearchFields`.

## Type
model

## Dépendances clés
- `ListLayoutMetaDataParser` (classe parente)
- `constants.php`
- `ParserSearchFields` (INCONNU — référence probable dans handleSave)

## Exports/Symboles principaux
- `SearchViewMetaDataParser` — classe
  - `$variableMap` — mapping `MB_BASICSEARCH => 'basic_search'`, `MB_ADVANCEDSEARCH => 'advanced_search'`
  - `$columns` — seulement `LBL_DEFAULT` et `LBL_HIDDEN` (pas de `LBL_AVAILABLE`)
  - `$allowParent` — booléen (true) autorisant les champs parent

## Interactions
- **Créé par :** `ParserFactory::getParser()` pour MB_BASICSEARCH et MB_ADVANCEDSEARCH
- **Appelé par :** `ModuleBuilderController::action_searchViewSave()`

## Notes
`ModuleBuilderController::action_searchViewSave()` utilise directement `new SearchViewMetaDataParser()` plutôt que `ParserFactory` (ligne 798 du contrôleur). Répare aussi les `SearchFields.php` via `TemplateRange::repairCustomSearchFields()`.
