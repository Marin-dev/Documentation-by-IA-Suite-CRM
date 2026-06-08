# view.popupview.php

**Chemin :** `modules/ModuleBuilder/views/view.popupview.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue de l'éditeur de layout Popup (popuplist, popupsearch). Affiche l'interface d'édition des colonnes des vues popup.

## Type
view

## Dépendances clés
- `SugarView` (parente)
- `ParserFactory`, `AjaxCompose`

## Exports/Symboles principaux
- `ViewPopupview` (ou similaire) — classe

## Interactions
- **Rendue par :** `ModuleBuilderController::action_editLayout()` -> `$this->view = 'popupview'`
- **Action :** `action_popupSave()` -> `$this->view = 'popupview'`
