# SuiteLogger.php

**Chemin :** `lib/Utility/SuiteLogger.php`
**Type :** PHP — Service (adaptateur de log PSR-3)
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Logger PSR-3 pour SuiteCRM. Adaptateur entre l'interface PSR-3 (`AbstractLogger`) et le systeme de log interne `LoggerManager`. Supporte l'interpolation des variables dans les messages via `{key}` placeholders.

## Role technique
Etend `Psr\Log\AbstractLogger`. Methode `log()` mappe chaque niveau PSR-3 vers la methode correspondante de `LoggerManager::getLogger()` (debug, info, warn, fatal, security). Note : les niveaux ERROR/CRITICAL/ALERT/EMERGENCY -> `$log->fatal()`.

---

## Dependances cles
- `Psr\Log\{AbstractLogger, LogLevel, InvalidArgumentException}`
- `LoggerManager` (global SuiteCRM)

## Exports / Symboles principaux
- `SuiteLogger` — classe PSR-3 logger
  - `log($level, $message, array $context = []): void`

- **Consommateurs identifies :**
  - `lib/Search/UI/SearchThrowableHandler.php`
  - `lib/Utility/AntiMalware/FileScanner.php`
  - `lib/Search/ElasticSearch/ElasticSearchHooks.php`
  - `lib/Search/Index/AbstractIndexer.php`

---

## Points d'attention
- Les niveaux EMERGENCY, ALERT, CRITICAL, ERROR sont tous routes vers `$log->fatal()` — perte de granularite.
- `$log->warn()` pour WARNING et NOTICE — idem.
- Si `$level` est invalide : leve `Psr\Log\InvalidArgumentException` (ligne 102).
