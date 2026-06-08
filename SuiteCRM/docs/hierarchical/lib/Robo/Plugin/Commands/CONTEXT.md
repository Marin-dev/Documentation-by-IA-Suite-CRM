# Commands

## Rôle
Ce dossier contient les commandes Robo CLI de SuiteCRM. Ces commandes permettent d'automatiser les opérations de maintenance, de build, de test et de gestion de l'API V8 depuis la ligne de commande. Elles sont invocables via `./vendor/bin/robo` et couvrent des domaines variés : API, build, cache, couverture de code, standards de codage, ElasticSearch, réparation, tests et mise à jour.

## Contenu
| Fichier | Rôle |
|---|---|
| `ApiCommands.php` | Configuration et gestion de l'API V8 (clés OAuth2, clients, utilisateurs, .htaccess, export Postman) |
| `BuildCommands.php` | Commandes de build du projet |
| `CleanCacheCommands.php` | Nettoyage du cache SuiteCRM |
| `CodeCoverageCommands.php` | Génération de rapports de couverture de code |
| `CodingStandardCommands.php` | Vérification et correction des standards de codage (PHPCS) |
| `ElasticSearchCommands.php` | Gestion des index ElasticSearch (création, réindexation, suppression) |
| `RepairCommands.php` | Commandes de réparation SuiteCRM (Quick Repair & Rebuild) |
| `TestEnvironmentCommands.php` | Configuration de l'environnement de test |
| `TestRunCommands.php` | Lancement des suites de tests (unitaires, fonctionnels, acceptance) |
| `UpgradeCommands.php` | Gestion des mises à jour SuiteCRM |

## Points d'entrée
- `ApiCommands.php` — `./vendor/bin/robo api:configure-v8` — configuration initiale de l'API V8
- `ElasticSearchCommands.php` — `./vendor/bin/robo es:*` — gestion des index ES

## Dépendances clés
- **Dépend de :** `Robo\Tasks`, `lib/Robo/Traits/RoboTrait`, `lib/Robo/Traits/CliRunnerTrait`, `Api\Core\Config\ApiConfig`, `Api\V8\BeanDecorator\BeanManager`, `DBManagerFactory`
- **Utilisé par :** CLI Robo (`./vendor/bin/robo`)

## Notes
- `ApiCommands::apiCreateUser()` crée un utilisateur avec email `API@example.com` en dur — à adapter.
- `ApiCommands::apiGenerateKeys()` écrit les clés RSA OAuth2 directement sur le filesystem.
- Toutes les commandes qui interagissent avec SuiteCRM requièrent une connexion BD via `bootstrap()`.
