# _support

## Rôle
Répertoire de support partagé pour toutes les suites de tests Codeception SuiteCRM. Contient les acteurs générés (AcceptanceTester, ApiTester, UnitTester, InstallTester), les helpers de configuration de suite, les Page Objects, les Steps réutilisables et les classes utilitaires transversales.

## Contenu
| Fichier / Dossier | Rôle |
|---|---|
| `AcceptanceTester.php` | Acteur généré pour les tests d'acceptation |
| `ApiTester.php` | Acteur généré pour les tests API |
| `UnitTester.php` | Acteur généré pour les tests unitaires |
| `InstallTester.php` | Acteur généré pour les tests d'installation |
| `ModuleFields.php` | Utilitaire — définition des champs de modules pour les tests |
| `Helper/` | Helpers Codeception par suite (Acceptance, API, Unit, Install, WebDriver, PhpBrowser) |
| `Page/` | Page Objects pour les modules SuiteCRM (Accounts, Basic, Person, Company, etc.) |
| `Step/` | Steps réutilisables pour les tests d'acceptation (navigation, CRUD) |

## Points d'entrée
- `AcceptanceTester` — acteur principal pour tests d'acceptation
- `ApiTester` — acteur principal pour tests API
- `UnitTester` — acteur principal pour tests unitaires

## Dépendances clés
- Dépend de : Codeception, `SuiteCRM/Test/`
- Utilisé par : toutes les suites de tests (`acceptance/`, `api/`, `unit/`)

## Notes
Structure générée par Codeception (`build`) + code custom. Les fichiers `*Tester.php` sont régénérés automatiquement — ne pas modifier manuellement.
