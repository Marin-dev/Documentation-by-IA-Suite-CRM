# view.listview.php

**Chemin :** `modules/ModuleBuilder/views/view.listview.php`
**Type :** PHP (view)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Vue de l'éditeur de liste (ListView, subpanels). Affiche les colonnes disponibles/défaut/cachées avec interface de glisser-déposer.

## Type
view

## Dépendances clés
- `SugarView` (parente)
- `constants.php`, `SubPanel` (`include/SubPanel/SubPanel.php`)

## Exports/Symboles principaux
- `ViewListView` — classe

## Interactions
- **Rendue par :** `ModuleBuilderController` via `$this->view = 'listView'`
