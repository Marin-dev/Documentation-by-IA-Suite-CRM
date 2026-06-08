# Fichier : enablePortalUser.php

**Chemin :** `modules/Contacts/enablePortalUser.php`
**Type :** PHP - Script d'action (portail)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Reactive le compte utilisateur portail Joomla/AOP d'un contact prealablement desactive. Met a jour `portal_account_disabled = 0` sur le bean Contact.

## Role technique

Script procedural. Identique a `disablePortalUser.php` mais appelle `task=enable_user`. Met `portal_account_disabled = 0` apres succes.

---

## Dependances cles

- `modules/AOP_Case_Updates/util.php` — `isAOPEnabled()`
- `$sugar_config['aop']['joomla_url']`
- `BeanFactory::newBean('Contacts')`

## Exports / Symboles principaux

Aucune classe exportee. Script procedural.

## Consommateurs identifies

- Action "Activer l'utilisateur portail" dans la vue detail d'un contact

## Relations cles

- **Tables DB modifiees :** `contacts.portal_account_disabled = 0`
- **Appelle :** API Joomla `task=enable_user`

---

## Points d'attention

- Triptyque avec `createPortalUser.php` et `disablePortalUser.php` — memes patterns, memes risques.
