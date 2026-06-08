# view.layoutview.php

**Chemin :** `modules/ModuleBuilder/views/view.layoutview.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue de l'éditeur de layout en grille (EditView, DetailView, QuickCreate). Affiche l'éditeur drag-and-drop des champs dans les panneaux.

## Type
view

## Dépendances clés
- `SugarView` (parente)
- `ParserFactory`, `AjaxCompose`, `constants.php`

## Exports/Symboles principaux
- `ViewLayoutview` (ou similaire) — classe (nom exact INCONNU — partiellement lu)

## Interactions
- **Rendue par :** `ModuleBuilderController::action_editLayout()` via `$this->view = 'layoutView'`
