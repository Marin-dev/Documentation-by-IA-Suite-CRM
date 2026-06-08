# Exception

## Rôle
Ce dossier regroupe les exceptions HTTP de l'API v8 de SuiteCRM. Chaque exception représente un code d'erreur HTTP spécifique (400, 403, 404, 405, 406, 409, 415, 501, etc.) et est convertie en réponse JSON:API d'erreur par `ApiController::generateJsonApiErrorResponse()`. Cette hiérarchie d'exceptions garantit des réponses HTTP conformes à la spec JSON:API.

## Contenu
| Fichier | Rôle |
|---|---|
| `ApiException.php` | Exception de base — classe parente de toutes les exceptions API v8 |
| `BadRequestException.php` | HTTP 400 — requête malformée |
| `ConflictException.php` | HTTP 409 — conflit de données |
| `EmptyBodyException.php` | HTTP 400 — corps de requête vide |
| `ForbiddenException.php` | HTTP 403 — accès interdit |
| `IdAlreadyExistsException.php` | HTTP 409 — identifiant déjà utilisé |
| `InvalidJsonApiRequestException.php` | HTTP 400 — requête non conforme JSON:API |
| `InvalidJsonApiResponseException.php` | HTTP 500 — réponse générée non conforme JSON:API |
| `ModuleNotFoundException.php` | HTTP 404 — module SuiteCRM introuvable |
| `NotAcceptableException.php` | HTTP 406 — en-tête Accept non supporté |
| `NotAllowedException.php` | HTTP 405 — méthode HTTP non autorisée |
| `NotFoundException.php` | HTTP 404 — ressource introuvable |
| `NotImplementedException.php` | HTTP 501 — fonctionnalité non implémentée |
| `ReservedKeywordNotAllowedException.php` | HTTP 400 — utilisation d'un mot-clé réservé |
| `UnsupportedMediaTypeException.php` | HTTP 415 — Content-Type non supporté |

## Points d'entrée
- `ApiException.php` — classe de base
- `BadRequestException.php`, `NotFoundException.php` — les plus fréquemment levées

## Dépendances clés
- **Dépend de :** `SuiteCRM\Exception\Exception` ou `RuntimeException`
- **Utilisé par :** tous les contrôleurs et middlewares de `lib/API/v8/`, `lib/API/JsonApi/v1/`

## Notes
- La correspondance exception → code HTTP est gérée par `ApiController::generateJsonApiErrorResponse()`.
- `UnsupportedMediaTypeException` (415) et `NotAcceptableException` (406) sont levées par la négociation de contenu dans `ApiController`.
