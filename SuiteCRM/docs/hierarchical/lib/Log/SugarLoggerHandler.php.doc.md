# SugarLoggerHandler.php

**Chemin :** `lib/Log/SugarLoggerHandler.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Pont entre Monolog (PSR-3) et le systeme de logging historique de SugarCRM (`LoggerManager`). Permet aux composants utilisant Monolog d'ecrire dans les logs SuiteCRM habituels.

## Role technique
Etend `Monolog\Handler\AbstractProcessingHandler`. La methode `write()` extrait le message, le niveau et le canal depuis le record Monolog, convertit le niveau via `psrToSugarLevel()`, puis appelle dynamiquement la methode correspondante sur `LoggerManager::getLogger()` (ex. `$logger->debug(...)`, `$logger->fatal(...)`).

---

## Dependances cles
- `LoggerManager` — logger natif SugarCRM (global)
- `Monolog\Handler\AbstractProcessingHandler`
- `Monolog\LogRecord`

## Exports / Symboles principaux
- `SugarLoggerHandler` — classe handler Monolog
  - `write(array|LogRecord $record): void`
  - `psrToSugarLevel(int $level): string` (protected) — convertit 100->debug, 200->info, 300->warn, 400->error, 500/550/600->security/fatal

- **Consommateurs identifies :**
  - `lib/Search/Index/AbstractIndexer.php` (ligne 297)

## Relations cles
- **Appele par :** `AbstractIndexer::setupLogger()`
- **Appelle :** `LoggerManager::getLogger()`
- **Position dans le flux global :** pont de logging lors des operations d'indexation

---

## Points d'attention
- La conversion PSR vers Sugar n'est pas exhaustive (niveaux 550 et 600 -> `security`).
- `php://stderr` n'est pas utilise ici : les logs vont dans le fichier SuiteCRM habituel.
