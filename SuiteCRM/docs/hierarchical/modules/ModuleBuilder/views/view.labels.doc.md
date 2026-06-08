# view.labels.php

**Chemin :** `modules/ModuleBuilder/views/view.labels.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue de l'éditeur de labels pour les modules Studio (déployés). Hérite de `ViewModulefields`. Affiche la liste des labels du module avec possibilité d'édition inline multi-langue.

## Type
view

## Dépendances clés
- `ViewModulefields` (classe parente — hérite)
- `AjaxCompose`

## Exports/Symboles principaux
- `ViewLabels` — classe (hérite de `ViewModulefields`)

## Interactions
- **Rendue par :** `action_view_map.php` (INCONNU — action `labels`)
- **Action contrôleur :** `action_editLabels()` -> `$this->view = 'labels'`
