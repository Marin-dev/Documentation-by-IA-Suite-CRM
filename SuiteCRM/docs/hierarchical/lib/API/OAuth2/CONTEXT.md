# OAuth2

## Rôle
Ce dossier implémente la couche OAuth2 de l'API SuiteCRM côté `lib/`. Il fournit les entités OAuth2 (tokens, client, utilisateur, scope), les repositories de persistance, les middlewares serveur d'autorisation/ressources, les exceptions et la gestion des clés RSA. Il s'appuie sur la bibliothèque `league/oauth2-server` et stocke les tokens dans les beans SuiteCRM `OAuth2Tokens` et `OAuth2Clients`.

## Contenu
| Dossier/Fichier | Rôle |
|---|---|
| `Keys.php` | Gestion des clés RSA OAuth2 — génération automatique via OpenSSL |
| `Entities/` | Entités OAuth2 passives (AccessToken, AuthCode, Client, RefreshToken, Scope, User) |
| `Exception/` | Exceptions OAuth2 (base + GrantTypeNotAllowed) |
| `Middleware/` | Serveurs OAuth2 : AuthorizationServer (émission tokens) + ResourceServer (validation) |
| `Repositories/` | Persistance des entités OAuth2 en BD via beans SuiteCRM |

## Points d'entrée
- `Middleware/AuthorizationServer.php` — émission des tokens JWT
- `Middleware/ResourceServer.php` — validation des tokens sur chaque requête
- `Keys.php` — initialisation des clés RSA

## Dépendances clés
- **Dépend de :** `league/oauth2-server`, beans SuiteCRM `OAuth2Tokens`/`OAuth2Clients`/`Users`, extension PHP `openssl`
- **Utilisé par :** `lib/API/v8/container/AuthorizationServer.php`, `lib/API/v8/container/ResourceServer.php`, `lib/API/v8/Controller/OAuth2Controller.php`

## Notes
- Les clés RSA sont stockées dans `lib/API/OAuth2/` — protéger ce répertoire contre l'accès web public.
- `isAccessTokenRevoked()` écrit en BD pour marquer l'expiration — double écriture intentionnelle.
- `AuthorizationServer` est un fork de League — surveiller les mises à jour de sécurité.
