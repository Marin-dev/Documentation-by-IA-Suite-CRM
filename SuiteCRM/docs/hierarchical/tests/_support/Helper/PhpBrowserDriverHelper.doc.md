# PhpBrowserDriverHelper.php (helper Codeception)

**Chemin :** `tests/_support/Helper/PhpBrowserDriverHelper.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Equivalent de `WebDriverHelper` pour le driver PhpBrowser (tests sans navigateur réel). Fournit les mêmes méthodes d'accès aux variables d'environnement mais via le module `PhpBrowser` de Codeception. Utilisé principalement dans la suite API.

## Type
helper Codeception (API / acceptance sans navigateur)

## Dependances cles
- `Codeception\Module` — classe parente
- Module `PhpBrowser` de Codeception — source de config
- `SuiteCRM\Enumerator\DatabaseDriver`

## Variables d'environnement utilisees
| Variable | Defaut | Methode |
|---|---|---|
| `INSTANCE_URL` | `http://localhost` | `getInstanceURL()` |
| `DATABASE_DRIVER` | `MYSQL` | `getDatabaseDriver()` |
| `DATABASE_NAME` | `automated_tests` | `getDatabaseName()` |
| `DATABASE_HOST` | `database_host` | `getDatabaseHost()` |
| `DATABASE_USER` | `automated_tests` | `getDatabaseUser()` |
| `DATABASE_PASSWORD` | `automated_tests` | `getDatabasePassword()` |
| `INSTANCE_ADMIN_USER` | `admin` | `getAdminUser()` |
| `INSTANCE_ADMIN_PASSWORD` | `admin` | `getAdminPassword()` |
| `INSTANCE_CLIENT_ID` | `API-4c59-f678-cecc-6594-5a8d9c704473` | `getPasswordGrantClientId()` |
| `INSTANCE_CLIENT_SECRET` | `secret` | `getPasswordGrantClientSecret()` |
| `INSTANCE_CREDENTIALS_CLIENT_ID` | `API-ea74-c352-badd-c2be-5a8d9c9d4351` | `getClientCredentialsGrantClientId()` |
| `INSTANCE_CREDENTIALS_CLIENT_SECRET` | `secret` | `getClientCredentialsGrantClientSecret()` |

## Notes
- Bug dans `getEnvironmentVariableOrDefault()` ligne 229 : `$lowerCase = strtoupper($variable)` devrait être `strtolower`. La clé de config YAML est lue en uppercase, ce qui peut empêcher la lecture depuis le YAML.
- Namespace : `Helper`.
