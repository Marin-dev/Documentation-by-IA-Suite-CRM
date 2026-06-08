# core

## Rôle
Ce dossier est le bootstrapper de l'API REST SuiteCRM côté `lib/`. Il contient le point d'entrée `app.php` (déprécié — à migrer vers `Api/V8/`) et le fichier `containers.php` qui configure le container DI de l'API v8. Il initialise Slim, charge les services DI, enregistre les routes et lance l'application.

## Contenu
| Fichier | Rôle |
|---|---|
| `app.php` | Bootstrap Slim de l'API v8 — charge containers, routes, callables, exécute `$app->run()` (déprécié) |
| `containers.php` | Enregistrement de tous les services DI de l'API v8 (controllers, OAuth2, utilities) |

## Points d'entrée
- `app.php` — appelé par `lib/API/public/index.php`

## Dépendances clés
- **Dépend de :** `lib/API/v8/container/`, `lib/API/v8/route/`, `lib/API/v8/callable/`, `vendor/autoload.php`, `include/entryPoint.php`
- **Utilisé par :** `lib/API/public/index.php`

## Notes
- `app.php` est déprécié : les intégrations actuelles doivent pointer vers `Api/V8/` (couche applicative).
- `containers.php` est le fichier pivot qui assemble tout le graphe de dépendances de l'API v8.
