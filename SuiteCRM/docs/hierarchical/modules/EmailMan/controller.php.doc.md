# controller.php

**Chemin :** `modules/EmailMan/controller.php`
**Type :** controller
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Contrôleur MVC du module EmailMan. Gère l'action `Save` de la configuration de l'envoi email de masse (Mass Emailer). Réservé aux administrateurs.

## Type
controller

---

## Dépendances clés
- `SugarController` (classe parente)
- `OutboundEmail` (`include/OutboundEmail/OutboundEmail.php`)
- `Configurator` (`modules/Configurator/Configurator.php`)
- `BeanFactory` — instanciation Administration

## Exports / Symboles principaux
- `EmailManController` — classe — contrôleur du module EmailMan
- `action_Save()` — méthode — sauvegarde la configuration Mass Emailer (SMTP, tracking, etc.)

## Interactions
- **Appelé par :** framework SugarCRM (dispatcher MVC)
- **Appelle :** Administration bean, Configurator

## Notes
- Accès restreint aux admins globaux ou admins des modules Emails/Campaigns.
- Force `mail_sendtype = SMTP` si `allow_sendmail_outbound` n'est pas activé dans la config.
