# project_contacts_1MetaData.php

**Chemin :** `metadata/project_contacts_1MetaData.php`
**Type :** config (métadonnées de table de jointure générée par Studio)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `project_contacts_1_c` qui matérialise la relation many-to-many entre les projets (`Project`) et les contacts (`Contacts`). Généré par Studio le 2014-06-24.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['project_contacts_1']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `project_contacts_1_c`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage |
| `deleted` | bool(1) | Soft delete |
| `project_contacts_1project_ida` | varchar(36) | FK vers `project.id` |
| `project_contacts_1contacts_idb` | varchar(36) | FK vers `contacts.id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `Project`, table `project`, clé `id`
- **RHS :** module `Contacts`, table `contacts`, clé `id`

## Notes

- Généré par Studio le 2014-06-24.
