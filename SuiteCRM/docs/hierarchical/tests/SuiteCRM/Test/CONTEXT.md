# Test

## Rôle
Infrastructure de test de base pour SuiteCRM. Fournit les classes fondamentales dont héritent les tests PHPUnit (cas de test de base, cas de test BeanFactory), un logger de test, et les drivers de navigation pour les tests d'acceptation.

## Contenu
| Fichier / Dossier | Rôle |
|---|---|
| `SuitePHPUnitFrameworkTestCase.php` | Classe de base PHPUnit pour tous les tests SuiteCRM — setup/teardown global |
| `BeanFactoryTestCase.php` | Cas de test spécialisé pour les tests impliquant BeanFactory |
| `TestLogger.php` | Logger de test — capture les logs pour assertions dans les tests |
| `Driver/` | Drivers de navigation (WebDriver, PhpBrowserDriver) pour tests d'acceptation |

## Points d'entrée
- `SuitePHPUnitFrameworkTestCase` — classe parente de tous les tests unitaires SuiteCRM

## Dépendances clés
- Dépend de : PHPUnit, Codeception, `SuiteCRM/Enumerator/`
- Utilisé par : tous les tests unitaires et d'acceptation du projet

## Notes
Point central de l'infrastructure de test — tout test SuiteCRM passe par ces classes de base.
