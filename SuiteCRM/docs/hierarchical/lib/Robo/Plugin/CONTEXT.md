# Plugin

## Rôle
Ce dossier contient le plugin Robo de SuiteCRM. Il héberge les classes de commandes CLI organisées dans le sous-dossier `Commands/`. Ces commandes couvrent la gestion de l'API, le build, le cache, les tests, ElasticSearch, la réparation et la mise à jour de SuiteCRM. Ce dossier suit la convention de structure des plugins Robo (`Plugin/Commands/`).

## Contenu
| Dossier | Rôle |
|---|---|
| `Commands/` | Classes de commandes Robo (API, Build, Cache, Tests, ES, Repair, Upgrade, etc.) |

## Points d'entrée
- `Commands/ApiCommands.php` — commandes de configuration de l'API V8
- `Commands/TestRunCommands.php` — lancement des suites de tests

## Dépendances clés
- **Dépend de :** `lib/Robo/Traits/`, framework Robo
- **Utilisé par :** CLI Robo (`./vendor/bin/robo`), `lib/Robo/config.php`

## Notes
- Ce dossier suit la convention de plugin Robo — les commandes sont auto-découvertes via la configuration Robo.
