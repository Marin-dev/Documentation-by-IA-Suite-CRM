# Fichier : vardefs.php

**Chemin :** `modules/Accounts/vardefs.php`
**Type :** `PHP`
**Categorie :** configuration (definition du schema)
**Derniere mise a jour doc :** 2026-05-31

---

## Ce que ce fichier configure

Definit le schema complet du bean `Account` via `$dictionary['Account']`. Declare les champs supplementaires propres aux comptes (parent_id, sic_code, etc.), les champs de lien ORM vers les autres modules, les index SQL, les relations, et invoque `VardefManager::createVardef()` pour heriter des templates `default`, `assignable`, `security_groups`, `company`.

---

## Parametres cles

| Parametre | Type | Effet |
| --- | --- | --- |
| `table` | `accounts` | Nom de la table SQL |
| `audited` | `true` | Active l'audit des modifications |
| `unified_search` | `true` | Inclus dans la recherche globale |
| `full_text_search` | `true` | Indexation full-text activee |
| `duplicate_merge` | `true` | Fusion de doublons activee |
| `optimistic_locking` | `true` | Verrouillage optimiste pour les sauvegardes EditView |
| `parent_id` | id | Compte parent (auto-relation hierarchique) |
| `sic_code` | varchar(10) | Code SIC de la societe |
| `email_opt_out` | bool non-db | Opt-out email (derive de email_addr_bean_rel) |
| `invalid_email` | bool non-db | Email invalide (derive de email_addr_bean_rel) |

### Relations declarees

| Relation | Type | Module lie |
| --- | --- | --- |
| `member_accounts` | one-to-many (self) | Accounts (hierarchie parent/fils) |
| `account_cases` | one-to-many | Cases |
| `account_leads` | one-to-many | Leads |
| `account_aos_quotes` | one-to-many | AOS_Quotes |
| `account_aos_invoices` | one-to-many | AOS_Invoices |
| `account_aos_contracts` | one-to-many | AOS_Contracts |
| `account_campaign_log` | one-to-many | CampaignLog |

### Index SQL

| Nom | Champs |
| --- | --- |
| `idx_accnt_id_del` | `id`, `deleted` |
| `idx_accnt_name_del` | `name`, `deleted` |
| `idx_accnt_assigned_del` | `deleted`, `assigned_user_id` |
| `idx_accnt_parent_id` | `parent_id` |

## Impacte par / impacte

- Consomme par `VardefManager` au demarrage pour construire le schema ORM
- Utilise par `Account.php` via `$this->field_defs`
- Surcharge possible dans `custom/Extension/modules/Accounts/Ext/Vardefs/`

## Points d'attention

- `email_opt_out` et `invalid_email` sont `source = non-db` : valeurs derivees de `email_addr_bean_rel`, pas stockees dans `accounts`.
- Le champ `email` (type `email`) utilise une sous-requete pour la recherche dans la vue de liste.
- `campaign_id` est de type `id` (pas `relate`) : le nom de campagne est resolu dans `Account::fill_in_additional_detail_fields()`.
- `member_accounts` est une auto-relation (Accounts -> Accounts via `parent_id`) permettant la hierarchie de comptes.
