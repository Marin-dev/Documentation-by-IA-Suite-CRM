# roles_usersMetaData.php

**Chemin :** `metadata/roles_usersMetaData.php`
**Type :** config (métadonnées de table de jointure rôles-utilisateurs)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `roles_users` qui associe des rôles du système `Roles` aux utilisateurs. Système de rôles hérité de SugarCRM, distinct du système `ACLRoles`.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['roles_users']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `roles_users`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `role_id` | varchar(36) | FK vers `roles.id` |
| `user_id` | varchar(36) | FK vers `users.id` |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Relation

- **Type :** many-to-many
- **LHS :** module `Roles`, table `roles`, clé `id`
- **RHS :** module `Users`, table `users`, clé `id`

## Notes

- Analogue à `acl_roles_users` mais pour le système de rôles `Roles` (ancien système SugarCRM vs. système ACL de SuiteCRM).
