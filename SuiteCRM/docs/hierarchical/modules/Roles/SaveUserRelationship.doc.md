# SaveUserRelationship.php

**Chemin :** `modules/Roles/SaveUserRelationship.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Script d'action qui assigne plusieurs utilisateurs a un role depuis la popup de selection d'utilisateurs. Ajoute les relations dans `roles_users`.

## Type
controller (action script)

## Dependances cles
- `BeanFactory::newBean('Roles')`
- `$_REQUEST['mass']` — tableau d'user_id selectionnees
- `$sugar_config['site_url']`

## Interactions
- **Appelle :** `$focus->set_user_relationship($focus->id, $_REQUEST['mass'])`
- **Appele par :** popup `PopupUsers` du module Roles

## Notes
- Utilise JS pour recharger la fenetre parente et rediriger vers `PopupUsers`.
