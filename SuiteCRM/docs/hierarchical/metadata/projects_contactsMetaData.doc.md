# projects_contactsMetaData.php

**Chemin :** `metadata/projects_contactsMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `projects_contacts` qui matérialise la relation many-to-many entre les projets (`Project`) et les contacts (`Contacts`).

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['projects_contacts']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `projects_contacts`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `contact_id` | varchar(36) | FK vers `contacts.id` |
| `project_id` | varchar(36) | FK vers `project.id` |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Relation

- **Type :** many-to-many
- **LHS :** module `Project`, table `project`, clé `id`
- **RHS :** module `Contacts`, table `contacts`, clé `id`

## Notes

- RAS.
