# view.property.php

**Chemin :** `modules/ModuleBuilder/views/view.property.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue d'édition d'une propriété (label/titre) d'une section ou d'un panneau. Utilisée par les éditeurs de layout pour modifier les titres de panneaux.

## Type
view

## Dépendances clés
- `SugarView` (parente)
- `AjaxCompose`

## Exports/Symboles principaux
- `ViewProperty` (ou similaire) — classe

## Interactions
- **Rendue par :** `ModuleBuilderController::action_EditProperty()` -> `$this->view = 'property'`
