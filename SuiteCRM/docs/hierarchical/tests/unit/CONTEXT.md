# unit

## Rôle
Suite de tests unitaires SuiteCRM via Codeception + PHPUnit. Teste les composants en isolation (sans BDD réelle, sans navigateur). Organisée autour du dossier `phpunit/` qui reflète la structure du code source.

## Contenu
| Fichier / Dossier | Rôle |
|---|---|
| `_bootstrap.php` | Bootstrap de la suite unitaire — initialisation Codeception/PHPUnit |
| `phpunit/` | Tests PHPUnit organisés par espace de code (data, includes, include, lib) |

## Points d'entrée
- `_bootstrap.php` — chargé automatiquement par Codeception
- `phpunit/` — dossier principal des tests unitaires

## Dépendances clés
- Dépend de : `UnitTester`, `_support/Helper/Unit.php`, PHPUnit, `SuiteCRM/Test/`
- Utilisé par : pipeline CI/CD (suite unit — plus rapide que acceptance et api)

## Notes
Tests sans déploiement SuiteCRM — idéal pour le développement itératif et la régression rapide.
