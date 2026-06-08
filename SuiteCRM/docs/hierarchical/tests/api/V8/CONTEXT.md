# V8

## Rôle
Tests d'acceptation pour l'API V8 (JSON:API) de SuiteCRM. Vérifie les opérations CRUD via les endpoints REST V8 : authentification OAuth2, création, lecture et suppression de modules.

## Contenu
| Fichier | Rôle |
|---|---|
| `OAuth2Cest.php` | Tests d'authentification OAuth2 (obtention token, refresh, révocation) |
| `CreateModuleCest.php` | Tests de création d'enregistrements via POST /api/v8/modules/{module} |
| `GetModuleCest.php` | Tests de lecture d'enregistrements via GET /api/v8/modules/{module} |
| `DeleteModuleCest.php` | Tests de suppression via DELETE /api/v8/modules/{module}/{id} |

## Points d'entrée
- `OAuth2Cest` — prérequis d'authentification pour tous les autres tests API

## Dépendances clés
- Dépend de : `ApiTester`, `_support/Helper/api.php`
- Utilisé par : pipeline CI/CD (suite api)

## Notes
API V8 conforme JSON:API spec. OAuth2 avec client_credentials flow. Tests nécessitent SuiteCRM déployé.
