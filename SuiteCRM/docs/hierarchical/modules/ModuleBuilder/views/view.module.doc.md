# view.module.php

**Chemin :** `modules/ModuleBuilder/views/view.module.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue de détail d'un module MB (package). Affiche les informations du module et les liens de navigation (champs, labels, relations, layouts) via `AjaxCompose`.

## Type
view

## Dépendances clés
- `SugarView` (parente)
- `AjaxCompose`

## Exports/Symboles principaux
- `ViewModule` — classe
  - `$mbModule` — propriété publique (module MB en cours)

## Interactions
- **Rendue par :** `action_view_map.php` -> `'module' => 'module'`
