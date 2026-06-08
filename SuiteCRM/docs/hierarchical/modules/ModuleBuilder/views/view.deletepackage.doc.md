# view.deletepackage.php

**Chemin :** `modules/ModuleBuilder/views/view.deletepackage.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue de confirmation de suppression d'un package MB. Affiche un message de confirmation après suppression.

## Type
view

## Dépendances clés
- `SugarView` (parente)
- `AjaxCompose`

## Exports/Symboles principaux
- `ViewDeletepackage` (ou similaire) — classe

## Interactions
- **Rendue par :** `ModuleBuilderController::action_DeletePackage()` -> `$this->view = 'deletepackage'`
