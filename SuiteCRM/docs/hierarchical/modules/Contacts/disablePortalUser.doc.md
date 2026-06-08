# disablePortalUser.php

**Chemin :** `modules/Contacts/disablePortalUser.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Script de désactivation d'un compte portal Joomla lié à un contact SuiteCRM. Appelle l'API du portail AOP (Advanced Open Portal) via HTTP pour désactiver l'accès, puis met à jour `portal_account_disabled = 1` sur le bean Contact.

**Type :** action (script d'action admin/portail)

---

## Dépendances clés

- `modules/AOP_Case_Updates/util.php` — `isAOPEnabled()`
- `modules/Contacts/Contact.php`
- `BeanFactory::newBean('Contacts')`
- `$sugar_config['aop']['joomla_url']` — URL du portail Joomla
- `$_REQUEST['record']` — ID du contact
- `$bean->joomla_account_id` — ID du compte Joomla correspondant

---

## Exports / Symboles principaux

Aucune classe exportée — script procédural.

---

## Interactions

**Appelle :**
- `file_get_contents($portalURL . '/index.php?option=com_advancedopenportal&task=disable_user&...')` — API Joomla
- `$bean->save(false)` — mise à jour `portal_account_disabled`
- `SugarApplication::appendErrorMessage()` — feedback utilisateur

**Appelée par :** Bouton "Désactiver utilisateur portail" dans la vue détail d'un Contact.

**Position dans le flux global :** Gestion du cycle de vie des comptes portail ; symétrique avec `enablePortalUser.php`.

---

## Notes

- Ne fonctionne que si AOP est activé et que `$sugar_config['aop']['joomla_url']` est configuré.
- Si le portail Joomla retourne `success=false`, le message d'erreur de la réponse est affiché.
- Définit `sugarEntry = true` manuellement (ligne 29) — peut être appelé hors contexte HTTP standard.
