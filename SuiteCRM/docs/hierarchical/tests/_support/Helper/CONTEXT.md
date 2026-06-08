# Helper

## Rôle
Helpers Codeception pour les différentes suites de tests SuiteCRM. Fournit les classes de configuration et d'extension de chaque suite (Acceptance, API, Unit, Install) ainsi que des helpers spécialisés pour la navigation WebDriver et PhpBrowser.

## Contenu
| Fichier | Rôle |
|---|---|
| `Acceptance.php` | Helper de la suite d'acceptation — configuration et méthodes communes |
| `WebDriverHelper.php` | Helper spécialisé WebDriver — actions avancées pour tests en navigateur réel |
| `PhpBrowserDriverHelper.php` | Helper spécialisé PhpBrowser — actions pour tests sans navigateur |
| `Unit.php` | Helper de la suite unitaire — setup commun pour les tests PHPUnit |
| `Install.php` | Helper de la suite d'installation — scénarios d'installation SuiteCRM |
| `api.php` | Helper de la suite API — configuration et authentification pour tests API |

## Points d'entrée
Chaque helper est déclaré dans le fichier de configuration Codeception de sa suite.

## Dépendances clés
- Dépend de : Codeception, `SuiteCRM/Test/Driver/`
- Utilisé par : suites `acceptance/`, `api/`, `unit/`, `install/` via Codeception

## Notes
Pattern standard Codeception — un helper par suite pour étendre les acteurs de test.
