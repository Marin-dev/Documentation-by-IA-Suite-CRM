# Fichier : OAuth2Controller.php

**Chemin :** `lib/API/v8/Controller/OAuth2Controller.php`
**Type :** PHP — controller
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Contrôleur dédié à l'authentification OAuth2 de l'API v8. Il expose un unique point d'entrée (`authenticate`) qui délègue la génération du token d'accès au serveur d'autorisation OAuth2 (League OAuth2 Server). C'est la porte d'entrée pour obtenir un `access_token` via les grants `password` ou `client_credentials`.

**Type :** controller

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `League\OAuth2\Server\Exception\OAuthServerException` | Exceptions spécifiques OAuth2 |
| `Psr\Http\Message\ResponseInterface` | Réponse HTTP PSR-7 |
| `Psr\Http\Message\ServerRequestInterface` | Requête HTTP PSR-7 |
| `SuiteCRM\API\OAuth2\Middleware\AuthorizationServer` | Serveur d'autorisation OAuth2 |
| `ApiController` (parent) | Classe de base (negotiation contenu, gestion erreurs) |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `OAuth2Controller` | classe | Contrôleur d'authentification OAuth2 |
| `authenticate()` | méthode publique | Traite `POST /oauth/access_token`, retourne un token JWT |

---

## Interactions

**Appelé par :**
- `lib/API/v8/route/oauth2Routes.php` → route `POST /oauth/access_token`
- `lib/API/v8/container/OAuth2Controller.php` (instanciation DI)

**Appelle :**
- Container `AuthorizationServer` (`lib/API/v8/container/AuthorizationServer.php`)
- `$server->respondToAccessTokenRequest()` — League OAuth2 Server
- `ApiController::handleExceptionIntoPayloadError()` et `generateJsonApiResponse()` (héritage)

---

## Notes

- La méthode `authenticate()` capture `OAuthServerException` et génère une réponse HTTP via `$exception->generateHttpResponse($response)` — comportement natif League OAuth2 Server.
- Les erreurs non-OAuth2 tombent dans le handler générique de la classe parente.
- Le container `AuthorizationServer` configure deux grants : `PasswordGrant` (TTL token 1h, refresh 1 mois) et `ClientCredentialsGrant`.
