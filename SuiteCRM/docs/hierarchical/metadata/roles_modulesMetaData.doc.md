# roles_modulesMetaData.php

**Chemin :** `metadata/roles_modulesMetaData.php`
**Type :** config (métadonnées de table de jointure rôles-modules)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `roles_modules` qui associe des rôles (`Roles`, système de rôles hérité de SugarCRM) à des modules, avec un champ `allow` indiquant si l'accès est autorisé. Distinct du système ACL (`acl_roles_actions`).

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['roles_modules']` | variable globale PHP | Définition de la table |

### Structure de la table `roles_modules`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `role_id` | varchar(36) | FK vers `roles.id` (INCONNU — module Roles) |
| `module_id` | varchar(36) | FK vers un module (INCONNU — table source) |
| `allow` | bool(1) | Accès autorisé (défaut : 0) |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `roles_modulespk` | primary | `id` |
| `idx_role_id` | index | `role_id` |
| `idx_module_id` | index | `module_id` |

## Notes

- Pas de section `relationships` dans ce fichier.
- Système de rôles "Roles" distinct du système ACL "ACLRoles" — INCONNU si les deux coexistent ou si l'un est obsolète.
- `module_id` : INCONNU — référence probablement une table `acl_roles_modules` ou `modules` non définie ici.
