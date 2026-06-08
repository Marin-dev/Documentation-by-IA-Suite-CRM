# view.searchview.php

**Chemin :** `modules/ModuleBuilder/views/view.searchview.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue de l'éditeur de vue de recherche (basic_search, advanced_search). Affiche l'interface d'édition des champs du formulaire de recherche.

## Type
view

## Dépendances clés
- `SugarView` (parente)
- `ParserFactory`, `AjaxCompose`, `constants.php`

## Exports/Symboles principaux
- `ViewSearchview` (ou similaire) — classe

## Interactions
- **Rendue par :** `ModuleBuilderController::action_editLayout()` -> `$this->view = 'searchView'`
