# queues_beansMetaData.php

**Chemin :** `metadata/queues_beansMetaData.php`
**Type :** config (métadonnées de table de jointure file d'attente-beans)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table `queues_beans` qui associe des éléments (beans) à une file d'attente (`Queues`). Table de jointure polymorphe permettant à une file d'attente de contenir différents types d'objets (principalement des emails).

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['queues_beans']` | variable globale PHP | Définition de la table |

### Structure de la table `queues_beans`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | id | Clé primaire UUID (requis) |
| `deleted` | bool | Soft delete (requis, défaut : 0) |
| `date_entered` | datetime | Date d'entrée dans la file (requis) |
| `date_modified` | datetime | Horodatage (requis) |
| `queue_id` | id | FK vers `queues.id` (requis) |
| `module_dir` | varchar(30) | Module du bean (discriminant polymorphe, requis) |
| `object_id` | id | UUID du bean (requis) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `queues_itemspk` | primary | `id` |
| `idx_queue_id` | index | `queue_id` |
| `idx_object_id` | index | `object_id` |

### Relation

- **Type :** many-to-many (discriminant `module_dir`)
- `queues_emails_rel` : Files d'attente ↔ Emails (valeur `module_dir` = `Emails`)

## Notes

- Polymorphe via `module_dir` : extensible à d'autres modules que Emails.
