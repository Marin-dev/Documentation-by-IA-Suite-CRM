# Fichier : User.php

**Chemin :** `modules/Users/User.php`
**Type :** PHP — Modele (SugarBean)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Modele central du module Users. Represente un utilisateur CRM (agent, administrateur, utilisateur groupe ou portail). Gere la creation, la modification, l'authentification et les preferences de l'utilisateur. Sert de bean de reference pour toute operation liee a un utilisateur dans l'application.

## Role technique

La classe `User` etend `Person` et implemente `EmailInterface`. Elle stocke tous les champs utilisateur (nom, contacts, adresse, statut, roles). Elle encapsule la gestion des signatures email (table `users_signatures`), les preferences utilisateur via `UserPreference`, l'authentification par hash de mot de passe, et la double authentification (`factor_auth`). Elle surcharge `save()` avec une logique specifique aux emails.

---

## Dependances principales

| Import | Chemin | Role |
|---|---|---|
| `Person` | `include/SugarObjects/templates/person/Person.php` | Classe parente (SugarBean specialise personne) |
| `EmailInterface` | `include/EmailInterface.php` | Interface email |
| `EmailUI` | `modules/Emails/EmailUI.php` | Gestion UI email |
| `UserPreference` | `modules/UserPreferences/UserPreference.php` | Preferences utilisateur (chargee dans `__construct`) |

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `User` | classe | Bean principal utilisateur |
| `User::getSystemUser()` | methode | Recupere l'utilisateur admin systeme (id=1 ou premier admin actif) |
| `User::getDefaultSignature()` | methode | Retourne la signature email par defaut |
| `User::getSignatures()` / `getSignaturesArray()` | methodes | Retourne les signatures HTML ou tableau |
| `User::getEmailAccountSignatures()` | methode | Signatures pour comptes email |
| `User::generatePassword()` | methode statique | Genere un mot de passe aleatoire |
| `User::getPasswordHash()` | methode statique | Hache un mot de passe |
| `User::checkPassword()` | methode statique | Verifie un mot de passe contre son hash |
| `User::getAllUsers()` / `getActiveUsers()` | methodes statiques | Listes des utilisateurs |
| `$table_name` | propriete | `users` |
| `$factor_auth` | propriete | Active ou non la double authentification |
| `$lastSaveErrorIsEmailAddressSaveError` | propriete | Indique si une erreur de sauvegarde est liee aux emails |

## Consommateurs identifies

- `modules/Users/controller.php` — utilise `BeanFactory::newBean('Users')`
- `modules/Users/GeneratePassword.php` — instancie `new user()`
- `modules/Users/reassignUserRecords.php` — appelle `User::getAllUsers()`, `User::getActiveUsers()`
- `modules/Users/ChangePassword.php` — appelle `$focus->change_password()`
- `modules/Users/Changenewpassword.php` — appelle `User::checkPassword()`, `$usr->setNewPassword()`

---

## Relations cles

- **Etend :** `Person` (include/SugarObjects/templates/person/Person.php)
- **Implemente :** `EmailInterface`
- **Appelle :** `UserPreference`, `DBManager`, `users_signatures` (SQL direct)
- **Appele par :** quasiment tous les modules du CRM via `$GLOBALS['current_user']` ou `BeanFactory`

---

## Points d'attention

- `save()` peut retourner `false` meme si l'utilisateur est sauvegarde correctement, si les adresses email echouent. Le flag `$lastSaveErrorIsEmailAddressSaveError` permet de distinguer ce cas (ligne 141).
- `__set()` logue un message `fatal` si `id` est mis a `1` (detection debug, ligne 153-155).
- `getSystemUser()` tente d'abord `retrieve('1')` ; si cet ID n'existe pas, cherche le premier admin actif — comportement a connaitre lors de migrations.
- Champs `$encodeFields` = `['first_name', 'last_name', 'description']` (echappement HTML automatique).
