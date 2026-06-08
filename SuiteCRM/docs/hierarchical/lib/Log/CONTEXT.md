# Log

## Rôle
Ce dossier contient les handlers et formateurs de log personnalisés de SuiteCRM pour Monolog. Il fournit l'intégration entre le système de logging Monolog (utilisé dans l'indexation Search et l'API) et les deux sorties de log de SuiteCRM : le fichier SugarLog natif et la sortie terminal colorée (CLI). Ces composants sont utilisés notamment par `AbstractIndexer` pour le logging de l'indexation.

## Contenu
| Fichier | Rôle |
|---|---|
| `CliLoggerFormatter.php` | Formateur Monolog — sortie colorée ANSI pour terminal |
| `CliLoggerHandler.php` | Handler Monolog — envoie les logs vers stdout (CLI) avec formatage ANSI |
| `SugarLoggerHandler.php` | Handler Monolog — envoie les logs vers SugarLogger (fichier log SuiteCRM natif) |

## Points d'entrée
- `SugarLoggerHandler.php` — handler principal pour les logs en production
- `CliLoggerHandler.php` — handler pour les commandes Robo/CLI

## Dépendances clés
- **Dépend de :** `Monolog\Handler\AbstractHandler`, `Monolog\Formatter\FormatterInterface`, `SugarLogger` (global SuiteCRM)
- **Utilisé par :** `lib/Search/Index/AbstractIndexer.php` (triple handler), commandes Robo

## Notes
- `CliLoggerFormatter::formatBatch()` retourne seulement le dernier record — comportement potentiellement incorrect.
- `$alwaysColourLine = true` dans `CliLoggerFormatter` — couleurs forcées même sous WARNING.
- Requiert un terminal ANSI compatible pour les couleurs CLI.
