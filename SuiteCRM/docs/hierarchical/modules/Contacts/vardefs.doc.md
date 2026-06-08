# vardefs.php

**Chemin :** `modules/Contacts/vardefs.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Définit le schéma de données (vardefs) de l'entité Contact : champs, index, relations avec les autres modules CRM. Hérite des templates `default`, `assignable`, `security_groups`, `person`.

## Type

`config`

---

## Dépendances clés

| Import / Dépendance | Rôle |
|---|---|
| `VardefManager::createVardef()` | Applique les templates person, default, assignable, security_groups |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `$dictionary['Contact']` | tableau | Schéma complet : table `contacts`, champs, index, relations |

### Champs clés

| Champ | Type | Notes |
|---|---|---|
| `account_name` / `account_id` | relate/id | Lien vers le compte principal |
| `lead_source` | enum | `lead_source_dom` |
| `birthdate` | date | Date de naissance |
| `reports_to_id` | id | Lien vers le contact supérieur hiérarchique |
| `campaign_id` / `campaign_name` | id/relate | Campagne d'origine |
| `sync_contact` | bool (non-db) | Synchronisation Outlook |
| `portal_name`, `portal_active`, `portal_user_type` | divers | Accès portail Joomla/AOP |
| `joomla_account_id` | varchar | ID compte Joomla |

### Relations déclarées

| Relation | Modules liés | Type |
|---|---|---|
| `accounts_contacts` | Contact → Account | many-to-one |
| `opportunities_contacts` | Contact ↔ Opportunity | many-to-many |
| `contact_direct_reports` | Contact → Contact (hiérarchie) | one-to-many |
| `contact_leads` | Contact → Lead | one-to-many |
| `contact_campaign_log` | Contact → CampaignLog | one-to-many |
| `contact_aos_quotes/invoices/contracts` | Contact → AOS modules | one-to-many |
| `contacts_aop_case_updates` | Contact → AOP_Case_Updates | one-to-many |
| `fp_events_contacts` | Contact ↔ FP_Events | many-to-many |
| `contacts_users` (user_sync) | Contact ↔ Users | many-to-many |

---

## Interactions

- **Consommé par :** `Contact.php` (bean), framework ORM, Studio, module import
- **Impacte :** Schéma de la table `contacts`

---

## Points d'attention

- Verrouillage optimiste activé (`optimistic_locking: true`).
- Les champs portail (`portal_*`, `joomla_*`) reflètent une intégration avec Joomla/AOP — dépendante de la configuration.
- Le champ `sync_contact` est non-db — calculé à la volée via la relation `contacts_users`.
