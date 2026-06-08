# view.home.php

**Chemin :** `modules/ModuleBuilder/views/view.home.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue de la page d'accueil ModuleBuilder. Affiche les sections Studio, Module Builder et Dropdown Editor selon les droits de l'utilisateur, en utilisant `AjaxCompose`.

## Type
view

## Dépendances clés
- `SugarView` (parente)
- `AjaxCompose` (`MB/AjaxCompose.php`)
- `ModuleBuilderController::getModuleTitle()` — titre de la section

## Exports/Symboles principaux
- `ViewHome` — classe

## Interactions
- **Rendue par :** `action_view_map.php` -> `'home' => 'home'`
