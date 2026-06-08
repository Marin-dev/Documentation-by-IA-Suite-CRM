# cron_remove_documentsMetaData.php

**Chemin :** `metadata/cron_remove_documentsMetaData.php`
**Type :** config (métadonnées de table de file d'attente cron)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table `cron_remove_documents` utilisée comme file d'attente pour la suppression différée de beans (documents, fichiers, etc.) par le planificateur (cron). Permet de marquer des enregistrements à supprimer physiquement lors de la prochaine exécution du cron.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['cron_remove_documents']` | variable globale PHP | Définition de la table de file d'attente |

### Structure de la table `cron_remove_documents`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `bean_id` | varchar(36) | UUID du bean à supprimer |
| `module` | varchar(25) | Module du bean à supprimer |
| `date_modified` | datetime | Horodatage (utilisé pour le nettoyage) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `cron_remove_documentspk` | primary | `id` |
| `idx_cron_remove_document_bean_id` | index | `bean_id` |
| `idx_cron_remove_document_stamp` | index | `date_modified` |

## Interactions

- **Appelé par :** planificateur SuiteCRM (cron), processus de suppression différée
- **Appelle :** rien

## Notes

- Pas de champ `deleted` : cette table est vidée progressivement par le cron après traitement.
- Pas de champ `bean_module` mais `module` (varchar(25)) : longueur courte, peut tronquer les noms de modules longs.
- L'index sur `date_modified` permet un nettoyage des entrées périmées.
