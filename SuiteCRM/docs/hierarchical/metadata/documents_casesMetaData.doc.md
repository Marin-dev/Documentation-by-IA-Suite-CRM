# documents_casesMetaData.php

**Chemin :** `metadata/documents_casesMetaData.php`
**Type :** config (metadonnees de table de jointure)
**Derniere mise a jour doc :** 2026-05-31

---

## Role

Definit la structure de la table de jointure `documents_cases` qui materialise la relation many-to-many entre les documents (`Documents`) et les cas support (`Cases`). Permet d'attacher des documents a des dossiers de support client.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary["documents_cases"]` | variable globale PHP | Definition de la table de jointure et de la relation |

### Structure de la table `documents_cases`

| Colonne | Type SQL | Role |
|---|---|---|
| `id` | varchar(36) | Cle primaire UUID |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (defaut : 0, requis) |
| `document_id` | varchar(36) | FK vers `documents.id` |
| `case_id` | varchar(36) | FK vers `cases.id` |

### Index

| Nom | Type | Champs |
|---|---|---|
| `documents_casesspk` | primary | `id` |
| `documents_cases_case_id` | alternate_key | `case_id`, `document_id` |
| `documents_cases_document_id` | alternate_key | `document_id`, `case_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `Documents`, table `documents`, cle `id`
- **RHS :** module `Cases`, table `cases`, cle `id`
- **Table de jointure :** `documents_cases`

## Interactions

- **Appele par :** framework SugarCRM (dictionnaire de schema, module Documents, module Cases)
- **Appelle :** rien

## Notes

- Deux index `alternate_key` dans les deux sens pour optimiser les requetes (recherche par document ou par cas).
