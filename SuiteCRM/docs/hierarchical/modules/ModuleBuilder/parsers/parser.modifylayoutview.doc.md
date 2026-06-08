# parser.modifylayoutview.php

**Chemin :** `modules/ModuleBuilder/parsers/parser.modifylayoutview.php`
**Type :** PHP (model / parser)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Parser de layout pour les vues en grille (EditView, DetailView, QuickCreate). Charge les définitions de panneaux et champs depuis les fichiers de metadata, gère l'édition (ajout/suppression de slots), et sauvegarde vers le fichier custom ou le fichier de travail (working file).

## Type
model

## Dépendances clés
- `ModuleBuilderParser` (classe parente)
- `TemplateHandler` (`include/TemplateHandler/`) — invalidation du cache de templates
- `$beanList`, `$beanFiles` (globals) — chargement du bean pour les field_defs

## Exports/Symboles principaux
- `ParserModifyLayoutView` — classe (hérite de `ModuleBuilderParser`)
  - `init($module, $view, $submittedLayout)` — initialise (détermine le fichier source : working > custom > base)
  - `getAvailableFields()` — champs disponibles (dans le modèle mais pas dans la vue)
  - `getLayout()` — retourne les panels courants
  - `writeWorkingFile()` — sauvegarde dans `custom/working/modules/{Module}/metadata/`
  - `handleSave()` — sauvegarde dans `custom/modules/{Module}/metadata/` + vide le cache template
  - `_loadLayoutFromRequest()` — reconstruit les panels depuis `$_REQUEST` (format `slot-panel#-slot#-property`)
  - `_padFields()` — ajoute les slots (empty) manquants pour l'affichage
  - `_parseData($panels)` — normalise le format des panels (gère un seul panel sans niveau panel)
  - `_getModelFields()` — tous les champs éligibles au layout
  - `_getOrigFieldViewDefs()` — champs de la définition originale (base)

## Interactions
- **Appelé par :** vues de layout ModuleBuilder (view.layoutview.php, etc.)
- **Appelle :** `TemplateHandler::clearCache()`, `ModuleBuilderParser::_loadFromFile()`, `_writeToFile()`

## Notes
- Gère le format QuickCreate spécial : si pas de quickcreatedefs.php, utilise editviewdefs.php comme source. Ligne 92.
- Le format des slots dans `$_REQUEST` est `slot-{panel#}-{slot#}-{property}`. Ligne 207.
- `usingWorkingFile` (booléen) est exposé publiquement pour que les vues sachent si un brouillon existe.
