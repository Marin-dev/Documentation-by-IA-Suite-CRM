# Fichier : ChangePassword.php

**Chemin :** `modules/Users/ChangePassword.php`
**Type :** PHP — Vue/Action (changement de mot de passe force)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Affiche et traite le formulaire de changement de mot de passe lorsque celui-ci a expire (mot de passe systeme genere ou expiration par politique). Apres validation, redirige vers le wizard de premier demarrage ou la page d'accueil.

## Role technique

Script dual : si `$_POST['saveConfig']` est present, recupere le bean User, appelle `$focus->change_password($old, $new)`, et redirige. Sinon, construit la vue Smarty avec les parametres de politique de mot de passe (`$sugar_config['passwordsetting']`), assigne le formulaire et affiche `Changenewpassword.tpl`.

---

## Dependances principales

| Import | Role |
|---|---|
| `modules/Users/User.php` | Bean utilisateur |
| `SuiteValidator` | Validation de l'ID record |
| `modules/Administration/Forms.php` | Helpers formulaires |
| `modules/Configurator/Configurator.php` | Acces configuration globale |
| `Sugar_Smarty` | Rendu template |

## Exports / Symboles principaux

Aucun. Script d'action produisant HTML ou redirection.

---

## Relations cles

- **Appele par :** `Authenticate.php` (redirection si mot de passe expire), routeur CRM (`action=ChangePassword`)
- **Appelle :** `User::change_password()`, `SugarApplication::redirect()`
- **Affiche :** `modules/Users/Changenewpassword.tpl`

---

## Points d'attention

- Si la redirection wizard (`ut` vide) est declenche, l'utilisateur est envoye vers `Users/Wizard` (ligne 65).
- La validation ID utilise `SuiteValidator::isValidId()` — evite les injections par record ID malformes.
