# SuiteCRM

## Rôle
Namespace SuiteCRM de l'infrastructure de test. Regroupe les classes partagées entre toutes les suites de tests : enums de configuration (drivers DB, breakpoints), cas de test de base PHPUnit, logger de test, et drivers de navigation. Ce sous-arbre fournit les fondations techniques communes à tous les tests du projet.

## Contenu
| Dossier | Rôle |
|---|---|
| `Enumerator/` | Enums pour paramétrer les tests (DatabaseDriver, DesignBreakPoint, SugarObjectType) |
| `Test/` | Classes de base PHPUnit, BeanFactoryTestCase, TestLogger, drivers navigation |

## Points d'entrée
- `Test/SuitePHPUnitFrameworkTestCase.php` — point d'entrée principal pour tous les tests unitaires

## Dépendances clés
- Dépend de : PHPUnit, Codeception, SuiteCRM core
- Utilisé par : `tests/unit/`, `tests/acceptance/`, `tests/api/`

## Notes
Equivalent du dossier `tests/support` mais organisé par namespace PHP SuiteCRM.
