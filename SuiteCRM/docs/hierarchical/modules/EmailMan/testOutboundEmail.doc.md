# testOutboundEmail.php (EmailMan)

**Chemin :** `modules/EmailMan/testOutboundEmail.php`
**Type :** PHP — entry point AJAX
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Script AJAX de test de la connexion SMTP sortante. Accepte les parametres SMTP en POST (`mail_smtpserver`, `mail_smtpport`, `mail_smtpssl`, etc.), recupere le mot de passe depuis `OutboundEmailAccounts` si absent, et appelle `Email::sendEmailTest()`. Retourne un JSON.

**Type :** helper / entry point

---

## Dependances cles
- `Email` (`modules/Emails/Email.php`)
- `OutboundEmail`
- `BeanFactory::getBean('OutboundEmailAccounts')`
- `$sugar_config['outbound_email_test_max_timeout']` (defaut 30s)

---

## Notes
- Modifie `max_execution_time` dynamiquement (ligne 62).
- Appelle `getJSONobj()` pour encoder la reponse.
