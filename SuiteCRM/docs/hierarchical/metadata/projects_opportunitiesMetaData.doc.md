# projects_opportunitiesMetaData.php

**Chemin :** `metadata/projects_opportunitiesMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `projects_opportunities` qui matérialise la relation many-to-many entre les projets (`Project`) et les opportunités (`Opportunities`).

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['projects_opportunities']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `projects_opportunities`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `opportunity_id` | varchar(36) | FK vers `opportunities.id` |
| `project_id` | varchar(36) | FK vers `project.id` |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Relation

- **Type :** many-to-many
- **LHS :** module `Project`, table `project`, clé `id`
- **RHS :** module `Opportunities`, table `opportunities`, clé `id`

## Notes

- RAS.
