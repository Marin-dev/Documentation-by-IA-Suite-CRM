# 📄 UserRepository.php

**Chemin :** `lib/API/OAuth2/Repositories/UserRepository.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Repository OAuth2 pour l'authentification des utilisateurs via le grant type `password`. Valide les credentials (username/password) contre le système d'authentification SuiteCRM et retourne une entité utilisateur.

## ⚙️ Rôle technique
Implémente `UserRepositoryInterface`. `getUserEntityByUserCredentials()` :
1. Charge `AuthenticationController` depuis le module `Users`
2. Appelle `$authController->login($username, $password, ['passwordEncrypted' => false])`
3. Si succès, récupère l'ID via `User::retrieve_user_id($username)` et retourne une `UserEntity`
4. Retourne `null` si échec

---

## 📥 Entrées / Dépendances
- `League\OAuth2\Server\Entities\ClientEntityInterface`
- `League\OAuth2\Server\Repositories\UserRepositoryInterface`
- `SuiteCRM\API\OAuth2\Entities\UserEntity`
- `SuiteCRM\Utility\Paths`
- `\AuthenticationController`, `\User` (classes SugarCRM)

## 📤 Sorties / Exports
- `UserRepository` — classe (repository)
  - `getUserEntityByUserCredentials(string, string, string, ClientEntityInterface): ?UserEntity`
- **Consommateurs identifiés :** librairie League OAuth2 (flux password grant)

---

## 💡 Points d'attention
- Le mot de passe est transmis en clair à `login()` (`passwordEncrypted: false`) — s'assurer que la couche de transport est HTTPS.
- Dépendance directe à `AuthenticationController` via `require_once` — couplage fort au système de fichiers SuiteCRM.
- Supporte le SSO et les modules d'authentification personnalisés SuiteCRM via `AuthenticationController`.
