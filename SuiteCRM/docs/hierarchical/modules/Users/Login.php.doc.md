# Fichier : Login.php

**Chemin :** `modules/Users/Login.php`
**Type :** PHP — Vue (affichage formulaire de connexion)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche la page de connexion du CRM. Gere la langue d'affichage, les messages d'erreur, le nom d'utilisateur pre-rempli, le lien "mot de passe oublie", le reCAPTCHA, et le logo personnalisable. Choisit dynamiquement le template Smarty a utiliser (custom ou defaut).

## Role technique

Script procedural execute par le routeur (`action=Login`). Utilise `Sugar_Smarty` pour assigner les variables et afficher `login.tpl`. La priorite de template est : theme custom > modules/Users custom > theme courant > defaut `modules/Users/login.tpl`. Appelle `$authController->authController->pre_login()` en entree (hook pre-connexion).

---

## Dependances principales

| Dependance | Role |
|---|---|
| `$authController` | Hook pre-login |
| `Sugar_Smarty` | Moteur de templates |
| `SugarThemeRegistry` | Logo et theme courant |
| `recaptcha_utils.php` | Affichage CAPTCHA |
| `get_languages()` | Liste des langues disponibles |
| `$sugar_config` | Configuration (langue defaut, mot de passe oublie, etc.) |

## Exports / Symboles principaux

Aucun symbole exporte. Produit le HTML de la page de login.

Variables Smarty assignees : `LOGIN_IMAGE`, `LOGIN_ERROR_MESSAGE`, `LOGIN_VARS`, `LOGIN_USER_NAME`, `LOGIN_PASSWORD`, `LOGIN_ERROR`, `WAITING_ERROR`, `SELECT_LANGUAGE`, `CAPTCHA`, `DISPLAY_FORGOT_PASSWORD_FEATURE`.

---

## Relations cles

- **Appele par :** routeur CRM (`index.php?module=Users&action=Login`)
- **Suit :** `Logout.php` ou premiere visite
- **Precede :** `Authenticate.php` (soumission du formulaire)

---

## Points d'attention

- Presence d'un appel hex-encode (`"\x4c\x4f\x47\x49\x4e..."` = `LOGIN_LOGO_ERROR`) ligne 122 — code de validation de logo obscurci, probablement heritage SugarCRM.
- Le cookie `loginErrorMessage` est lu et efface immediatement (ligne 81-85).
- Le mot de passe depuis `$_SESSION['login_password']` ou `$sugar_config['default_password']` est assigne a Smarty — verifier que `default_password` n'est pas expose en production.
