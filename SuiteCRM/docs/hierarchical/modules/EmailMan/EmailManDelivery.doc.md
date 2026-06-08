# EmailManDelivery.php

**Chemin :** `modules/EmailMan/EmailManDelivery.php`
**Type :** PHP — script de livraison (entry point / scheduler)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Script de traitement de la file d'envoi email des campagnes. Selectionne les enregistrements `emailman` a envoyer, gere les listes de suppression (domaines/adresses), orchestre l'envoi via `EmailMan::sendEmail()` ou l'envoi opt-in via `EmailMan::sendOptInEmail()`. Redirige vers la vue d'origine a la fin.

**Type :** controller / script

---

## Dependances cles
- `SugarPHPMailer` (`include/SugarPHPMailer.php`)
- `EmailMan` (bean file)
- `BeanFactory` (Administration, EmailMarketing, EmailTemplates, OutboundEmailAccounts)
- `DBManagerFactory`
- `TimeDate`
- `Configurator`

---

## Variables d'environnement / config
| Parametre | Defaut | Effet |
|---|---|---|
| `massemailer_campaign_emails_per_run` | 500 | Nombre max d'emails par execution |
| `massemailer_email_copy` | 0 | Sauvegarder une copie individuelle par destinataire |
| `$_REQUEST['mode']` = `'test'` | — | Active le mode test (liste prospect type `test`) |
| `$_REQUEST['send_all']` | false | Continue jusqu'a vider la file |

---

## Interactions
- **Appele par :** scheduler SuiteCRM, ou manuellement via `EmailMan > index` (POST `manual`)
- **Appelle :** `EmailMan::sendEmail()`, `EmailMan::sendOptInEmail()`, `OutboundEmailAccounts`

---

## Notes
- La boucle `do...while` avec `$send_all` peut epuiser la memoire ou le temps d'execution PHP si la file est grande et que `send_all = true`.
- Configuration du compte SMTP sortant prioritaire via `OutboundEmailAccounts` si `$current_emailmarketing->outbound_email_id` est defini.
- `DBManager::setQueryLimit(0)` desactive la limite de requetes (ligne 130) — risque de performances.
