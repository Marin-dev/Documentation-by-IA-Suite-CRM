# testOutboundEmail.php

**Chemin :** `modules/EmailMan/testOutboundEmail.php`
**Type :** helper (script de test)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Script de test de la configuration email sortante. Envoie un email de test via SMTP depuis l'interface admin. Récupère le mot de passe SMTP depuis `OutboundEmailAccounts` ou `OutboundEmail` selon le contexte.

## Type
helper (script procédural)

---

## Dépendances clés
- `modules/Emails/Email.php`
- `OutboundEmail` (`include/OutboundEmail/OutboundEmail.php`)
- `BeanFactory` — lecture OutboundEmailAccounts
- `$sugar_config['outbound_email_test_max_timeout']` — timeout configurable (défaut 30s)

## Exports / Symboles principaux
- Aucun — script procédural, retourne JSON

## Interactions
- **Appelé par :** interface admin EmailMan (action test SMTP)
- **Appelle :** `OutboundEmail::getSystemMailerSettings()`, `OutboundEmail::getMailerByName()`

## Notes
- Limite d'exécution forcée via `ini_set('max_execution_time', $testMaxTimeout)`.
