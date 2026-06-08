# DeleteUserRelationship.php

**Chemin :** `modules/Roles/DeleteUserRelationship.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Script d'action qui retire un utilisateur d'un role (suppression de la relation dans `roles_users`).

## Type
controller (action script)

## Dependances cles
- `BeanFactory::newBean('Roles')`
- `$_REQUEST['user_id']`, `$_REQUEST['record']`

## Interactions
- **Appelle :** `$focus->clear_user_relationship($focus->id, $_REQUEST['user_id'])`
- **Appele par :** sous-panneau Users de la vue detail Roles

## Notes
- Redirige vers return_action/return_module/return_id.
