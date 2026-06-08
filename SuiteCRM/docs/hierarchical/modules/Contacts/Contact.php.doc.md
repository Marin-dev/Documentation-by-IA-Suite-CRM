# Fichier : Contact.php

**Chemin :** `modules/Contacts/Contact.php`
**Type :** PHP - Modele (Person/SugarBean)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Modele central du module Contacts. Represente une personne physique dans le CRM (client, prospect, interlocuteur). Gere ses relations avec les comptes, opportunites, campagnes, appels, reunions, bugs, et la synchronisation Outlook.

## Role technique

Etend `Person` (via `include/SugarObjects/templates/person/Person.php`) et implemente `EmailInterface`. Mappe la table `contacts`. Override plusieurs methodes (`create_new_list_query`, `fill_in_additional_detail_fields`, `save_relationship_changes`, etc.) pour gerer les specificites du module.

---

## Dependances cles

- **Extends :** `Person` (`include/SugarObjects/templates/person/Person.php`)
- **Implements :** `EmailInterface` (`include/EmailInterface.php`)
- **BeanFactory :** `Campaigns`, `Users` (utilises dans `fill_in_additional_detail_fields`)
- **ACLController** — controle d'acces sur la vue liste
- **Tables liees :** `contacts`, `accounts_contacts`, `opportunities_contacts`

## Exports / Symboles principaux

- `Contact` — classe — modele principal du module Contacts
  - `fill_in_additional_detail_fields()` — charge compte, "reports to", campagne associee, sync Outlook (l.410)
  - `fill_in_additional_list_fields()` — construit le nom complet et les champs email (l.397)
  - `create_new_list_query(...)` — redirige vers popup d'adresse si `action=ContactAddressPopup` (l.218)
  - `address_popup_create_new_list_query(...)` — requete specialisee pour le popup d'adresse (l.267)
  - `create_export_query(...)` — requete d'export avec jointures accounts/emails (l.355)
  - `load_contacts_users_relationship()` — charge la relation de sync Outlook (l.492)
  - `save_relationship_changes(...)` — delie l'ancien compte si `account_id` change (l.593)
  - `process_sync_to_outlook($list_of_users)` — lie le contact aux utilisateurs Outlook (l.631)
  - `get_contact_id_by_email($email)` — retrouve un contact par email (l.576)
  - `bean_implements('ACL')` — retourne true (l.607)

## Consommateurs identifies

- `modules/Contacts/Save.php` (via `ContactFormBase`)
- `modules/Contacts/ContactFormBase.php`
- `modules/Contacts/AcceptDecline.php`
- `modules/Campaigns/Campaign.php` (relation `campaign_contacts`)

## Relations cles

- **Relations ORM :** `accounts`, `opportunities`, `calls`, `meetings`, `tasks`, `notes`, `emails`, `bugs`, `cases`, `documents`, `leads`, `user_sync`, `campaign_contacts`, `prospect_lists`, `fp_events_contacts`, `aos_quotes`, `aos_invoices`, `aos_contracts`
- **Sync Outlook :** via relation `contacts_users`

---

## Points d'attention

- `create_new_list_query` detecte `action=ContactAddressPopup` via `$_REQUEST` — couplage avec la couche HTTP.
- `fill_in_additional_detail_fields` effectue une requete SQL directe pour charger le compte et le "reports to" (l.420-436) — risque N+1 si appele en boucle.
- `process_sync_to_outlook` avec `'all'` synchronise avec TOUS les utilisateurs non supprimes — usage avec precaution.
- `save_relationship_changes` supprime l'ancienne relation avec le compte si `account_id` est modifie (l.598-603).
