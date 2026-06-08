# Fichier : Authenticate.php

**Chemin :** `modules/Users/Authenticate.php`
**Type :** PHP — Script d'action (authentification)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Point d'entree de l'authentification utilisateur. Reçoit les identifiants soumis depuis le formulaire de connexion, delegue la verification a `$authController->login()`, puis redirige vers la page appropriee (accueil, changement de mot de passe expire, ou retour au formulaire de login en cas d'echec).

## Role technique

Script procedural execute par le routeur CRM (`action=Authenticate`). Utilise la variable globale `$authController` pour appeler la methode `login($user_name, $password)`. Verifie ensuite `$_SESSION['authenticated_user_id']` pour determiner le succes. En cas de mot de passe expire, redirige vers `ChangePassword`. En cas de succes, determine la page d'accueil selon `$sugar_config['default_module']` ou la liste des modules accessibles. Regenere l'ID de session avant le traitement (protection CSRF, ligne 46).

---

## Dependances principales

| Dependance | Role |
|---|---|
| `$authController` (global) | Controleur d'authentification injecte par le bootstrap |
| `$GLOBALS['app']->getLoginVars()` | Variables de redirection post-login |
| `query_module_access_list()` | Liste des modules accessibles a l'utilisateur |
| `$GLOBALS['sugar_config']` | Configuration site (default_module, default_action) |

## Exports / Symboles principaux

Aucun symbole exporte. Script d'action pur produisant une redirection HTTP.

---

## Relations cles

- **Appele par :** routeur CRM (`index.php?module=Users&action=Authenticate`)
- **Appelle :** `$authController->login()`, `sugar_cleanup()`, `header()` (redirection)
- **Suit :** `Login.php` (affichage formulaire)
- **Precede :** vue Home ou `ChangePassword`

---

## Points d'attention

- `session_regenerate_id(false)` est appele en debut de script sauf dans les tests PHPUnit (`SUITE_PHPUNIT_RUNNER`), ce qui empeche la fixation de session.
- La detection du mot de passe expire se base sur `$_SESSION['hasExpiredPassword'] == '1'` (ligne 61).
- Si aucun module accessible n'est trouve, `$url` peut rester non definie — risque potentiel de redirection nulle.
