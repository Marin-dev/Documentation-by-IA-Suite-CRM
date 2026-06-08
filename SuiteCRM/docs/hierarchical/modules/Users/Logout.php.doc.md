# Fichier : Logout.php

**Chemin :** `modules/Users/Logout.php`
**Type :** PHP — Script d'action (deconnexion)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Gere la deconnexion de l'utilisateur : sauvegarde le dernier theme utilise, vide la session, detruit le cookie de session, declenche les hooks avant/apres deconnexion, et appelle la methode `logout()` du controleur d'authentification.

## Role technique

Script procedural. Parcourt `$_SESSION` pour vider chaque cle (evite les segfaults PHP sur certaines versions). Appelle les logic hooks `before_logout` et `after_logout`. Delègue la deconnexion SSO/SAML/LDAP a `$authController->authController->logout()`.

---

## Dependances principales

| Dependance | Role |
|---|---|
| `$authController` | Logout SSO/auth externe |
| `$current_user` | Sauvegarde dernier theme (`setPreference('lastTheme')`) |
| `LogicHook` | Hooks `before_logout` / `after_logout` |
| `SugarApplication::setCookie()` | Suppression cookie de session |

## Exports / Symboles principaux

Aucun. Script d'action pur.

---

## Relations cles

- **Appele par :** routeur CRM (`action=Logout`)
- **Appelle :** `LogicHook`, `session_destroy()`, `$authController->authController->logout()`

---

## Points d'attention

- Le vidage de session utilise `$_SESSION[$key] = ''` (et non `unset`) pour eviter les segfaults (commentaire ligne 58).
- Le cookie est supprime avec une date d'expiration dans le passe (`time()-42000`).
