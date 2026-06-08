# Save.php

**Chemin :** `modules/Roles/Save.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Script d'action qui sauvegarde un role : nom, description, et liste des modules autorises/refus depuis les onglets de navigation.

## Type
controller (action script)

## Dependances cles
- `BeanFactory::newBean('Roles')` — bean Role
- `$_REQUEST['display_tabs_def']`, `$_REQUEST['hide_tabs_def']` — listes de modules (URL-encoded, separees par `:::`)

## Interactions
- **Appelle :** `$focus->save()`, `$focus->clear_module_relationship()`, `$focus->set_module_relationship()`
- **Appele par :** formulaire EditView du module Roles

## Notes
- `print_r($_POST)` laisse un debug non supprime (ligne 60) — dette technique.
- Redirige vers DetailView apres sauvegarde.
