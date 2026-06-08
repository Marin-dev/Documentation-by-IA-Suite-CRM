# securitygroups_acl_rolesMetaData.php

**Chemin :** `metadata/securitygroups_acl_rolesMetaData.php`
**Type :** config (métadonnées de table de jointure sécurité)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `securitygroups_acl_roles` qui associe des groupes de sécurité (`SecurityGroups`) à des rôles ACL (`ACLRoles`). Permet d'attribuer des droits ACL à un groupe de sécurité entier.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['securitygroups_acl_roles']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `securitygroups_acl_roles`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | char(36) | Clé primaire UUID (requis) |
| `securitygroup_id` | char(36) | FK vers `securitygroups.id` |
| `role_id` | char(36) | FK vers `acl_roles.id` |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete (requis, défaut : 0) |

### Relation

- **Type :** many-to-many
- **LHS :** module `SecurityGroups`, table `securitygroups`, clé `id`
- **RHS :** module `ACLRoles`, table `acl_roles`, clé `id`

## Notes

- Pas de garde `sugarEntry` dans ce fichier.
- Utilise `char` au lieu de `varchar` pour les UUID — légère différence par rapport aux autres fichiers.
