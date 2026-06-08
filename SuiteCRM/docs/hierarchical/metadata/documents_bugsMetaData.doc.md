# documents_bugsMetaData.php

**Chemin :** `metadata/documents_bugsMetaData.php`
**Type :** config (metadonnees de table de jointure)
**Derniere mise a jour doc :** 2026-05-31

---

## Role

Definit la structure de la table de jointure `documents_bugs` qui materialise la relation many-to-many entre les documents (`Documents`) et les bogues (`Bugs`). Permet d'attacher des documents a des tickets de bugs.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary["documents_bugs"]` | variable globale PHP | Definition de la table de jointure et de la relation |

### Structure de la table `documents_bugs`

| Colonne | Type SQL | Role |
|---|---|---|
| `id` | varchar(36) | Cle primaire UUID |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (defaut : 0, requis) |
| `document_id` | varchar(36) | FK vers `documents.id` |
| `bug_id` | varchar(36) | FK vers `bugs.id` |

### Index

| Nom | Type | Champs |
|---|---|---|
| `documents_bugsspk` | primary | `id` |
| `documents_bugs_bug_id` | alternate_key | `bug_id`, `document_id` |
| `documents_bugs_document_id` | alternate_key | `document_id`, `bug_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `Documents`, table `documents`, cle `id`
- **RHS :** module `Bugs`, table `bugs`, cle `id`
- **Table de jointure :** `documents_bugs`

## Interactions

- **Appele par :** framework SugarCRM (dictionnaire de schema, module Documents, module Bugs)
- **Appelle :** rien

## Notes

- Deux index `alternate_key` dans les deux sens pour optimiser les requetes (recherche par document ou par bug).
- Genere via Studio (`from_studio` absent, fichier core).
