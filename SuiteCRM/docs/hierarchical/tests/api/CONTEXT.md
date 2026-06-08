# api

## Rôle
Suite de tests d'API SuiteCRM via Codeception. Teste les endpoints REST de l'API V8 (JSON:API) : authentification OAuth2 et opérations CRUD sur les modules. Ces tests valident le contrat de l'API exposée aux clients externes.

## Contenu
| Fichier / Dossier | Rôle |
|---|---|
| `_bootstrap.php` | Bootstrap de la suite API — initialisation Codeception |
| `V8/` | Tests des endpoints API V8 (OAuth2, CRUD modules) |

## Points d'entrée
- `_bootstrap.php` — chargé automatiquement par Codeception
- `V8/OAuth2Cest.php` — point d'entrée authentification

## Dépendances clés
- Dépend de : `ApiTester`, `_support/Helper/api.php`, SuiteCRM déployé avec API V8 activée
- Utilisé par : pipeline CI/CD, tests de contrat API

## Notes
Tests d'intégration API — nécessitent un SuiteCRM opérationnel. Vérifient la conformité JSON:API spec.
