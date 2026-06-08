# WebDriverHelper.php (helper Codeception)

**Chemin :** `tests/_support/Helper/WebDriverHelper.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Module Codeception fournissant l'accès aux variables de configuration d'environnement pour les tests acceptance via WebDriver. Chaque méthode lit d'abord la variable d'environnement correspondante, puis fallback sur la config YAML du module WebDriver.

## Type
helper Codeception (acceptance)

## Dependances cles
- `Codeception\Module` — classe parente
- `SuiteCRM\Test\Driver\WebDriver` — source de configuration YAML
- `SuiteCRM\Enumerator\DatabaseDriver` — valeur par défaut du driver

## Variables d'environnement utilisees
| Variable | Defaut | Methode |
|---|---|---|
| `INSTANCE_URL` | `http://localhost/` | `getInstanceURL()` |
| `DATABASE_DRIVER` | `MYSQL` | `getDatabaseDriver()` |
| `DATABASE_NAME` | `automated_tests` | `getDatabaseName()` |
| `DATABASE_HOST` | `localhost` | `getDatabaseHost()` |
| `DATABASE_USER` | `automated_tests` | `getDatabaseUser()` |
| `DATABASE_PASSWORD` | `automated_tests` | `getDatabasePassword()` |
| `INSTANCE_ADMIN_USER` | `admin` | `getAdminUser()` |
| `INSTANCE_ADMIN_PASSWORD` | `admin` | `getAdminPassword()` |
| `INSTANCE_ELASTIC_SEARCH_HOST` | `localhost` | `getElasticSearchHost()` |
| `BROWSERSTACK_USERNAME` | `''` | `getBrowserStackUsername()` |
| `BROWSERSTACK_ACCESS_KEY` | `''` | `getBrowserStackAccessKey()` |
| `BROWSERSTACK_LOCAL_FOLDER_URL` | `''` | `getBrowserStackLocalFolderURL()` |

## Notes
- Bug potentiel dans `getAdminUser()` : utilise `INSTANCE_ADMIN_USER` comme nom de variable pour `$envDatabasePassword` (copier-coller) mais le comportement final est correct.
- Consommé par `InstallTester` et les steps d'acceptance nécessitant un accès DB.
- Namespace : `Helper`.
