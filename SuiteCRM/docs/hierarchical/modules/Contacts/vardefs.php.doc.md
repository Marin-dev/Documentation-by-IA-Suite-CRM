# Fichier : vardefs.php (Contacts)

**Chemin :** `modules/Contacts/vardefs.php`
**Type :** PHP - Configuration (vardefs)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Definit le schema de la table `contacts` et toutes les relations ORM du module Contacts. Declare les champs specifiques, les index de performance, et les relations avec plus de 20 modules.

## Role technique

Script procedural peuplant `$dictionary['Contact']`. Active la recherche unifiee, la recherche plein texte, la fusion de doublons, et le verrouillage optimiste. Appelle `VardefManager::createVardef()` avec les mixins `default`, `assignable`, `security_groups`, `person`.

---

## Dependances cles

- `VardefManager::createVardef()` — injection des champs standards

## Exports / Symboles principaux

- `$dictionary['Contact']` — schema complet du module Contacts

## Champs notables

| Champ | Type | Role |
|---|---|---|
| `campaign_id` | id | Campagne d'origine du contact |
| `campaign_name` | relate | Nom de la campagne (non-db) |
| `sync_contact` | bool | Sync Outlook (non-db) |
| `portal_name`, `portal_active` | varchar/bool | Acces portail |
| `reports_to_id` | id | Hierarchie interne (contact superieur) |
| `joomla_account_id` | varchar | Integration Joomla |

## Relations definies

| Nom | Type | Modules |
|---|---|---|
| `accounts_contacts` | many-to-many | Contacts <-> Accounts |
| `opportunities_contacts` | many-to-many | Contacts <-> Opportunities |
| `contact_direct_reports` | one-to-many | self (hierarchie) |
| `contact_campaign_log` | one-to-many | Contacts -> CampaignLog |
| `contact_aos_quotes/invoices/contracts` | one-to-many | Contacts -> AOS modules |
| `contacts_aop_case_updates` | one-to-many | Contacts -> AOP_Case_Updates |

---

## Points d'attention

- `optimistic_locking = true` — gestion des conflits de sauvegarde simultanee activee.
- Le champ `sync_contact` est `source='non-db'` — stocke en session/relation, pas directement en base.
- La relation `campaign_contacts` pointe vers `Campaign` (one-to-many via `campaign_id` sur `contacts`).
