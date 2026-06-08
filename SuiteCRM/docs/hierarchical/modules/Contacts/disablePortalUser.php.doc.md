# Fichier : disablePortalUser.php

**Chemin :** `modules/Contacts/disablePortalUser.php`
**Type :** PHP - Script d'action (portail)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Desactive le compte utilisateur portail Joomla/AOP associe a un contact. Appelle l'API Joomla pour desactiver l'utilisateur et met a jour le champ `portal_account_disabled = 1` sur le bean Contact.

## Role technique

Script procedural. Identique structurellement a `createPortalUser.php`. Appelle `task=disable_user` sur le portail avec l'ID Joomla du contact (`joomla_account_id`).

---

## Dependances cles

- `modules/AOP_Case_Updates/util.php` — `isAOPEnabled()`
- `$sugar_config['aop']['joomla_url']` — URL du portail
- `BeanFactory::newBean('Contacts')` — bean Contact

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Action "Desactiver l'utilisateur portail" dans la vue detail d'un contact

## Relations cles

- **Tables DB modifiees :** `contacts.portal_account_disabled = 1`
- **Appelle :** API Joomla `task=disable_user`

---

## Points d'attention

- Dependant de `joomla_account_id` sur le bean — doit etre defini avant appel.
- Utilise `file_get_contents()` — appel HTTP synchrone.
