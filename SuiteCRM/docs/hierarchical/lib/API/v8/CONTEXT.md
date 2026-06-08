# v8

## Rôle
Ce dossier contient l'implémentation de l'API REST v8 de SuiteCRM côté `lib/`. Il regroupe les contrôleurs (CRUD modules, OAuth2, schéma), les exceptions HTTP, les bibliothèques utilitaires, les callables de configuration, les fichiers de container DI et les définitions de routes. C'est le coeur de l'API REST v8 avant migration vers `Api/V8/`.

## Contenu
| Dossier | Rôle |
|---|---|
| `Controller/` | Contrôleurs API v8 : `ApiController` (base), `ModuleController`, `OAuth2Controller`, `SchemaController` |
| `Exception/` | Exceptions HTTP typées (400, 403, 404, 405, 406, 409, 415, 501, etc.) |
| `Library/` | Bibliothèques utilitaires : `ModulesLib` (listes paginées), `UtilityLib` |
| `callable/` | Callables de configuration Slim (OAuth2) |
| `container/` | Factories DI pour tous les services de l'API v8 |
| `route/` | Définitions des routes Slim (modules, OAuth2, schéma) |

## Points d'entrée
- `Controller/ModuleController.php` — contrôleur principal des opérations CRUD
- `Controller/OAuth2Controller.php` — contrôleur d'authentification
- `route/moduleRoutes.php` — routes des modules

## Dépendances clés
- **Dépend de :** `lib/API/JsonApi/v1/`, `lib/API/OAuth2/`, `lib/Utility/`, container DI Slim, `\BeanFactory`
- **Utilisé par :** `lib/API/core/app.php`, `lib/API/core/containers.php`

## Notes
- `ApiController::VERSION_STABILITY = 'ALPHA'` — API en alpha.
- La couche `Api/V8/` (dossier racine) est la nouvelle couche applicative qui prend le relais.
- Bug potentiel dans `ModulesLib` ligne 352 ($limit vs $offset).
