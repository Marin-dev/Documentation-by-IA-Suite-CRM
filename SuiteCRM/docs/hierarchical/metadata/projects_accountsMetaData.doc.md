# projects_accountsMetaData.php

**Chemin :** `metadata/projects_accountsMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `projects_accounts` qui matérialise la relation many-to-many entre les projets (`Project`) et les comptes (`Accounts`).

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['projects_accounts']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `projects_accounts`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `account_id` | varchar(36) | FK vers `accounts.id` |
| `project_id` | varchar(36) | FK vers `project.id` |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Relation

- **Type :** many-to-many
- **LHS :** module `Project`, table `project`, clé `id`
- **RHS :** module `Accounts`, table `accounts`, clé `id`

## Notes

- RAS.
