# Role.php

**Chemin :** `modules/Roles/Role.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Modele du bean Role. Represente un role d'acces permettant de definir quels modules sont accessibles (allow/disallow) pour les utilisateurs qui lui sont assignes. Systeme d'ACL par module (ancien systeme Roles, different de ACLRoles).

## Type
model

## Dependances cles
- `SugarBean` (heritage)
- Tables DB : `roles`, `roles_modules`, `roles_users`
- `BeanFactory::newBean('Users')`

## Exports / Symboles principaux
- `class Role extends SugarBean`
- `disable_row_level_security = true`
- Methodes :
  - `query_modules($allow)` — liste les module_id autorises ou bloques pour ce role
  - `set_module_relationship($role_id, $mod_ids, $allow)` — cree les relations role-module
  - `clear_module_relationship($role_id)` — supprime toutes les relations role-module
  - `set_user_relationship($role_id, $user_ids)` — assigne des utilisateurs au role
  - `clear_user_relationship($role_id, $user_id)` — retire un utilisateur du role
  - `query_user_allowed_modules($user_id)` — liste les modules autorises pour un utilisateur
  - `query_user_disallowed_modules($user_id, $allowed)` — liste les modules bloques
  - `get_users()` — retourne les utilisateurs assignes au role
  - `check_user_role_count($user_id)` — nombre de roles d'un utilisateur

## Interactions
- **Appele par :** `Save.php`, `Delete.php`, `SaveUserRelationship.php`, `DeleteUserRelationship.php`, framework SuiteCRM

## Notes
- Ce module Roles (legacy) gere les acces par module uniquement. Pour les acces granulaires par action, voir ACLRoles.
- `disable_row_level_security = true`.
