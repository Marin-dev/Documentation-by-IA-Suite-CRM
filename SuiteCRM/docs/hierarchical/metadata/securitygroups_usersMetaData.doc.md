# securitygroups_usersMetaData.php

**Chemin :** `metadata/securitygroups_usersMetaData.php`
**Type :** config (métadonnées de table de jointure sécurité-utilisateurs)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `securitygroups_users` qui associe des groupes de sécurité (`SecurityGroups`) à des utilisateurs (`Users`). Inclut des indicateurs pour le groupe principal et l'héritage.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['securitygroups_users']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `securitygroups_users`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete (requis, défaut : 0) |
| `securitygroup_id` | varchar(36) | FK vers `securitygroups.id` |
| `user_id` | varchar(36) | FK vers `users.id` |
| `primary_group` | bool | Groupe principal de l'utilisateur |
| `noninheritable` | bool | Le groupe ne peut pas être hérité par les enregistrements |

### Index (4 index)

| Nom | Type | Champs |
|---|---|---|
| `securitygroups_usersspk` | primary | `id` |
| `securitygroups_users_idxa` | index | `securitygroup_id` |
| `securitygroups_users_idxb` | index | `user_id` |
| `securitygroups_users_idxc` | index | `user_id`, `deleted`, `securitygroup_id`, `id` |
| `securitygroups_users_idxd` | index | `user_id`, `deleted`, `securitygroup_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `SecurityGroups`, table `securitygroups`, clé `id`
- **RHS :** module `Users`, table `users`, clé `id`

## Interactions

- **Appelé par :** module SecurityGroups, gestion des utilisateurs
- **Appelle :** rien

## Notes

- `primary_group` : commenter ligne 37 explique que si un utilisateur est membre de plusieurs groupes, ce champ détermine quel layout personnalisé afficher.
- `noninheritable` : commenter ligne 43 explique qu'un groupe non-héritable ne se propage pas automatiquement aux enregistrements créés par l'utilisateur.
- Pas de garde `sugarEntry`.
