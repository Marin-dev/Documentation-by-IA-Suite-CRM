# acl_roles_usersMetaData.php

**Chemin :** `metadata/acl_roles_usersMetaData.php`
**Type :** config (métadonnées de table de jointure ACL)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `acl_roles_users` qui associe des rôles ACL (`ACLRoles`) à des utilisateurs (`Users`). Permet d'attribuer un ou plusieurs rôles de sécurité à chaque utilisateur SuiteCRM.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Protégé par la constante `sugarEntry`.

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['acl_roles_users']` | variable globale PHP | Définition de la table ACL rôles-utilisateurs |

### Structure de la table `acl_roles_users`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `role_id` | varchar(36) | FK vers `acl_roles.id` |
| `user_id` | varchar(36) | FK vers `users.id` |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `acl_roles_userspk` | primary | `id` |
| `idx_aclrole_id` | index | `role_id` |
| `idx_acluser_id` | index | `user_id` |
| `idx_aclrole_user` | alternate_key | `role_id`, `user_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `ACLRoles`, table `acl_roles`, clé `id`
- **RHS :** module `Users`, table `users`, clé `id`
- **Table de jointure :** `acl_roles_users`

## Interactions

- **Appelé par :** framework SugarCRM (dictionnaire de schéma, moteur ACL)
- **Appelle :** rien

## Notes

- Table critique pour la sécurité : lie utilisateurs et rôles ACL.
- Fonctionne en tandem avec `acl_roles_actions` pour former le système de droits complet.
