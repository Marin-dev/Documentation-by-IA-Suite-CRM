# 📄 AuthorizationServer.php (Middleware)

**Chemin :** `lib/API/OAuth2/Middleware/AuthorizationServer.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Serveur d'autorisation OAuth2. Gère l'émission des tokens d'accès et la validation des requêtes d'autorisation pour tous les grant types activés (password, client_credentials, refresh_token, etc.). C'est le point central d'émission des tokens JWT SuiteCRM.

## ⚙️ Rôle technique
Réimplémentation/fork de `League\OAuth2\Server\AuthorizationServer` (même interface, même comportement). Implémente `EmitterAwareInterface`. Méthodes principales :
- `enableGrantType(GrantTypeInterface, DateInterval)` : active un grant type avec son TTL de token
- `validateAuthorizationRequest(Request)` : valide une demande d'autorisation (flux Authorization Code)
- `completeAuthorizationRequest(AuthorizationRequest, Response)` : complète le flux Authorization Code
- `respondToAccessTokenRequest(Request, Response)` : traite les demandes de token (password, client_credentials, refresh_token)

Utilise `CryptKey` pour les clés RSA et `BearerTokenResponse` pour le format de réponse JWT.

---

## 📥 Entrées / Dépendances
- `League\OAuth2\Server\CryptKey`
- `League\OAuth2\Server\Exception\OAuthServerException`
- `League\OAuth2\Server\Grant\GrantTypeInterface`
- `League\OAuth2\Server\Repositories\AccessTokenRepositoryInterface`, `ClientRepositoryInterface`, `ScopeRepositoryInterface`
- `League\OAuth2\Server\ResponseTypes\BearerTokenResponse`
- `League\Event\EmitterAwareInterface`, `EmitterAwareTrait`

## 📤 Sorties / Exports
- `AuthorizationServer` — classe (serveur OAuth2)
  - `enableGrantType(GrantTypeInterface, ?DateInterval): void`
  - `validateAuthorizationRequest(Request): AuthorizationRequest`
  - `completeAuthorizationRequest(AuthorizationRequest, Response): Response`
  - `respondToAccessTokenRequest(Request, Response): Response`
  - `setEncryptionKey(string): void`
- **Consommateurs identifiés :** INCONNU (containers v8)

## 🔗 Relations clés
- **Appelé par :** contrôleur OAuth2 (INCONNU — à chercher dans `lib/API/v8/`)
- **Position dans le flux global :** cœur de l'émission des tokens OAuth2

---

## 💡 Points d'attention
- Si `encryptionKey` est null, un `E_USER_DEPRECATED` est déclenché — obligatoire depuis league/oauth2-server v5 pour la sécurité.
- TTL par défaut des tokens : 1 heure (`PT1H`) si non spécifié lors de `enableGrantType()`.
- Cette classe est un fork de la librairie League — vérifier les mises à jour de sécurité de la librairie originale.
