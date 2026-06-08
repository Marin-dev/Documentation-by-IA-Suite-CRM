# Controller

## Rôle
Ce dossier contient les contrôleurs de l'API v8 de SuiteCRM. `ApiController` est la classe de base abstraite qui fournit les mécanismes communs (réponses JSON:API, gestion d'erreurs, négociation de contenu, validation de schéma). `ModuleController`, `OAuth2Controller` et `SchemaController` implémentent les opérations CRUD des modules, le flux OAuth2 et l'exposition du schéma API respectivement.

## Contenu
| Fichier | Rôle |
|---|---|
| `ApiController.php` | Classe de base abstraite — génération réponses JSON:API, gestion erreurs, validation schéma |
| `ModuleController.php` | Opérations CRUD sur les modules SuiteCRM via JSON:API |
| `OAuth2Controller.php` | Endpoints OAuth2 (token, refresh) |
| `SchemaController.php` | Exposition du schéma JSON:API des modules disponibles |

## Points d'entrée
- `ModuleController.php` — contrôleur principal, point d'entrée pour les opérations CRUD
- `OAuth2Controller.php` — point d'entrée pour l'authentification

## Dépendances clés
- **Dépend de :** `lib/API/JsonApi/v1/JsonApi`, `lib/API/JsonApi/v1/Resource/SuiteBeanResource`, `lib/API/OAuth2/Middleware/`, `Slim\Http\Request`, `JsonSchema\Validator`
- **Utilisé par :** containers DI (`lib/API/v8/container/`), routes (`lib/API/v8/route/`)

## Notes
- `ApiController::VERSION_STABILITY = 'ALPHA'` — l'API v8 est en alpha.
- `negotiatedJsonApiContent()` est strict sur le Content-Type (`application/vnd.api+json`).
- `generateJsonApiResponse()` valide la réponse sortante contre le schéma avant envoi.
