# view.dashlet.php

**Chemin :** `modules/ModuleBuilder/views/view.dashlet.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue de l'éditeur de layout Dashlet. Affiche l'interface d'édition des colonnes du dashlet (liste et recherche).

## Type
view

## Dépendances clés
- `SugarView` (parente)
- `ParserFactory`, `AjaxCompose`, `constants.php`

## Exports/Symboles principaux
- `ViewDashlet` (ou similaire) — classe

## Interactions
- **Rendue par :** `ModuleBuilderController::action_editLayout()` -> `$this->view = 'dashlet'`
