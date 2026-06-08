# Fichier : AccessTokenRepository.php

**Chemin :** `Api/V8/OAuth2/Repository/AccessTokenRepository.php`
**Type :** service
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Repository OAuth2 gérant le cycle de vie des jetons d'accès : création, persistance en base, révocation et vérification de validité. Implémente `AccessTokenRepositoryInterface` de `league/oauth2-server`. Interagit avec les beans SuiteCRM `OAuth2Clients` et `OAuth2Tokens`.

---

## Type

service

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\BeanDecorator\BeanManager` | Accès aux beans SuiteCRM (`OAuth2Clients`, `OAuth2Tokens`) |
| `Api\V8\OAuth2\Entity\AccessTokenEntity` | Entité token injectée et retournée par `getNewToken()` |
| `BeanFactory` (global SuiteCRM) | Chargement de l'utilisateur via `BeanFactory::getBean('Users', $userId)` |
| `League\OAuth2\Server\Entities\AccessTokenEntityInterface` | Interface de l'entité token d'accès |
| `League\OAuth2\Server\Entities\ClientEntityInterface` | Interface de l'entité client |
| `League\OAuth2\Server\Repositories\AccessTokenRepositoryInterface` | Interface du repository à implémenter |
| `OAuth2Tokens` (global SuiteCRM) | Bean de persistance des tokens |
| `User` (global SuiteCRM) | Vérification que l'utilisateur est activé |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `AccessTokenRepository` | classe | Repository de gestion des access tokens OAuth2 |
| `getNewToken(ClientEntityInterface, array $scopes, ?string $userIdentifier)` | méthode publique | Configure et retourne l'entité token d'accès |
| `persistNewAccessToken(AccessTokenEntityInterface)` | méthode publique | Persiste le token en base via le bean `OAuth2Tokens` |
| `revokeAccessToken(string $tokenId)` | méthode publique | Marque le token comme supprimé (`mark_deleted`) |
| `isAccessTokenRevoked(string $tokenId)` | méthode publique | Vérifie si le token est révoqué ou expiré |

---

## Interactions

**Appelé par :**
- `Api/V8/Config/services/middlewares.php` — enregistrement DI

**Appelle :**
- `BeanManager::getBeanSafe('OAuth2Clients', $clientId)` — récupération du client (ligne 65)
- `BeanFactory::getBean('Users', $userId)` — vérification de l'utilisateur (ligne 83)
- `BeanManager::newBeanSafe(OAuth2Tokens::class)` — création/lecture de token (lignes 90, 110, 128)
- `OAuth2Tokens::retrieve_by_string_fields()` — recherche par valeur de champ
- `OAuth2Tokens::mark_deleted()` — révocation du token (ligne 119)

---

## Notes

- `persistNewAccessToken()` gère trois types de grant : `authorization_code`, `password` (userId depuis le token) et `client_credentials` (userId depuis `client->assigned_user_id`) (lignes 67-77).
- Lève `InvalidArgumentException('Not Authorized')` si l'utilisateur est introuvable ou désactivé (lignes 84-87).
- `isAccessTokenRevoked()` retourne `true` si le token est absent, si `token_is_revoked === '1'`, ou si la date d'expiration est dépassée (ligne 133).
- La révocation (`revokeAccessToken`) supprime le bean en base via `mark_deleted` — opération douce (soft delete) (ligne 119).
