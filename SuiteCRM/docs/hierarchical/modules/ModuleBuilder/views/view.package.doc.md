# view.package.php

**Chemin :** `modules/ModuleBuilder/views/view.package.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue de détail d'un package ModuleBuilder. Affiche les propriétés du package (auteur, description, clé, modules) et les actions disponibles (build, deploy, export, delete).

## Type
view

## Dépendances clés
- `SugarView` (parente)
- `AjaxCompose`, `ModuleBuilder`

## Exports/Symboles principaux
- `ViewPackage` — classe

## Interactions
- **Rendue par :** `action_view_map.php` -> `'package' => 'package'`
- **Action contrôleur :** `action_SavePackage()` -> `$this->view = 'package'`
