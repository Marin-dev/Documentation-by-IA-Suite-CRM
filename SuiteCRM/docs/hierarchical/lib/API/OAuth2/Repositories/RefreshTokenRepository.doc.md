# 📄 RefreshTokenRepository.php

**Chemin :** `lib/API/OAuth2/Repositories/RefreshTokenRepository.php`
**Type :** `PHP`
**Dernière mise à jour doc :** 2026-05-30

---

## 🎯 Rôle fonctionnel
Repository OAuth2 pour la persistance des refresh tokens dans la table `OAuth2Tokens`. Lie le refresh token à l'access token correspondant et gère son expiration.

## ⚙️ Rôle technique
Implémente `RefreshTokenRepositoryInterface`. Méthodes :
- `persistNewRefreshToken()` : retrouve le token `OAuth2Tokens` par `access_token`, ajoute le `refresh_token` et sa date d'expiration
- `revokeRefreshToken(string $tokenId)` : met `token_is_revoked = true` (utilise `access_token` comme identifiant — **attention : paramètre nommé $tokenId mais compare sur access_token**)
- `isRefreshTokenRevoked(string $tokenId)` : même logique d'expiration que `AccessTokenRepository`
- `getNewRefreshToken()` : crée une `RefreshTokenEntity`

---

## 📤 Sorties / Exports
- `RefreshTokenRepository` — classe (repository)
  - `persistNewRefreshToken(RefreshTokenEntityInterface): void`
  - `revokeRefreshToken(string): void`
  - `isRefreshTokenRevoked(string): bool`
  - `getNewRefreshToken(): RefreshTokenEntity`

---

## 💡 Points d'attention
- **Incohérence** : `revokeRefreshToken($tokenId)` et `isRefreshTokenRevoked($tokenId)` recherchent sur le champ `access_token` et non sur `refresh_token` — la révocation par identifiant de refresh token peut ne pas fonctionner correctement.
- Le refresh token et l'access token partagent la même ligne en BD (`OAuth2Tokens`) — design qui peut compliquer la révocation sélective.
