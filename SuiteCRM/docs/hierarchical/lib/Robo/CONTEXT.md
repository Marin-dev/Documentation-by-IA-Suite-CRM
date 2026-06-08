# Robo

## Rôle
Ce dossier contient l'infrastructure des tâches Robo CLI de SuiteCRM. Il fournit le fichier de bootstrap de configuration (`config.php`), les traits utilitaires partagés (`Traits/`) et le plugin Robo contenant toutes les commandes CLI (`Plugin/Commands/`). Robo est utilisé pour automatiser les opérations de développement, de maintenance et de déploiement de SuiteCRM.

## Contenu
| Fichier/Dossier | Rôle |
|---|---|
| `config.php` | Bootstrap de la configuration SuiteCRM pour les tâches Robo (charge `$GLOBALS['sugar_config']`) |
| `Traits/` | Traits utilitaires : prompts interactifs, lecture config, exécution shell |
| `Plugin/` | Plugin Robo — classes de commandes CLI (API, Build, Cache, Tests, ES, Repair, Upgrade) |

## Points d'entrée
- `./vendor/bin/robo api:configure-v8` — configuration initiale de l'API V8
- `./vendor/bin/robo es:index` — indexation ElasticSearch
- `./vendor/bin/robo test:run` — lancement des tests

## Dépendances clés
- **Dépend de :** framework `robo/robo`, `Api\Core\Config\ApiConfig`, `Api\V8\BeanDecorator\BeanManager`, `DBManagerFactory`, `SugarConfig`
- **Utilisé par :** CLI via `./vendor/bin/robo`

## Notes
- `config.php` charge `$GLOBALS['sugar_config']` — nécessite les fichiers `config.php` et `config_override.php` à la racine SuiteCRM.
- Toutes les commandes interagissant avec la BD nécessitent un bootstrap SuiteCRM préalable.
