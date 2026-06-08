# email_addressesMetaData.php

**Chemin :** `metadata/email_addressesMetaData.php`
**Type :** config (métadonnées de tables email — fichier riche multi-tables)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Définit la structure de **trois tables** liées à la gestion centralisée des adresses email dans SuiteCRM :
1. `email_addresses` — table centrale des adresses email (dédupliquée)
2. `emails_email_addr_rel` — normalisation des champs multi-adresses (To, CC, BCC)
3. `email_addr_bean_rel` — lien entre adresses email et n'importe quel bean SugarCRM

## Type

config

## Dépendances clés

- Variable globale `$dictionary` (framework SugarCRM).
- Protégé par la constante `sugarEntry`.
- Inclusion conditionnelle du cache : `cache/modules/EmailAddresses/EmailAddressvardefs.php` (ligne 159).

## Exports / Symboles principaux

### Table `email_addresses`

| Colonne | Type SQL | Rôle |
|---|---|---|
| `id` | id/varchar(36) | Clé primaire UUID (requis) |
| `email_address` | varchar(100) | Adresse email (requis) |
| `email_address_caps` | varchar(100) | Adresse en majuscules pour recherche insensible à la casse |
| `invalid_email` | bool | Email invalide (défaut : 0) |
| `opt_out` | bool | Opt-out marketing (défaut : 0, audité) |
| `confirm_opt_in` | enum | Statut opt-in (défaut : `not-opt-in`, audité) |
| `confirm_opt_in_date` | datetime | Date de confirmation opt-in |
| `confirm_opt_in_sent_date` | datetime | Date d'envoi de l'email de confirmation |
| `confirm_opt_in_fail_date` | datetime | Date d'échec de confirmation |
| `confirm_opt_in_token` | varchar(255) | Token de confirmation opt-in |
| `date_created` | datetime | Date de création |
| `date_modified` | datetime | Date de modification |
| `deleted` | bool | Soft delete |

Index clés : `idx_ea_caps_opt_out_invalid` sur `(email_address_caps, opt_out, invalid_email)`, `idx_ea_opt_out_invalid` sur `(email_address, opt_out, invalid_email)`.

### Table `emails_email_addr_rel`

Normalisation des destinataires d'un email (To, CC, BCC).

| Colonne | Type | Rôle |
|---|---|---|
| `id` | id | Clé primaire |
| `email_id` | id | FK vers `emails.id` |
| `address_type` | varchar(4) | Type : `to`, `cc`, `bcc` |
| `email_address_id` | id | FK vers `email_addresses.id` |
| `deleted` | bool | Soft delete |

### Table `email_addr_bean_rel`

Lien polymorphe entre adresses email et beans SugarCRM.

| Colonne | Type | Rôle |
|---|---|---|
| `id` | id | Clé primaire |
| `email_address_id` | id | FK vers `email_addresses.id` |
| `bean_id` | id | UUID du bean lié |
| `bean_module` | varchar(100) | Module du bean (polymorphe) |
| `primary_address` | bool | Adresse principale (défaut : 0) |
| `reply_to_address` | bool | Adresse de réponse (défaut : 0) |
| `date_created` / `date_modified` | datetime | Horodatages |
| `deleted` | bool | Soft delete |

## Interactions

- **Appelé par :** framework SugarCRM, module EmailAddresses, tous les modules ayant des champs email (Contacts, Leads, Accounts, etc.)
- **Appelle :** `cache/modules/EmailAddresses/EmailAddressvardefs.php` (si existant) via `include()`

## Notes

- `$dictionary['EmailAddress'] = $dictionary['email_addresses']` (ligne 162) : alias pour le module EmailAddress.
- Gestion RGPD via `opt_out`, `confirm_opt_in`, et les champs de date associés.
- `email_address_caps` (majuscules) : optimisation pour les recherches insensibles à la casse sans `UPPER()` en SQL.
- `email_addr_bean_rel` est polymorphe : un seul `bean_module` identifie le type de bean (pattern utilisé également dans `emails_beans`).
