# project_users_1MetaData.php

**Chemin :** `metadata/project_users_1MetaData.php`
**Type :** config (métadonnées de table de jointure générée par Studio)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `project_users_1_c` qui matérialise la relation many-to-many entre les projets (`Project`) et les utilisateurs (`Users`). Généré par Studio le 2014-06-20.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['project_users_1']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `project_users_1_c`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete |
| `project_users_1project_ida` | varchar(36) | FK vers `project.id` |
| `project_users_1users_idb` | varchar(36) | FK vers `users.id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `Project`, table `project`, clé `id`
- **RHS :** module `Users`, table `users`, clé `id`

## Notes

- Généré par Studio le 2014-06-20.
