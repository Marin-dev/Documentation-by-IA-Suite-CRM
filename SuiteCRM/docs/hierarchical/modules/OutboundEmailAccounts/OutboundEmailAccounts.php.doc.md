# OutboundEmailAccounts.php

**Chemin :** `modules/OutboundEmailAccounts/OutboundEmailAccounts.php`
**Type :** model

**Dernière mise à jour doc :** 2026-06-02

---

## Rôle

Modèle des comptes email sortants. Stocke la configuration SMTP (serveur, port, authentification, chiffrement) utilisée pour envoyer des emails depuis SuiteCRM. Supporte plusieurs types d'authentification : `no_auth`, `basic` (login/mot de passe), `oauth` (OAuth2 externe).

## Type

model

---

## Dépendances clés

- `OutboundEmailAccounts_sugar` (classe parente — générée)
- `BeanFactory` — récupération du bean pour préserver le mot de passe chiffré
- `Administration` (BeanFactory) — sauvegarde `notify/fromname` et `notify/fromaddress` si compte système
- `blowfishEncode()` / `blowfishGetKey()` — chiffrement du mot de passe SMTP

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `OutboundEmailAccounts` | classe | Entité compte SMTP sortant (table `outbound_email`) |
| `save()` | méthode | Sauvegarde avec chiffrement du mot de passe et mise à jour admin si système |
| `$auth_type` | propriété | Type d'auth : `no_auth`, `basic`, `oauth` |
| `$external_oauth_connection_id` | propriété | ID connexion OAuth externe |
| `hasAccessToPersonalAccount()` | méthode | Vérifie les droits d'accès au compte personnel |

## Interactions

- **Appelé par :** `EmailManDelivery.php` (configuration SMTP par campagne), `testOutboundEmail.php`, vues OutboundEmailAccounts
- **Appelle :** Administration (sauvegarde fromname/fromaddress)

## Notes

- `disable_row_level_security = true` (hérité de `OutboundEmailAccounts_sugar`).
- Le mot de passe SMTP est toujours chiffré en base (Blowfish). Ne jamais stocker en clair.
- Si `auth_type = no_auth`, le mot de passe est forcé à vide et `mail_smtpauth_req = 0`.
- Si `type = system`, synchronise les paramètres avec le module Administration.
