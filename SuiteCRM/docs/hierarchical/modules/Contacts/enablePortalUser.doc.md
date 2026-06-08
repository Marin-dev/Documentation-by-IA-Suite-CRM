# enablePortalUser.php

**Chemin :** `modules/Contacts/enablePortalUser.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Script de réactivation d'un compte portal Joomla lié à un contact SuiteCRM. Symétrique de `disablePortalUser.php`. Appelle l'API AOP pour réactiver l'accès et met à jour `portal_account_disabled = 0` sur le bean Contact.

**Type :** action (script d'action admin/portail)

---

## Dépendances clés

- `modules/AOP_Case_Updates/util.php` — `isAOPEnabled()`
- `modules/Contacts/Contact.php`
- `BeanFactory::newBean('Contacts')`
- `$sugar_config['aop']['joomla_url']` — URL du portail Joomla
- `$_REQUEST['record']` — ID du contact
- `$bean->joomla_account_id` — ID du compte Joomla

---

## Exports / Symboles principaux

Aucune classe exportée — script procédural.

---

## Interactions

**Appelle :**
- `file_get_contents($portalURL . '/index.php?option=com_advancedopenportal&task=enable_user&...')` — API Joomla
- `$bean->save(false)` — mise à jour `portal_account_disabled = 0`
- `SugarApplication::appendErrorMessage()` — feedback utilisateur
- `SugarApplication::redirect()` — retour vers la vue détail

**Appelée par :** Bouton "Activer utilisateur portail" dans la vue détail d'un Contact.

**Position dans le flux global :** Réactivation d'un compte portail désactivé ; symétrique avec `disablePortalUser.php`.

---

## Notes

- Mêmes prérequis que `disablePortalUser.php` : AOP activé + `joomla_url` configuré.
- La tâche Joomla appelée est `enable_user` (vs `disable_user` pour la désactivation).
