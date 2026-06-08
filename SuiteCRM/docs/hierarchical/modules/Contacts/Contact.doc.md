# Contact.php

**Chemin :** `modules/Contacts/Contact.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle fonctionnel

Modèle principal du module Contacts. Représente une personne physique dans le CRM (client, prospect converti). Gère les données personnelles, la relation avec le compte, la synchronisation Outlook, et l'intégration avec les campagnes.

## Type

`model`

---

## Dépendances clés

| Import / Héritage | Rôle |
|---|---|
| `Person` (extend) | Template ORM SugarCRM pour les personnes |
| `EmailInterface` (implement) | Interface email SuiteCRM |
| `include/SugarObjects/templates/person/Person.php` | Inclusion explicite |
| `include/EmailInterface.php` | Inclusion interface |
| `BeanFactory::newBean('Campaigns')` | Récupération du nom de campagne dans detail fields |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `Contact` | classe | Bean principal de la table `contacts` |
| `create_new_list_query()` | méthode | Override : redirige vers popup adresse si action `ContactAddressPopup` |
| `address_popup_create_new_list_query()` | méthode | Requête SQL spécifique pour le popup d'adresse (jointures accounts, email) |
| `create_export_query()` | méthode | Requête d'export avec jointures accounts, users, email_addresses |
| `fill_in_additional_detail_fields()` | méthode | Hydrate account_name, report_to_name, campaign_name, portal_active |
| `load_contacts_users_relationship()` | méthode | Charge la relation user_sync (synchronisation Outlook) |
| `get_list_view_data()` | méthode | Override : injecte `SYNC_CONTACT` et `EMAIL_AND_NAME1` |
| `build_generic_where_clause()` | méthode | Recherche sur last_name, first_name, account name, email, téléphones |
| `save_relationship_changes()` | méthode | Override : déliaison de l'ancien compte si account_id change |
| `process_sync_to_outlook()` | méthode | Synchronise le contact avec les utilisateurs Outlook (import) |
| `get_contact_id_by_email()` | méthode | Retourne l'ID contact par email |
| `bean_implements()` | méthode | Déclare support ACL |

---

## Interactions

- **Appelé par :** `Save.php`, `ContactFormBase`, modules Campaigns (relation campaign_contacts), AcceptDecline.php
- **Appelle :** `accounts_contacts` (relation), `contacts_users` (relation user_sync)
- **Position dans le flux global :** Entité centrale CRM personne ; liée aux comptes, opportunités, campagnes, activités

---

## Points d'attention

- `fill_in_additional_detail_fields()` fait une requête SQL avec ORDER BY `a_c.date_modified DESC` pour privilégier le compte le plus récemment modifié en cas de multi-comptes (bug 43196/44730).
- `load_contacts_users_relationship()` inclut 3 vérifications de sécurité sur `$this->user_sync` avec log FATAL si problème — indique un historique de bugs sur cette relation.
- `process_sync_to_outlook('all')` itère sur TOUS les utilisateurs non supprimés — potentiellement très lourd.
- La suppression de l'ancien compte (`save_relationship_changes`) utilise `accounts->delete()` — déclenche un soft-delete de la relation.
