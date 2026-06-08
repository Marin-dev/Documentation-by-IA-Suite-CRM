# accounts_contactsMetaData.php

**Chemin :** `metadata/accounts_contactsMetaData.php`
**Type :** config (métadonnées de table de jointure)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de la table de jointure `accounts_contacts` qui matérialise la relation many-to-many entre les comptes (`Accounts`) et les contacts (`Contacts`). Relation centrale du CRM : un contact peut appartenir à plusieurs comptes et vice-versa.

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Protégé par la constante `sugarEntry`.

## Exports / Symboles principaux

| Symbole | Type | Description |
|---|---|---|
| `$dictionary['accounts_contacts']` | variable globale PHP | Définition de la table de jointure et de la relation |

### Structure de la table `accounts_contacts`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | varchar(36) | Clé primaire UUID |
| `contact_id` | varchar(36) | FK vers `contacts.id` |
| `account_id` | varchar(36) | FK vers `accounts.id` |
| `date_modified` | datetime | Horodatage de modification |
| `deleted` | bool(1) | Soft delete (défaut : 0) |

### Index

| Nom | Type | Champs |
|---|---|---|
| `accounts_contactspk` | primary | `id` |
| `idx_account_contact` | alternate_key | `account_id`, `contact_id` |
| `idx_contid_del_accid` | index | `contact_id`, `deleted`, `account_id` |

### Relation

- **Type :** many-to-many
- **LHS :** module `Accounts`, table `accounts`, clé `id`
- **RHS :** module `Contacts`, table `contacts`, clé `id`
- **Table de jointure :** `accounts_contacts`

## Interactions

- **Appelé par :** framework SugarCRM (dictionnaire de schéma)
- **Appelle :** rien

## Notes

- L'index composite `(contact_id, deleted, account_id)` optimise les requêtes filtrant sur le contact avec exclusion des enregistrements supprimés.
- Relation très fréquemment utilisée dans le CRM (liste des contacts d'un compte, liste des comptes d'un contact).
