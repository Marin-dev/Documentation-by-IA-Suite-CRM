# view.dropdowns.php

**Chemin :** `modules/ModuleBuilder/views/view.dropdowns.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue de la liste de tous les dropdowns disponibles. Affiche l'ensemble des dropdowns (app_list_strings) avec liens vers leur éditeur individuel.

## Type
view

## Dépendances clés
- `SugarView` (parente)
- `AjaxCompose`

## Exports/Symboles principaux
- `ViewDropdowns` — classe

## Interactions
- **Rendue par :** `action_view_map.php` -> `'dropdowns' => 'dropdowns'`
- **Action contrôleur :** `action_SaveDropDown()` -> `$this->view = 'dropdowns'`
