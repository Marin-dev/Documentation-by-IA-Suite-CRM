# API

## Rôle
Ce dossier est la racine de la couche API de SuiteCRM dans `lib/`. Il regroupe tout ce qui concerne l'API REST : le bootstrapper (`core/`), l'implémentation JSON:API (`JsonApi/`), la couche OAuth2 (`OAuth2/`), le point d'entrée public (`public/`), et l'implémentation de l'API v8 (`v8/`). C'est la bibliothèque technique sur laquelle repose l'API REST SuiteCRM.

## Contenu
| Dossier | Rôle |
|---|---|
| `core/` | Bootstrap Slim — initialisation DI, routes, lancement app (déprécié pour `Api/V8/`) |
| `JsonApi/` | Bibliothèque JSON:API v1 — ressources, filtres, sérialisation, conformité spec |
| `OAuth2/` | Couche OAuth2 — entités, repositories, middlewares serveur, clés RSA |
| `public/` | Point d'entrée HTTP — entrypoint web de l'ancienne API (déprécié) |
| `v8/` | Implémentation API REST v8 — contrôleurs, exceptions, routes, container DI |

## Points d'entrée
- `public/index.php` — entrypoint HTTP de l'ancienne API (déprécié)
- `v8/Controller/ModuleController.php` — contrôleur principal
- `OAuth2/Middleware/AuthorizationServer.php` — émission des tokens

## Dépendances clés
- **Dépend de :** `league/oauth2-server`, `slim/slim`, `league/uri`, `JsonSchema\Validator`, beans SuiteCRM, `$GLOBALS['BASE_DIR']`, extension `openssl`
- **Utilisé par :** serveur web (requêtes `/api/`), `Api/V8/` (couche applicative qui utilise certaines classes `lib/`)

## Notes
- La couche `lib/API/` est en cours de migration vers `Api/V8/` — certains composants sont déjà dupliqués.
- `lib/API/core/app.php` est déprécié : les nouvelles intégrations doivent pointer vers `Api/V8/`.
- Les clés RSA OAuth2 sont dans `lib/API/OAuth2/` — protéger contre l'accès web public.
