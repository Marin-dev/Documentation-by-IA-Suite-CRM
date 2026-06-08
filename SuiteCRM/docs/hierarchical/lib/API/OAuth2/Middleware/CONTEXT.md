# Middleware

## Rôle
Ce dossier contient les middlewares OAuth2 de la couche `lib/API`. Il expose le serveur d'autorisation (`AuthorizationServer`) qui émet les tokens JWT, et le serveur de ressources (`ResourceServer`) qui valide les tokens sur chaque requête API. Ces deux middlewares sont les gardiens centraux de la sécurité de l'API SuiteCRM.

## Contenu
| Fichier | Rôle |
|---|---|
| `AuthorizationServer.php` | Serveur OAuth2 d'émission de tokens — gère tous les grant types (password, client_credentials, refresh_token, authorization_code) |
| `ResourceServer.php` | Serveur OAuth2 de validation de tokens — vérifie chaque JWT sur les requêtes entrantes |

## Points d'entrée
- `AuthorizationServer.php` — utilisé lors de la demande de token (`POST /oauth/token`)
- `ResourceServer.php` — middleware exécuté sur chaque requête API protégée

## Dépendances clés
- **Dépend de :** `league/oauth2-server` (interfaces Grant, CryptKey, BearerTokenResponse), `lib/API/OAuth2/Repositories/`, clés RSA OAuth2
- **Utilisé par :** containers DI (`lib/API/v8/container/AuthorizationServer.php`, `lib/API/v8/container/ResourceServer.php`), contrôleur `OAuth2Controller`

## Notes
- `AuthorizationServer` est un fork de la classe League — surveiller les mises à jour de sécurité.
- TTL par défaut des tokens : 1 heure si non spécifié via `enableGrantType()`.
- La clé de chiffrement (`encryptionKey`) est obligatoire depuis league/oauth2-server v5 — son absence génère une deprecation.
