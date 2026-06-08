# PasswordManager.php

**Chemin :** `modules/Administration/PasswordManager.php`
**Type :** PHP (view / page parametres)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Page d'administration de la securite des mots de passe et de l'authentification. Configure : generation automatique de mots de passe, templates d'email (reinitialisation, generation, double-facteur), regles de complexite (majuscule, minuscule, chiffre, caractere special, longueur min), expiration, verrouillage de compte, LDAP, SAML (non finalise), et reCAPTCHA.

## Role technique
Script procedral. En POST avec `saveConfig`, valide la cle publique reCAPTCHA via HTTP (Google API), gere LDAP (enable/disable + parametres groupe), sauvegarde les regles de complexite via `$configurator->config['passwordsetting']`, puis appelle `$configurator->saveConfig()` et `$focus->saveConfig()`. Affiche le template `PasswordManager.tpl` via Smarty.

---

## Dependances cles
| Element | Role |
|---|---|
| `modules/Configurator/Configurator.php` | Persistance passwordsetting et ldap dans config_override |
| `BeanFactory::newBean('Administration')` | Lecture/ecriture parametres config table |
| `BeanFactory::newBean('InboundEmail')` | Verification IMAP + options email |
| `include/Imap/ImapHandlerFactory.php` | Verification disponibilite IMAP |
| `include/SugarPHPMailer.php` | Verification configuration SMTP |
| `get_bean_select_array()` | Liste des templates email disponibles |
| `modules/Administration/Forms.php` | Helper JS (include) |

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `clearPasswordSettings()` | Fonction | Reinitialise les settings mot de passe dans $_POST quand LDAP est active |

## Interactions
- **Appele par :** `index.php?module=Administration&action=PasswordManager`
- **Appelle :** `Configurator::saveConfig()`, `Administration::saveConfig()`, `SugarPHPMailer::setMailerForSystem()`
- **Template :** `modules/Administration/PasswordManager.tpl`

---

## Notes
- Validation reCAPTCHA via `fopen()` HTTP sur `google.com` (ligne 83) — peut echouer si l'acces HTTP sortant est bloque.
- Si LDAP est active, les parametres de mot de passe standard sont vides (`clearPasswordSettings()`) — logique exclusive.
- `$sugar_smarty->assign('saml_enabled_checked', false)` (ligne 168) : SAML est present mais non configure ici.
- Si openssl absent, le champ de cle de chiffrement LDAP est mis en lecture seule (ligne 171).
