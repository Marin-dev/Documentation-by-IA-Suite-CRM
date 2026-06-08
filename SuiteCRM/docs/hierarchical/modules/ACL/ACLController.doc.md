# ACLController.php

**Chemin :** `modules/ACL/ACLController.php`
**Type :** `PHP`
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Controleur principal du systeme ACL (Access Control List) de SuiteCRM. Point d'entree pour toutes les verifications d'acces utilisateur : peut-il acceder a un module, effectuer une action, possede-t-il l'enregistrement ?

## Type
service / controller

## Dependances cles
- `ACLAction` (modules/ACLActions) — verification d'acces par action
- `modules/ACLActions/actiondefs.php` (ou `actiondefs.override.php`) — definitions des actions
- `ACLJSController` — export des regles ACL vers JavaScript
- `$current_user`, `is_admin()`

## Exports / Symboles principaux
- `class ACLController`
- **Methodes statiques cles :**
  - `checkAccess($category, $action, $is_owner, $type, $in_group)` — verifie si l'utilisateur a acces (admin => toujours true). Gere les cas speciaux : Calendar, Activities, AOS_Products_Quotes, AOR_Reports/EmailAddresses
  - `requireOwner($category, $value, $type)` — verifie si la propriete est requise
  - `requireSecurityGroup($category, $value, $type)` — verifie si appartenance a un groupe est requise
  - Autres methodes : INCONNU (voir reste du fichier non lu)

## Interactions
- **Appelle :** `ACLAction::userHasAccess()`, `ACLAction::userNeedsOwnership()`, `ACLAction::userNeedsSecurityGroup()`
- **Appele par :** partout dans SuiteCRM : Menu.php de chaque module, vues, hooks

## Notes
- Parametre `$in_group` ajoute par SecurityGroups (tag `BEGIN - SECURITY GROUPS`).
- `checkAccess` pour `Calendar` : delègue aux modules Calls, Meetings, Tasks.
- `actiondefs.override.php` permet de surcharger les definitions par defaut.
