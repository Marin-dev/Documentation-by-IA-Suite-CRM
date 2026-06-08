# Traits

## Rôle
Ce dossier contient les traits utilitaires partagés entre les commandes Robo de SuiteCRM. `RoboTrait` fournit des helpers de prompts interactifs et d'accès à la configuration ; `CliRunnerTrait` encapsule l'exécution de commandes shell via Robo. Ces traits évitent la duplication de code dans les classes de commandes.

## Contenu
| Fichier | Rôle |
|---|---|
| `RoboTrait.php` | Helpers de prompts interactifs et lecture de configuration SuiteCRM |
| `CliRunnerTrait.php` | Exécution de commandes shell depuis les tâches Robo |

## Points d'entrée
- `RoboTrait.php` — utilisé par la majorité des commandes Robo

## Dépendances clés
- **Dépend de :** `lib/Robo/config.php`, `SugarConfig` (singleton SuiteCRM), `Robo\Tasks`
- **Utilisé par :** `lib/Robo/Plugin/Commands/` — quasiment toutes les classes de commandes

## Notes
- `RoboTrait` inclut `config.php` au niveau fichier — effet de bord possible hors contexte Robo.
- `chooseConfigOrDefault()` lit la configuration via `SugarConfig::getInstance()->get()` — nécessite SuiteCRM bootstrappé.
