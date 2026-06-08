# acceptance

## Rôle
Suite de tests d'acceptation SuiteCRM via Codeception. Teste l'application de bout en bout depuis l'interface utilisateur (navigateur), couvrant les scénarios de connexion, les templates de modules Core, et l'ensemble des modules métier. Ces tests valident le comportement fonctionnel visible par l'utilisateur final.

## Contenu
| Fichier / Dossier | Rôle |
|---|---|
| `_bootstrap.php` | Bootstrap de la suite d'acceptation — initialisation Codeception |
| `LoginCest.php` | Tests d'acceptation du login/authentification SuiteCRM |
| `Core/` | Tests des templates de modules (Basic, Company, File, Issue, Person, Sale) + ModuleBuilder |
| `modules/` | Tests par module SuiteCRM (35 modules couverts) |

## Points d'entrée
- `_bootstrap.php` — chargé automatiquement par Codeception avant la suite
- `LoginCest.php` — premier test à faire passer (prérequis d'authentification)

## Dépendances clés
- Dépend de : `AcceptanceTester`, `_support/`, `_support/Helper/Acceptance.php`, SuiteCRM déployé
- Utilisé par : pipeline CI/CD, tests de régression UI

## Notes
Nécessite un SuiteCRM opérationnel avec base de données. Supporte WebDriver (Selenium) et PhpBrowser selon la configuration Codeception.
