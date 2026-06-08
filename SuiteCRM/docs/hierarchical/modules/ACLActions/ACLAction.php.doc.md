# 📄 ACLAction.php

**Chemin :** `modules/ACLActions/ACLAction.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Modèle et service central pour les actions ACL de SuiteCRM. Représente une action d'accès (ex : view, edit, delete) pour un module donné, avec son niveau d'accès. Fournit les méthodes statiques pour charger, tester et afficher les droits d'accès des utilisateurs, en tenant compte des rôles directs et des rôles de SecurityGroups.

## Rôle technique

Classe `ACLAction` héritant de `SugarBean` (table `acl_actions`). La méthode clé `getUserActions()` exécute une requête UNION de 3 parties : rôles utilisateur directs (`acl_roles_users`), rôles de groupes de sécurité (`securitygroups_acl_roles`), et actions par défaut. Le résultat est mis en cache dans `$_SESSION['ACL'][$user_id]`. Supporte le mode additif (accès le plus permissif) et le mode restrictif.

---

## Dépendances clés

- `modules/ACLActions/actiondefs.php` (ou `.override.php`) — `$ACLActions`, `$ACLActionAccessLevels`
- `SugarBean` — classe parente ORM
- `DBManagerFactory` — accès DB
- `BeanFactory::newBean('ACLActions')` — création d'instances
- `$_SESSION['ACL']` — cache des droits
- `$sugar_config['securitysuite_additive']`, `securitysuite_user_role_precedence` — modes de résolution
- Tables DB : `acl_actions`, `acl_roles_actions`, `acl_roles_users`, `securitygroups_users`, `securitygroups_acl_roles`

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ACLAction` | classe | Modèle d'une action ACL |
| `addActions($category, $type)` | méthode statique | Crée les actions par défaut pour un module |
| `removeActions($category, $type)` | méthode statique | Supprime les actions d'un module |
| `getUserActions($user_id, $refresh, $category, $type, $action)` | méthode statique | Retourne toutes les actions ACL de l'utilisateur (avec cache session) |
| `userHasAccess($user_id, $category, $action, $type, $is_owner, $in_group)` | méthode statique | Vérifie si l'utilisateur a accès à une action |
| `getUserAccessLevel($user_id, $category, $action, $type)` | méthode statique | Retourne le niveau d'accès numérique |
| `userNeedsOwnership($user_id, $category, $action, $type)` | méthode statique | Vérifie si la propriété est requise |
| `userNeedsSecurityGroup($user_id, $category, $action, $type)` | méthode statique | Vérifie si l'appartenance à un groupe est requise |
| `hasAccess($is_owner, $in_group, $access, $action)` | méthode statique | Évalue un niveau d'accès donné |
| `setupCategoriesMatrix(&$categories)` | méthode statique | Enrichit les catégories ACL avec couleurs/labels pour l'UI |
| `getDefaultActions($type, $action)` | méthode statique | Retourne les actions par défaut depuis la DB |
| `clearSessionCache()` | méthode | Vide le cache ACL de session |

## Consommateurs identifiés

- `modules/ACL/ACLController.php` — délégation de toutes les vérifications
- `modules/SecurityGroups/AssignGroups.php` — `getUserAccessLevel()`
- Framework SugarCRM (partout où les droits sont vérifiés)

---

## Relations clés

- **Appelé par :** `ACLController`, framework SugarCRM
- **Appelle :** `DBManagerFactory`, `BeanFactory`, cache `$_SESSION['ACL']`
- **Position dans le flux global :** couche de persistance et de calcul des droits ACL

---

## Notes

- La requête UNION (lignes 327-348) fusionne rôles directs (user_role=1), rôles de groupe (user_role=0) et défauts (user_role=-1). L'ordre de priorité dépend de `securitysuite_user_role_precedence`.
- Mode additif (`securitysuite_additive=true`) : le niveau d'accès le plus ÉLEVÉ parmi les rôles est retenu.
- Mode restrictif (défaut) : le niveau d'accès le plus BAS est retenu.
- `clearSessionCache()` doit être appelé après modification des rôles d'un utilisateur.
