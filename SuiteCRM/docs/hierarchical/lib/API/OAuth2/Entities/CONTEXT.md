# Entities

## Rôle
Ce dossier contient les entités OAuth2 de la couche `lib/API`. Ces entités représentent les objets du protocole OAuth2 (tokens, client, utilisateur, scope, code d'autorisation) et sont utilisées par la librairie `league/oauth2-server` pour transporter les informations d'authentification au cours des flux OAuth2. Elles n'implémentent aucune logique propre — tout est délégué aux traits League.

## Contenu
| Fichier | Rôle |
|---|---|
| `AccessTokenEntity.php` | Entité jeton d'accès OAuth2 (JWT) |
| `AuthCodeEntity.php` | Entité code d'autorisation OAuth2 |
| `ClientEntity.php` | Entité client OAuth2 (application cliente) |
| `RefreshTokenEntity.php` | Entité jeton de rafraîchissement OAuth2 |
| `ScopeEntity.php` | Entité scope OAuth2 (périmètre d'accès) |
| `UserEntity.php` | Entité utilisateur OAuth2 |

## Points d'entrée
- `AccessTokenEntity.php` — entité principale, créée par `AccessTokenRepository::getNewToken()`
- `ClientEntity.php` — entité client, instanciée par `ClientRepository`

## Dépendances clés
- **Dépend de :** `league/oauth2-server` (interfaces et traits)
- **Utilisé par :** `lib/API/OAuth2/Repositories/` — chaque repository crée et retourne l'entité correspondante

## Notes
- Toutes les entités sont passives : elles ne contiennent que la composition de traits League OAuth2.
- Ces entités correspondent aux entités parallèles dans `Api/V8/OAuth2/Entity/` (couche applicative vs couche lib).
