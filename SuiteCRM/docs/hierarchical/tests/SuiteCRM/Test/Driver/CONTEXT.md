# Driver

## Rôle
Drivers de navigation pour les tests d'acceptation SuiteCRM. Fournit les implémentations concrètes de pilotage de navigateur (WebDriver Selenium et PhpBrowser Codeception) utilisées dans les tests end-to-end.

## Contenu
| Fichier | Rôle |
|---|---|
| `WebDriver.php` | Driver Selenium WebDriver pour tests en navigateur réel |
| `PhpBrowserDriver.php` | Driver PhpBrowser Codeception pour tests sans navigateur (plus rapides) |

## Points d'entrée
- `WebDriver` — utilisé pour les tests d'acceptation nécessitant JavaScript
- `PhpBrowserDriver` — utilisé pour les tests d'acceptation simples sans JS

## Dépendances clés
- Dépend de : Codeception, Selenium WebDriver
- Utilisé par : `SuiteCRM/Test/`, suites d'acceptation

## Notes
Abstraction du choix de driver — permet de switcher entre navigateur réel et simulation HTTP selon le besoin.
