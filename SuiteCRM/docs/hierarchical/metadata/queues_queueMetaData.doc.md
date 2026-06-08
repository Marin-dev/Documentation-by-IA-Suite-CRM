# queues_queueMetaData.php

**Chemin :** `metadata/queues_queueMetaData.php`
**Type :** config (métadonnées de table de hiérarchie de files d'attente)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table `queues_queue` qui matérialise la relation hiérarchique (parent-enfant) entre les files d'attente (`Queues`). Permet de créer des files d'attente imbriquées / sous-queues.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['queues_queue']` | variable globale PHP | Définition de la table d'auto-référence files d'attente |

### Structure de la table `queues_queue`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | id | Clé primaire UUID (requis) |
| `deleted` | bool | Soft delete (requis, défaut : 0) |
| `date_entered` | datetime | Date d'entrée (requis) |
| `date_modified` | datetime | Horodatage (requis) |
| `queue_id` | id | FK vers une file d'attente enfant (requis) |
| `parent_id` | id | FK vers la file d'attente parente (requis) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `queues_queuepk` | primary | `id` |
| `idx_queue_id` | index | `queue_id` |
| `idx_parent_id` | index | `parent_id` |
| `compidx_queue_id_parent_id` | alternate_key | `queue_id`, `parent_id` |

### Relations auto-référentielles

| Relation | Description |
|---|---|
| `child_queues_rel` | Files d'attente enfants d'une file parente |
| `parent_queues_rel` | File d'attente parente d'une file enfant |

## Notes

- Relation auto-référentielle sur `queues` : LHS = RHS = module `Queues`.
- Les deux relations `child_queues_rel` et `parent_queues_rel` représentent la même relation physique dans les deux sens.
