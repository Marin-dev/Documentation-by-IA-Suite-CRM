# Exception

## Rôle
Ce dossier regroupe les exceptions du sous-système OAuth2 de la couche `lib/API`. Ces exceptions représentent les cas d'erreur spécifiques au protocole OAuth2 dans SuiteCRM : erreurs génériques OAuth2 et tentatives d'utilisation de grant types non autorisés pour un client donné.

## Contenu
| Fichier | Rôle |
|---|---|
| `OAuth2.php` | Exception de base du sous-système OAuth2 |
| `GrantTypeNotAllowedForClient.php` | Levée quand un client tente d'utiliser un grant type non autorisé |

## Points d'entrée
- `OAuth2.php` — classe de base de la hiérarchie d'exceptions OAuth2

## Dépendances clés
- **Dépend de :** `SuiteCRM\Exception\Exception` (classe parente)
- **Utilisé par :** `lib/API/OAuth2/Repositories/ClientRepository.php`, middlewares OAuth2

## Notes
- Hiérarchie d'exceptions légère — uniquement deux classes.
- `GrantTypeNotAllowedForClient` est levée par `ClientRepository` lors de la validation du client.
