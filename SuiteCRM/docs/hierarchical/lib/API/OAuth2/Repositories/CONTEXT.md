# Repositories

## Rôle
Ce dossier contient les repositories OAuth2 de la couche `lib/API`. Ces repositories gèrent la persistance et la récupération des entités OAuth2 (tokens d'accès, codes d'autorisation, clients, tokens de rafraîchissement, scopes, utilisateurs) dans la base de données SuiteCRM via les beans `OAuth2Tokens`, `OAuth2Clients` et `Users`. Ils implémentent les interfaces de `league/oauth2-server`.

## Contenu
| Fichier | Rôle |
|---|---|
| `AccessTokenRepository.php` | Persistance, révocation et vérification des tokens d'accès |
| `AuthCodeRepository.php` | Persistance et validation des codes d'autorisation OAuth2 |
| `ClientRepository.php` | Récupération et validation des clients OAuth2 |
| `RefreshTokenRepository.php` | Persistance, révocation et vérification des tokens de rafraîchissement |
| `ScopeRepository.php` | Résolution et validation des scopes OAuth2 |
| `UserRepository.php` | Authentification et récupération des utilisateurs SuiteCRM |

## Points d'entrée
- `AccessTokenRepository.php` — repository central du flux OAuth2
- `ClientRepository.php` — validé en premier lors de chaque demande de token

## Dépendances clés
- **Dépend de :** `lib/API/OAuth2/Entities/`, `league/oauth2-server` (interfaces repositories), beans SuiteCRM (`OAuth2Tokens`, `OAuth2Clients`, `Users`), `$timedate` global
- **Utilisé par :** `lib/API/OAuth2/Middleware/AuthorizationServer` et `ResourceServer` (via injection League OAuth2)

## Notes
- `isAccessTokenRevoked()` écrit en BD pour marquer l'expiration — double écriture intentionnelle.
- `UserRepository` s'appuie sur l'authentification SuiteCRM native (hachage MD5).
- Ces repositories correspondent aux repositories parallèles dans `Api/V8/OAuth2/Repository/`.
