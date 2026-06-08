# documents_accountsMetaData.php

**Chemin :** `metadata/documents_accountsMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `documents_accounts` qui matérialise la relation many-to-many entre les documents (`Documents`) et les comptes (`Accounts`). Permet d'attacher des documents à des comptes.

## Type

config

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['documents_accounts']` | variable globale PHP | Définition de la table de jointure |

### Structure de la table `documents_accounts`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0, requis) |
| `document_id` | varchar(36) | FK vers `documents.id` |
| `account_id` | varchar(36) | FK vers `accounts.id` |

### Index

| Nom | Type | Champs |
|---|---|---|
| `documents_accountsspk` | primary | `id` |
| `documents_accounts_account_id` | alternate_key | `account_id`, `document_id` |
| `documents_accounts_document_id` | alternate_key | `document_id`, `account_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `Documents`, table `documents`, clé `id`
- **RHS :** module `Accounts`, table `accounts`, clé `id`

## Interactions

- **Appelé par :** framework SugarCRM, module Documents
- **Appelle :** rien

## Notes

- Particularité : deux index `alternate_key` dans les deux sens (account_id+document_id et document_id+account_id) pour optimiser les requêtes dans les deux directions.
