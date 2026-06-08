# 📄 ACLRole.php

**Chemin :** `modules/ACLRoles/ACLRole.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Modèle représentant un rôle ACL dans SuiteCRM. Un rôle définit un ensemble de niveaux d'accès par module et par action. Les rôles sont assignés aux utilisateurs ou aux groupes de sécurité pour contrôler finement leurs permissions.

## Rôle technique

Classe `ACLRole` héritant de `SugarBean` (table `acl_roles`). Fournit des méthodes pour lire les actions d'un rôle, les assigner aux utilisateurs, et les nettoyer. La résolution des noms de rôles bénéficie d'un cache sugar (`sugar_cache_put/retrieve`).

---

## Dépendances clés

- `SugarBean` — classe parente ORM
- `DBManagerFactory::getInstance()` — accès DB
- `BeanFactory::newBean('ACLRoles')` / `BeanFactory::newBean('ACLActions')` — instanciation
- `sugar_cache_put/retrieve` — cache de noms de rôles
- Tables DB : `acl_roles`, `acl_roles_users`, `acl_roles_actions`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ACLRole` | classe | Modèle d'un rôle ACL |
| `setAction($role_id, $action_id, $access)` | méthode | Définit le niveau d'accès d'une action pour ce rôle |
| `getUserRoles($user_id, $getAsNameArray)` | méthode | Retourne les rôles d'un utilisateur |
| `getUserRoleNames($user_id)` | méthode statique | Retourne les noms de rôles (avec cache sugar) |
| `getAllRoles($returnAsArray)` | méthode | Retourne tous les rôles |
| `getRoleActions($role_id, $type)` | méthode | Retourne les actions d'un rôle avec les overrides de la DB |
| `mark_relationships_deleted($id)` | méthode | Supprime les `acl_roles_actions` lors de la suppression du rôle |
| `toArray()` | méthode | Sérialise le rôle (id, name, description) |

## Consommateurs identifiés

- `modules/ACLRoles/EditView.php`, `DetailView.php`, `Save.php` — gestion CRUD
- `modules/ACLActions/ACLAction.php` — `getUserActions()` lit les rôles via DB
- Framework SecurityGroups — `securitygroups_acl_roles` lie des rôles aux groupes

---

## Relations clés

- **Appelé par :** vues ACLRoles, `ACLAction::getUserActions()`
- **Appelle :** `DBManagerFactory`, `BeanFactory`, `sugar_cache`
- **Position dans le flux global :** définition des permissions par rôle, complète le système ACL

---

## Notes

- `disable_row_level_security = true` — les rôles ne sont pas eux-mêmes soumis aux SecurityGroups.
- `disable_custom_fields = true` — pas de champs personnalisés via Studio.
- La suppression d'un rôle déclenche `mark_relationships_deleted()` qui met `deleted=1` dans `acl_roles_actions` (ligne 257).
- `getRoleActions()` filtre les modules absents de `$beanList` (modules désinstallés) — ligne 217.
