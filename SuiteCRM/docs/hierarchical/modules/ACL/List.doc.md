# List.php

**Chemin :** `modules/ACL/List.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Dispatcher de liste ACL : selon `$_REQUEST['submodule']`, inclut soit la vue liste des roles (`Roles/ListView.php`) soit la liste des utilisateurs (`Roles/ListUsers.php`).

## Type
controller (dispatcher)

## Dependances cles
- `modules/ACL/Roles/ListView.php`
- `modules/ACL/Roles/ListUsers.php`

## Interactions
- **Appele par :** framework SuiteCRM (action=List dans module ACL)

## Notes
- Fichier minimal de dispatch.
