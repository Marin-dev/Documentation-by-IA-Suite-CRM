# tests

## Rôle
Répertoire racine de tous les tests automatisés de SuiteCRM. Organisé par type de test via Codeception : tests d'acceptation UI (acceptance), tests d'API REST (api), tests unitaires PHPUnit (unit). Contient également l'infrastructure partagée (_support/) et le namespace SuiteCRM des classes de base de test.

## Contenu
| Fichier / Dossier | Rôle |
|---|---|
| `_bootstrap.php` | Bootstrap global — initialisation commune à toutes les suites |
| `_support/` | Infrastructure partagée : acteurs, helpers, page objects, steps |
| `SuiteCRM/` | Classes de base de test (SuitePHPUnitFrameworkTestCase, enums, drivers) |
| `acceptance/` | Tests d'acceptation UI — login, Core templates, 35 modules métier |
| `api/` | Tests d'API REST V8 — OAuth2, CRUD modules |
| `unit/` | Tests unitaires PHPUnit — BeanFactory, SugarBean, TimeDate, CalendarSync, Search |

## Points d'entrée
- `_bootstrap.php` — point d'entrée global Codeception
- `acceptance/` — tests end-to-end via navigateur (WebDriver ou PhpBrowser)
- `api/` — tests de contrat API V8
- `unit/` — tests unitaires rapides (PHPUnit)

## Dépendances clés
- Dépend de : Codeception, PHPUnit, Selenium WebDriver (optionnel), SuiteCRM déployé (pour acceptance et api)
- Utilisé par : pipeline CI/CD, développeurs SuiteCRM

## Notes
- 3 suites distinctes : `unit` (rapide, sans déploiement), `api` (nécessite SuiteCRM + API V8), `acceptance` (nécessite SuiteCRM + navigateur)
- Les acteurs (`*Tester.php`) dans `_support/` sont générés par `codecept build` — ne pas modifier manuellement
- `SuiteCRM/Test/SuitePHPUnitFrameworkTestCase` est la classe mère de tous les tests unitaires
