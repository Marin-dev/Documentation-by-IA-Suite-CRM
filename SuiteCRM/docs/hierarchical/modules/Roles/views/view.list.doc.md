# view.list.php

**Chemin :** `modules/Roles/views/view.list.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Vue liste du module Roles. Surcharge `preDisplay()` pour desactiver le mass update.

## Type
view

## Exports / Symboles principaux
- `class RolesViewList extends ViewList`
- `preDisplay()` — instancie `ListViewSmarty` avec `showMassupdateFields = false`

## Notes
- Pas de masse-update pour les roles.
