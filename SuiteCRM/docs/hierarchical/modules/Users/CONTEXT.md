# 📁 Users

**Chemin :** `modules/Users/`
**Profondeur :** 3
**Mise à jour :** 2026-06-02

---

## 🎯 Responsabilité fonctionnelle
Le module Users gère les utilisateurs de SuiteCRM. Il couvre l'authentification (MD5/bcrypt, 2FA), la gestion des mots de passe, les préférences utilisateur, les signatures email, les rôles ACL et la réaffectation des enregistrements. `$current_user` est une instance de `User` disponible globalement dans toute l'application.

## ⚙️ Responsabilité technique
Bean `User` (hérite de `Person`, implémente `EmailInterface`). Table `users`. Hash bcrypt sur MD5 avec rétrocompatibilité. Préférences déléguées à `UserPreference`. Supporte PHP 8.2+ `#[\AllowDynamicProperties]`.

---

## 📂 Contenu

### Fichiers documentés (sélection)
| Fichier | Rôle en une ligne | Détails |
|---|---|---|
| `User.php` | Bean central des utilisateurs | [→ fiche](User.doc.md) |
| `controller.php` | Contrôleur MVC | [→ fiche](controller.doc.md) |
| `Authenticate.php` | Action d'authentification | [→ fiche](Authenticate.php.doc.md) |
| `Login.php` | Page de connexion | [→ fiche](Login.php.doc.md) |
| `Logout.php` | Action de déconnexion | [→ fiche](Logout.php.doc.md) |
| `ChangePassword.php` | Changement de mot de passe | [→ fiche](ChangePassword.php.doc.md) |
| `GeneratePassword.php` | Génération de mot de passe | [→ fiche](GeneratePassword.php.doc.md) |
| `password_utils.php` | Utilitaires de gestion des mots de passe | [→ fiche](password_utils.php.doc.md) |
| `UserViewHelper.php` | Helper de vue utilisateur | [→ fiche](UserViewHelper.php.doc.md) |
| `UserSignature.php` | Gestion des signatures email | [→ fiche](UserSignature.php.doc.md) |
| `reassignUserRecords.php` | Réaffectation des enregistrements | [→ fiche](reassignUserRecords.php.doc.md) |
| `vardefs.php` | Schéma de la table `users` | [→ fiche](vardefs.doc.md) |
| `Menu.php` | Menu de navigation | [→ fiche](Menu.php.doc.md) |

---

## 🔗 Interfaces avec le reste du repo
- **Consomme :** `Person`, `EmailInterface`, `UserPreference`, `ACLRole`, `TabController`, `FactorAuthFactory`
- **Consommé par :** Toute l'application via `$current_user`, `ACLController`, `SecurityGroups`
- **Flux typique :** Login → `Authenticate.php` → `User::load_user()` → session → `$current_user` disponible globalement

---

## 🧭 Guide de navigation
| Je cherche à... | Fichier cible |
|---|---|
| Comprendre l'authentification | [`Authenticate.php`](Authenticate.php.doc.md) |
| Voir la logique de mot de passe | [`password_utils.php`](password_utils.php.doc.md) |
| Comprendre le bean User | [`User.php`](User.doc.md) |

---

## ⚠️ Zones INCONNU
- ID `"1"` logué en `fatal` lors d'affectation : trace de débogage résiduelle
- `$lastSaveErrorIsEmailAddressSaveError` : ambiguïté sur le retour de `save()`
