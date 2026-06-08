# Fichier : RefreshTokenRepository.php

**Chemin :** `Api/V8/OAuth2/Repository/RefreshTokenRepository.php`
**Type :** service
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Repository OAuth2 gérant le cycle de vie des jetons de rafraîchissement. Lie le refresh token au record `OAuth2Tokens` existant (créé lors de la persistance de l'access token), gère la révocation et la vérification d'expiration. Implémente `RefreshTokenRepositoryInterface` de `league/oauth2-server`.

---

## Type

service

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\BeanDecorator\BeanManager` | Accès au bean `OAuth2Tokens` |
| `Api\V8\OAuth2\Entity\RefreshTokenEntity` | Entité retournée par `getNewRefreshToken()` |
| `League\OAuth2\Server\Entities\RefreshTokenEntityInterface` | Interface de l'entité refresh token |
| `League\OAuth2\Server\Repositories\RefreshTokenRepositoryInterface` | Interface du repository à implémenter |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `RefreshTokenRepository` | classe | Repository de gestion des refresh tokens OAuth2 |
| `getNewRefreshToken()` | méthode publique | Instancie et retourne une nouvelle `RefreshTokenEntity` |
| `persistNewRefreshToken(RefreshTokenEntityInterface)` | méthode publique | Ajoute le refresh token sur le record `OAuth2Tokens` de l'access token associé |
| `revokeRefreshToken(string $tokenId)` | méthode publique | Supprime le refresh token via `mark_deleted` |
| `isRefreshTokenRevoked(string $tokenId)` | méthode publique | Vérifie si le refresh token est absent ou expiré |

---

## Interactions

**Appelé par :**
- `Api/V8/Config/services/middlewares.php` — enregistrement DI

**Appelle :**
- `BeanManager::newBeanSafe(OAuth2Tokens::class)` — accès au bean token (lignes 41, 62, 83)
- `OAuth2Tokens::retrieve_by_string_fields()` — recherche par access_token ou refresh_token
- `OAuth2Tokens::mark_deleted()` — révocation (ligne 73)

---

## Notes

- `persistNewRefreshToken()` retrouve d'abord le record `OAuth2Tokens` existant via l'access token associé au refresh token (ligne 42-43) — le refresh token est un complément au record, pas un bean indépendant.
- Lève `\InvalidArgumentException` si l'access token ou le refresh token n'est pas trouvé lors de la persistance ou révocation (lignes 46-48 et 69-71).
- `isRefreshTokenRevoked()` retourne `true` si la date d'expiration est dépassée OU si le bean est introuvable (ligne 87). Pas de champ `token_is_revoked` pour le refresh token (contrairement à l'access token).
