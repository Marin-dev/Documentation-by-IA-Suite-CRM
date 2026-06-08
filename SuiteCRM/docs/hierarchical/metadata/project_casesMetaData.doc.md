# project_casesMetaData.php

**Chemin :** `metadata/project_casesMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `projects_cases` qui matérialise la relation many-to-many entre les projets (`Project`) et les cas support (`Cases`). Permet de lier des cas à un projet.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['projects_cases']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `projects_cases`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `case_id` | varchar(36) | FK vers `cases.id` |
| `project_id` | varchar(36) | FK vers `project.id` |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Relation

- **Type :** many-to-many
- **LHS :** module `Project`, table `project`, clé `id`
- **RHS :** module `Cases`, table `cases`, clé `id`

## Notes

- RAS. Même pattern que `project_bugsMetaData`.
