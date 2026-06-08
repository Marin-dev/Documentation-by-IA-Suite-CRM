# 📄 middlewares.php

**Chemin :** `Api/V8/Config/services/middlewares.php`
**Type :** PHP (configuration — conteneur DI)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Configure et enregistre les serveurs OAuth2 (`AuthorizationServer` et `ResourceServer`) de la bibliothèque `league/oauth2-server` dans le conteneur DI. C'est ici que sont définis les types de grants OAuth2 activés (ClientCredentials, Password, RefreshToken, AuthCode) et les clés cryptographiques utilisées.

**Type :** config

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Api\Core\Config\ApiConfig` | Constantes `OAUTH2_PRIVATE_KEY` et `OAUTH2_PUBLIC_KEY` (chemins des clés) |
| `Api\V8\BeanDecorator\BeanManager` | Injecté dans les repositories OAuth2 |
| `Api\V8\OAuth2\Entity\{AccessTokenEntity, ClientEntity}` | Entités OAuth2 |
| `Api\V8\OAuth2\Repository\{AccessToken, AuthCode, Client, RefreshToken, Scope, User}Repository` | Repositories OAuth2 (persistence des tokens) |
| `League\OAuth2\Server\{AuthorizationServer, ResourceServer}` | Serveurs OAuth2 (league/oauth2-server) |
| `League\OAuth2\Server\Grant\{ClientCredentialsGrant, PasswordGrant, AuthCodeGrant, RefreshTokenGrant}` | Types de grants OAuth2 |
| `League\OAuth2\Server\CryptKey` | Clé cryptographique RSA |
| `Api\V8\Helper\OsHelper` | Détection OS pour les permissions de fichiers |

---

## Services enregistrés

### `AuthorizationServer::class`

Configure le serveur d'émission de tokens avec :
- Clé privée RSA depuis `$GLOBALS['BASE_DIR']` + `ApiConfig::OAUTH2_PRIVATE_KEY`
- Clé de chiffrement symétrique depuis `$GLOBALS['sugar_config']['oauth2_encryption_key']` (fallback : `'SCRM-DEFK'` avec log fatal)
- 4 grants activés :

| Grant | TTL Access Token | TTL Refresh Token |
|---|---|---|
| `ClientCredentialsGrant` | 1h | — |
| `PasswordGrant` | 1h | — |
| `RefreshTokenGrant` | 1h | 1 mois |
| `AuthCodeGrant` | 1h (code : 10 min) | — |

### `ResourceServer::class`

Valide les access tokens entrants avec la clé publique RSA.

---

## Variables d'environnement / globales

| Variable | Usage |
|---|---|
| `$GLOBALS['BASE_DIR']` | Répertoire racine de l'application (doit être défini dans `entryPoint.php`) |
| `$GLOBALS['sugar_config']['oauth2_encryption_key']` | Clé de chiffrement des tokens (optionnelle, fallback dangereux) |
| `$GLOBALS['log']` | Logger SuiteCRM (pour le warning en cas de clé absente) |

---

## Interactions

- **Appelé par :** `Api/V8/Config/services.php` (via `require`)
- **`AuthorizationServer`** : utilisé dans `routes.php` pour le middleware `/access_token`
- **`ResourceServer`** : utilisé dans `routes.php` pour protéger tout le groupe `/V8` et dans `LogoutController`

---

## Notes

- Si `oauth2_encryption_key` est absent de `config.php`, la clé de secours `'SCRM-DEFK'` est utilisée avec un log `fatal` — risque de sécurité majeur en production.
- La vérification des permissions des fichiers de clés est désactivée sur Windows (`OsHelper::OS_WINDOWS`) pour compatibilité.
- `$GLOBALS['BASE_DIR']` doit être défini avant l'appel à ce fichier (commentaire ligne 26 : "base dir must exist in entryPoint.php").
