# ACLAction.php

**Chemin :** `modules/ACLActions/ACLAction.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Bean et service central du systeme ACL. Gere les actions d'acces (list, view, edit, delete, export, import...) par module et par utilisateur. Implementee avec support SecurityGroups (UNION query incluant les roles des groupes).

## Type
model / service

## Dependances cles
- `SugarBean` (heritage)
- `modules/ACLActions/actiondefs.php` — definitions des actions et niveaux d'acces
- `DBManagerFactory` — requetes directes
- `BeanFactory::newBean('ACLActions')`
- `$_SESSION['ACL'][$user_id]` — cache des ACL en session
- Tables DB : `acl_actions`, `acl_roles_actions`, `acl_roles_users`, `securitygroups_users`, `securitygroups_acl_roles`

## Exports / Symboles principaux
- `class ACLAction extends SugarBean`
- `disable_custom_fields = true`
- **Methodes statiques cles :**
  - `addActions($category, $type)` — ajoute les actions par defaut pour une categorie
  - `removeActions($category, $type)` — supprime les actions d'une categorie
  - `AccessColor($access)`, `AccessName($access)`, `AccessLabel($access)` — rendu des niveaux d'acces
  - `getAccessOptions($action, $type)` — options pour les select boxes
  - `getDefaultActions($type, $action)` — liste les actions par defaut
  - `getUserActions($user_id, $refresh, $category, $type, $action)` — recupere les ACL d'un utilisateur (cache session ou DB)
  - `userHasAccess()`, `userNeedsOwnership()`, `userNeedsSecurityGroup()`, `getUserAccessLevel()` — INCONNU (suite du fichier)
- Constantes (dans actiondefs.php) : `ACL_ALLOW_ADMIN_DEV=100`, `ACL_ALLOW_ADMIN=99`, `ACL_ALLOW_ALL=90`, `ACL_ALLOW_ENABLED=89`, `ACL_ALLOW_OWNER=75`, `ACL_ALLOW_NORMAL=1`, `ACL_ALLOW_DEFAULT=0`, `ACL_ALLOW_DISABLED=-98`, `ACL_ALLOW_NONE=-99`

## Interactions
- **Appelle :** `DBManagerFactory::getInstance()`, `BeanFactory::newBean('ACLActions')`, `$db->query()`
- **Appele par :** `ACLController::checkAccess`, partout dans SuiteCRM

## Notes
- La requete `getUserActions` utilise 3 UNION : roles utilisateur directs, roles via groupes de securite, et defauts globaux. Trie par `user_role DESC` pour privilegier les reglages specifiques.
- Cache en `$_SESSION['ACL'][$user_id]` — reinitialise sur `$refresh=true`.
