# 📄 LogoutService.php

**Chemin :** `Api/V8/Service/LogoutService.php`
**Type :** PHP (service)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Service de déconnexion OAuth2. Révoque le token d'accès de l'utilisateur en le supprimant (soft-delete) de la table `OAuth2Tokens`. Retourne une réponse JSON:API de confirmation.

**Type :** service

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\V8\BeanDecorator\BeanManager` | Accès au bean `OAuth2Tokens` |
| `Api\V8\JsonApi\Response\{DocumentResponse, MetaResponse}` | Construction de la réponse |

---

## Exports / Symboles principaux

**Classe :** `Api\V8\Service\LogoutService`

| Méthode | Signature | Description |
|---|---|---|
| `__construct` | `(BeanManager $beanManager)` | Injection du BeanManager |
| `logout` | `(string $accessToken): DocumentResponse` | Révoque le token, lève `InvalidArgumentException` si token introuvable |

---

## Flux de `logout`

1. `BeanManager::newBeanSafe(OAuth2Tokens::class)` — crée une instance vide du bean token
2. `retrieve_by_string_fields(['access_token' => $accessToken])` — recherche par valeur du token
3. Si `$token->id === null` → `InvalidArgumentException('Access token is not found for this client')`
4. `$token->mark_deleted($token->id)` — soft-delete SuiteCRM
5. Retourne `DocumentResponse` avec `MetaResponse(['message' => 'You have been successfully logged out'])`

---

## Interactions

- **Appelé par :** `LogoutController` (INCONNU le détail d'invocation)
- **Consommé dans DI :** `Api/V8/Config/services/services.php`
- **Appelle :** `SugarBean::retrieve_by_string_fields`, `SugarBean::mark_deleted`

---

## Notes

- Commentaire ligne 32 : "same logic in Access and Refresh token repository, refactor this later" — dette technique identifiée.
- `mark_deleted` est un soft-delete SuiteCRM standard (positionne `deleted=1` en base).
- La validation du token OAuth2 (signature JWT) est faite en amont par le middleware `ResourceServerMiddleware` dans `routes.php` — `LogoutService` ne fait que la révocation en base.
