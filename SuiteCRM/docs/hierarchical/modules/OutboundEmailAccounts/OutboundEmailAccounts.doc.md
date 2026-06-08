# OutboundEmailAccounts.php

**Chemin :** `modules/OutboundEmailAccounts/OutboundEmailAccounts.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Bean des comptes SMTP sortants. Permet de configurer plusieurs serveurs SMTP (systeme, campagne, personnel) avec authentification basique, sans authentification ou OAuth. Gere le chiffrement Blowfish du mot de passe SMTP a la sauvegarde.

**Type :** model

---

## Dependances cles
- `OutboundEmailAccounts_sugar` (classe parente generee)
- `Basic` (grand-parent SugarCRM)
- `BeanFactory::newBean('OutboundEmailAccounts')` (pour recuperer l'ancien mot de passe)
- `blowfishEncode()` / `blowfishGetKey('OutBoundEmail')` (chiffrement)

---

## Exports / Symboles principaux
| Symbole | Type | Role |
|---|---|---|
| `OutboundEmailAccounts` | classe | Bean compte SMTP sortant |
| `save()` | methode | Sauvegarde avec chiffrement mdp, gestion auth_type |
| `$auth_type` | propriete | Type d'authentification : `no_auth`, `basic`, `oauth` |
| `$mail_smtppass` | propriete | Mot de passe SMTP (chiffre en base) |
| `$external_oauth_connection_id` | propriete | ID connexion OAuth externe |

---

## Interactions
- **Appele par :** `EmailManDelivery.php`, `EmailMan::sendEmail()`, `testOutboundEmail.php`, controller
- **Appelle :** `blowfishEncode()`, `BeanFactory`

---

## Notes
- Le mot de passe est rechiffre a chaque sauvegarde. Si le champ est vide et qu'un ID existe, l'ancien mot de passe est recupere depuis la DB pour eviter de l'effacer.
- `hasAccessToPersonalAccount()` : controle d'acces aux comptes personnels (vs systeme).
