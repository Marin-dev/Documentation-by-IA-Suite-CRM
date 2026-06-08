# route

## Rôle
Ce dossier contient les fichiers de définition des routes de l'API v8 de SuiteCRM. Chaque fichier enregistre un groupe de routes Slim correspondant à un domaine fonctionnel : opérations sur les modules, flux OAuth2, et exposition du schéma API. Les routes lient les URLs aux méthodes des contrôleurs.

## Contenu
| Fichier | Rôle |
|---|---|
| `moduleRoutes.php` | Définit les routes CRUD des modules (`GET/POST/PATCH/DELETE /api/v8/module/{moduleName}`) |
| `oauth2Routes.php` | Définit les routes OAuth2 (`POST /api/v8/oauth2/token`, `/oauth2/refresh`, `/oauth2/revoke`) |
| `schemaRoutes.php` | Définit les routes de schéma (`GET /api/v8/module/{moduleName}/schema`) |

## Points d'entrée
- `moduleRoutes.php` — routes principales de l'API, les plus utilisées
- `oauth2Routes.php` — routes d'authentification, point d'entrée pour obtenir un token

## Dépendances clés
- **Dépend de :** `lib/API/v8/Controller/ModuleController`, `lib/API/v8/Controller/OAuth2Controller`, `lib/API/v8/Controller/SchemaController`
- **Utilisé par :** bootstrapper de l'API v8 (`lib/API/core/app.php`)

## Notes
- Les routes sont enregistrées dans l'application Slim lors du bootstrap.
- Les routes de modules supportent les relations via `/module/{name}/{id}/relationships/{linkField}`.
