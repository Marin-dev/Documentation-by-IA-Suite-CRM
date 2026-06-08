# 📄 Role.php

**Chemin :** `modules/Roles/Role.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle fonctionnel

Modèle du module Roles (système de rôles hérité de SugarCRM CE). Ce système permet d'autoriser ou interdire l'accès à des modules entiers pour des utilisateurs. Distinct du système ACLRoles (granularité action) : ici la granularité est le module.

## Rôle technique

Classe `Role` héritant de `SugarBean` (table `roles`). Gère les relations `roles_modules` (modules autorisés/interdits) et `roles_users` (utilisateurs assignés au rôle). Fournit des méthodes de requête pour déterminer les modules accessibles/inaccessibles d'un utilisateur.

---

## Dépendances clés

- `SugarBean` — classe parente ORM
- `DBManager` (via `$this->db`) — accès DB
- `BeanFactory::newBean('Users')` — construction de la liste utilisateurs
- Tables DB : `roles`, `roles_modules`, `roles_users`
- `$moduleList` (global) — liste de tous les modules

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `Role` | classe | Modèle d'un rôle de module |
| `query_modules($allow)` | méthode | Retourne les module_id autorisés/interdits pour ce rôle |
| `set_module_relationship($role_id, &$mod_ids, $allow)` | méthode | Assigne des modules à un rôle |
| `clear_module_relationship($role_id)` | méthode | Supprime toutes les relations modules du rôle |
| `set_user_relationship($role_id, &$user_ids)` | méthode | Assigne des utilisateurs au rôle |
| `clear_user_relationship($role_id, $user_id)` | méthode | Retire un utilisateur du rôle |
| `query_user_allowed_modules($user_id)` | méthode | Modules autorisés pour un utilisateur |
| `query_user_disallowed_modules($user_id, &$allowed)` | méthode | Modules interdits pour un utilisateur |
| `get_users()` | méthode | Liste des utilisateurs du rôle |
| `check_user_role_count($user_id)` | méthode | Compte les rôles d'un utilisateur |

---

## Relations clés

- **Appelé par :** `modules/Roles/DetailView.php`, `EditView.php`, `Save.php`, `DeleteUserRelationship.php`
- **Appelle :** `DBManager`, `BeanFactory::newBean('Users')`
- **Position dans le flux global :** système de filtrage de modules (historique), complémentaire au système ACLRoles

---

## Notes

- Ce module `Roles` est le système LEGACY de SugarCRM CE (contrôle par module entier). Le système granulaire actuel est `ACLRoles`.
- `disable_row_level_security = true` — pas de SecurityGroups sur les rôles.
- Les suppressions dans `roles_modules` utilisent un DELETE direct (pas de soft delete) — ligne 122.
- `query_user_allowed_modules()` fait deux requêtes imbriquées sans optimisation — potentiellement lent sur de nombreux rôles.
