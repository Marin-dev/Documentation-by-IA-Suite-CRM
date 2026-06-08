# Fichier : GeneratePassword.php

**Chemin :** `modules/Users/GeneratePassword.php`
**Type :** PHP — Script d'action AJAX (generation/envoi de mot de passe)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel

Genere un nouveau mot de passe ou un lien de reinitialisation pour un utilisateur, puis envoie le resultat par email. Utilise en AJAX depuis l'interface d'administration utilisateur. Supporte deux modes : generation de mot de passe direct ou creation d'un lien a usage unique.

## Role technique

Script procedural. Identifie l'utilisateur cible par `user_name` + `email`, ou `userId`, ou `sugar_user_name`. Verifie que l'email principal correspond. Selon le mode (`$_POST['link']`), soit genere un mot de passe via `User::generatePassword()`, soit insere une ligne dans `users_password_link` avec un GUID et une cle hachee. Appelle `$usr->sendEmailForPassword()` avec le template approprie. Retourne `'1'` en succes ou un message d'erreur en echec.

---

## Dependances principales

| Import | Role |
|---|---|
| `include/entryPoint.php` | Bootstrap |
| `modules/Users/language/en_us.lang.php` | Chaines de messages |
| `User::generatePassword()` | Generation mot de passe |
| `User::getPasswordHash()` | Hachage cle de lien |
| `$usr->sendEmailForPassword()` | Envoi email |
| `$sugar_config['passwordsetting']` | Templates email et flags activation |

## Exports / Symboles principaux

Aucun. Sortie : `'1'` (succes) ou string d'erreur (echec). Table ecrite : `users_password_link`.

---

## Relations cles

- **Appele par :** INCONNU — probablement un formulaire AJAX de la vue edition utilisateur
- **Appelle :** `User::generatePassword()`, `User::getPasswordHash()`, `$usr->sendEmailForPassword()`, `DBManager`
- **Lie a :** `Changenewpassword.php` (consomme les liens generes ici)

---

## Points d'attention

- Si `SystemGeneratedPasswordON` est desactive dans la config et que le mode n'est pas "lien", le script retourne `'Access Denied'` (ligne 131).
- La validation email utilise un regex simple (`/^\w+(['\.\-\+]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,})+$/`) — ne couvre pas tous les formats RFC 5321.
- Le lien insere dans `users_password_link` n'a pas de mecanisme de nettoyage automatique des liens expires non utilises.
