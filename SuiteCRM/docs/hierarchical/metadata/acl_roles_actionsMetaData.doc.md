# acl_roles_actionsMetaData.php

**Chemin :** `metadata/acl_roles_actionsMetaData.php`
**Type :** config (métadonnées de table de jointure ACL)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `acl_roles_actions` qui associe des rôles ACL (`ACLRoles`) à des actions ACL (`ACLActions`). Pilier du système de contrôle d'accès (ACL) de SuiteCRM : permet d'attribuer des droits d'accès précis par rôle et par action.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Protégé par la constante `sugarEntry`.

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['acl_roles_actions']` | variable globale PHP | Définition de la table ACL rôles-actions |

### Structure de la table `acl_roles_actions`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `role_id` | varchar(36) | FK vers `acl_roles.id` |
| `action_id` | varchar(36) | FK vers `acl_actions.id` |
| `access_override` | int(3) | Valeur de surcharge du niveau d'accès (nullable) |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `acl_roles_actionspk` | primary | `id` |
| `idx_acl_role_id` | index | `role_id` |
| `idx_acl_action_id` | index | `action_id` |
| `idx_aclrole_action` | alternate_key | `role_id`, `action_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `ACLRoles`, table `acl_roles`, clé `id`
- **RHS :** module `ACLActions`, table `acl_actions`, clé `id`
- **Table de jointure :** `acl_roles_actions`

## Interactions

- **Appelé par :** framework SugarCRM (dictionnaire de schéma, moteur ACL)
- **Appelle :** rien

## Notes

- Le champ `access_override` est spécifique à cette table de jointure : il permet de surcharger le niveau d'accès standard défini par l'action pour un rôle donné.
- Table critique pour la sécurité : toute modification impacte directement les droits utilisateurs.
