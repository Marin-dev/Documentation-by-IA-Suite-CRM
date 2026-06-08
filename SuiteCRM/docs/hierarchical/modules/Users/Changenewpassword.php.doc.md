# Fichier : Changenewpassword.php

**Chemin :** `modules/Users/Changenewpassword.php`
**Type :** PHP — Point d'entree (reset mot de passe par lien)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Gere le flux de reinitialisation de mot de passe via un lien email temporaire. Verifie la validite du lien (GUID + cle hashee + expiration), affiche le formulaire de saisie du nouveau mot de passe, puis authentifie automatiquement l'utilisateur apres changement reussi.

## Role technique

Script procedural accessible via `entryPoint=Changenewpassword`. Lit `guid` et `key` en parametre, requete la table `users_password_link`, verifie le hash de la cle avec `User::checkPassword()`, controle l'expiration selon `$sugar_config['passwordsetting']['linkexpiration']`. Si valide et formulaire soumis (`login=1`), appelle `$usr->setNewPassword()`, invalide le lien (deleted=1) et execute l'application pour connecter l'utilisateur. Integre la validation reCAPTCHA. Affiche le template via `Changenewpassword.tpl`.

---

## Dependances principales

| Import | Role |
|---|---|
| `DBManagerFactory` | Requetes sur `users_password_link` |
| `User::checkPassword()` | Verification hash cle |
| `BeanFactory::getBean('Users')` | Chargement utilisateur |
| `recaptcha_utils.php` | Validation CAPTCHA |
| `SugarView` | Header/footer page |
| `Sugar_Smarty` | Rendu formulaire |

## Exports / Symboles principaux

Aucun. Script d'action/vue.

---

## Relations cles

- **Appele par :** `GeneratePassword.php` (creation du lien), email de reset
- **Appelle :** `User::checkPassword()`, `$usr->setNewPassword()`, `$GLOBALS['app']->execute()` (reauthentification)
- **Table utilisee :** `users_password_link` (id, keyhash, username, date_generated, user_id, deleted)

---

## Points d'attention

- Apres changement reussi, le script appelle `$GLOBALS['app']->execute()` suivi de `die()` pour connecter l'utilisateur sans redirection visible (ligne 132-134).
- L'expiration du lien calcule `date_generated + Z` (offset timezone, ligne 91) — attention aux fuseaux horaires serveur.
- Si le lien est expire, il est immediatement invalide (`deleted=1`, ligne 141) — lien a usage unique.
