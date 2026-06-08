# documents_contactsMetaData.php

**Chemin :** `metadata/documents_contactsMetaData.php`
**Type :** config (metadonnees de table de jointure)
**Derniere mise a jour doc :** 2026-05-31

---

## Role

Definit la structure de la table de jointure `documents_contacts` qui materialise la relation many-to-many entre les documents (`Documents`) et les contacts (`Contacts`). Permet d'associer des documents a des contacts CRM.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary["documents_contacts"]` | variable globale PHP | Definition de la table de jointure et de la relation |

### Structure de la table `documents_contacts`

| Colonne | Type SQL | Role |
|---|---|---|
| `id` | varchar(36) | Cle primaire UUID |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (defaut : 0, requis) |
| `document_id` | varchar(36) | FK vers `documents.id` |
| `contact_id` | varchar(36) | FK vers `contacts.id` |

### Index

| Nom | Type | Champs |
|---|---|---|
| `documents_contactsspk` | primary | `id` |
| `documents_contacts_contact_id` | alternate_key | `contact_id`, `document_id` |
| `documents_contacts_document_id` | alternate_key | `document_id`, `contact_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `Documents`, table `documents`, cle `id`
- **RHS :** module `Contacts`, table `contacts`, cle `id`
- **Table de jointure :** `documents_contacts`

## Interactions

- **Appele par :** framework SugarCRM (dictionnaire de schema, module Documents, module Contacts)
- **Appelle :** rien

## Notes

- Deux index `alternate_key` bidirectionnels pour optimiser les requetes.
