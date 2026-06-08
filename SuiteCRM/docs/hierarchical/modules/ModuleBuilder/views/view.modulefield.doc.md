# view.modulefield.php

**Chemin :** `modules/ModuleBuilder/views/view.modulefield.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue du formulaire d'édition d'un champ individuel. Utilise `FieldViewer` pour afficher le formulaire dynamique d'édition des propriétés du champ.

## Type
view

## Dépendances clés
- `SugarView` (parente)
- `AjaxCompose`
- `FieldViewer` (`modules/DynamicFields/FieldViewer.php`)

## Exports/Symboles principaux
- `ViewModulefield` — classe

## Interactions
- **Rendue par :** `action_view_map.php` -> `'modulefield' => 'modulefield'`
- **Incluse par :** `view.modulefields.php`
