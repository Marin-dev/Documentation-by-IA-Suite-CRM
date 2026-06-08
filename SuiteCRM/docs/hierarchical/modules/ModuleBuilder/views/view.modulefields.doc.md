# view.modulefields.php

**Chemin :** `modules/ModuleBuilder/views/view.modulefields.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue de la liste des champs d'un module (Studio ou MB). Affiche la liste des champs avec leur type, label, et options d'édition.

## Type
view

## Dépendances clés
- `SugarView` (parente)
- `AjaxCompose`
- `view.modulefield.php` (inclus)

## Exports/Symboles principaux
- `ViewModulefields` — classe
  - `$mbModule` — module en cours

## Interactions
- **Rendue par :** `action_view_map.php` -> `'modulefields' => 'modulefields'`
