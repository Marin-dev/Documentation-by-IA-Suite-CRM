# SaveSecurityGroupUserRelationship.php

**Chemin :** `modules/SecurityGroups/SaveSecurityGroupUserRelationship.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Script d'action qui sauvegarde les modifications d'une relation groupe-utilisateur : flags `noninheritable` et `primary_group`. Si `primary_group=1`, reinitialise les autres groupes principaux de l'utilisateur.

## Type
controller (action script)

## Dependances cles
- `SecurityGroupUserRelationship`
- `include/utils.php` (`safe_map`)
- `DBManagerFactory` — requete UPDATE pour reset des primary_group
- `$_REQUEST['record']`

## Interactions
- **Appelle :** `$focus->save()`, `$db->query()` (UPDATE securitygroups_users)
- **Appele par :** formulaire `SecurityGroupUserRelationshipEdit.php`

## Notes
- Controle d'acces : seul un admin ou le proprio des donnees peut modifier (ligne 23-29).
- Redirige vers `return_action/return_module/return_id`.
