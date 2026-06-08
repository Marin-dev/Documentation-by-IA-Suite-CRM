# 📄 AccessTokenRepository.php

**Chemin :** `lib/API/OAuth2/Repositories/AccessTokenRepository.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Repository OAuth2 pour la persistance des tokens d'accès dans la table `OAuth2Tokens` de SuiteCRM. Gère la création, la révocation et la vérification d'expiration des access tokens.

## ⚙️ Rôle technique
Implémente `AccessTokenRepositoryInterface`. Méthodes :
- `persistNewAccessToken()` : crée un enregistrement `OAuth2Tokens` avec `access_token`, `expires`, `client`, `assigned_user_id`
- `revokeAccessToken(string $tokenId)` : met `token_is_revoked = true` pour tous les enregistrements correspondants
- `isAccessTokenRevoked(string $tokenId)` : vérifie si le token est expiré ou révoqué (compare `access_token_expires` avec l'heure courante)
- `getNewToken()` : crée une nouvelle instance `AccessTokenEntity`

---

## 📥 Entrées / Dépendances
- `League\OAuth2\Server\Entities\AccessTokenEntityInterface`, `ClientEntityInterface`
- `League\OAuth2\Server\Repositories\AccessTokenRepositoryInterface`
- `SuiteCRM\API\OAuth2\Entities\AccessTokenEntity`
- `\OAuth2Tokens`, `\OAuth2Clients` (SugarBeans)
- `$timedate` (global SuiteCRM)

## 📤 Sorties / Exports
- `AccessTokenRepository` — classe (repository)
  - `persistNewAccessToken(AccessTokenEntityInterface): void`
  - `revokeAccessToken(string): void`
  - `isAccessTokenRevoked(string): bool`
  - `getNewToken(ClientEntityInterface, array, $user): AccessTokenEntity`
- **Consommateurs identifiés :** `AuthorizationServer` (via league/oauth2-server)

## 🔗 Relations clés
- **Appelé par :** librairie League OAuth2 (interne au flux de token)
- **Position dans le flux global :** persistance des tokens d'accès

---

## 💡 Points d'attention
- `isAccessTokenRevoked()` re-sauvegarde le token avec `token_is_revoked = true` quand il est expiré — double écriture en BD pour marquer l'expiration.
- `revokeAccessToken()` peut révoquer plusieurs tokens si plusieurs lignes ont le même `access_token` (hypothèse : unicité non garantie par contrainte DB).
