# project_bugsMetaData.php

**Chemin :** `metadata/project_bugsMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `projects_bugs` qui matérialise la relation many-to-many entre les projets (`Project`) et les bogues (`Bugs`). Permet de lier des bogues à un projet.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['projects_bugs']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `projects_bugs`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `bug_id` | varchar(36) | FK vers `bugs.id` |
| `project_id` | varchar(36) | FK vers `project.id` |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Relation

- **Type :** many-to-many
- **LHS :** module `Project`, table `project`, clé `id`
- **RHS :** module `Bugs`, table `bugs`, clé `id`

## Notes

- Commentaire source ligne 44 : "adding project-to-bugs relationship".
