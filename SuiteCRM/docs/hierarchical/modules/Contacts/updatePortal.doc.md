# updatePortal.php

**Chemin :** `modules/Contacts/updatePortal.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle

Classe de notification par email lors de la création ou mise à jour d'un compte portail AOP pour un contact. Envoie un email au contact avec ses identifiants d'accès au portail Joomla (mot de passe et URL). Utilisée comme logic hook `after_save` sur le bean Contact.

**Type :** helper / logic hook

---

## Dépendances clés

- `modules/AOP_Case_Updates/util.php` — `isAOPEnabled()`, `aop_parse_template()`, `getPortalEmailSettings()`
- `BeanFactory::getBean('EmailTemplates', ...)` — template email AOP
- `$sugar_config['aop']['joomla_account_creation_email_template_id']` — ID du template
- `$sugar_config['aop']['joomla_url']` — URL du portail
- `SugarPHPMailer` — envoi email
- `BeanFactory::newBean('Emails')` — archivage de l'email envoyé
- `$bean->joomla_account_access` — mot de passe Joomla généré
- `$bean->email1` — adresse email du contact destinataire

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `updatePortal` | classe | Envoi de notification email portail |
| `updateUser($bean)` | méthode publique | Vérifie si `joomla_account_access` est défini et envoie l'email de bienvenue |
| `sendEmail($emailTo, $subject, $body, $altBody, $relatedBean)` | méthode publique | Envoie l'email via `SugarPHPMailer` et archive dans `Emails` |

---

## Interactions

**Appelle :**
- `BeanFactory::getBean('EmailTemplates')` pour le template
- `aop_parse_template()` pour le rendu du template avec variables
- `new SugarPHPMailer()` et `$mail->send()` pour l'envoi

**Appelée par :** Logic hook `after_save` sur le bean `Contact` (configuration dans `logic_hooks.php` — INCONNU si présent dans ce module ou en `custom/`).

**Position dans le flux global :** Notification automatique après création de compte portail pour un contact.

---

## Notes

- Les variables `$joomla_pass` et `$portal_address` sont remplacées dans le template (lignes 65-66).
- Si l'envoi échoue (`@$mail->send()` retourne false), l'email n'est pas archivé — silencieux.
- L'archivage de l'email est créé avec `modified_user_id = '1'` et `created_by = '1'` (admin).
