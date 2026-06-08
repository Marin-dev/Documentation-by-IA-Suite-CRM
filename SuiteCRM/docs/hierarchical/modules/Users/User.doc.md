# User.php

**Chemin :** `modules/Users/User.php`
**Type :** PHP (Model / SugarBean)
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Modèle central de l'entité utilisateur SuiteCRM. Gère l'authentification, les préférences, les mots de passe, les signatures email, les rôles ACL et toutes les opérations CRUD sur les enregistrements `users`.

## Type
model

## Dépendances clés
- `include/SugarObjects/templates/person/Person.php` — classe parente (SugarBean étendu)
- `include/EmailInterface.php` — interface implémentée
- `modules/Emails/EmailUI.php` — génération de liens email
- `modules/UserPreferences/UserPreference` — délégation des préférences (via `_userPreferenceFocus`)
- `modules/MySettings/TabController.php` — gestion des onglets du menu
- `SugarApplication`, `BeanFactory`, `ACLRole`, `DBManagerFactory` — framework SuiteCRM

## Exports / Symboles principaux
- `class User extends Person implements EmailInterface` — bean principal
- `authenticate_user($password)` — authentification MD5 (ligne 1121)
- `load_user($username_password, $password_encoded)` — chargement complet avec session (ligne 1193)
- `findUserPassword($name, $password)` — requête DB avec vérification de hash (ligne 1298, static)
- `getPasswordHash($password)` / `checkPasswordMD5($md5, $hash)` — gestion bcrypt (lignes 1242-1288)
- `change_password($old, $new)` / `setNewPassword($new)` — changement de mot de passe (lignes 1352-1381)
- `save($check_notify)` — sauvegarde avec logique métier (2FA, email, préférences) (ligne 608)
- `setPreference()` / `getPreference()` / `savePreferencesToDB()` — proxy vers UserPreference
- `check_role_membership($role_name, $user_id)` — vérification d'appartenance à un rôle ACL (ligne 1052)
- `getLicensedUsersWhere()` — clause WHERE pour compter les licences (static, ligne 582)
- `getSignatures()` / `getDefaultSignature()` — gestion des signatures email
- `getAllUsers()` / `getActiveUsers()` — listes d'utilisateurs (static)
- `saveFormPreferences()` — sauvegarde des préférences depuis le formulaire POST (ligne 750)

## Interactions
- **Appelé par :** `controller.php` (actions EditView, delete, wizard), `Authenticate.php`, `ChangePassword.php`, `GeneratePassword.php`, `reassignUserRecords.php`
- **Appelle :** `UserPreference`, `ACLRole::getUserRoleNames()`, `BeanFactory`, `EmailUI`, `FactorAuthFactory`, `TabController`
- **Position dans le flux global :** Entité racine du module Users ; utilisée globalement via `$current_user` dans toute l'application

## Notes
- Le hash de mot de passe utilise `password_hash(PASSWORD_DEFAULT)` sur le MD5 du mot de passe en clair. Rétrocompatibilité avec les anciens hash MD5 purs (ligne 1280).
- `save()` retourne `false` si la sauvegarde des adresses email échoue mais que le reste a réussi — ambiguïté documentée via `$lastSaveErrorIsEmailAddressSaveError` (ligne 141).
- La désactivation d'un utilisateur (status=Inactive) déclenche `beforeDisable()` (ligne 694).
- Propriété `#[\AllowDynamicProperties]` : accepte des attributs dynamiques PHP 8.2+.
- L'ID `"1"` est loggé en `fatal` lors de toute tentative d'affectation (ligne 153) — trace de débogage résiduelle.
