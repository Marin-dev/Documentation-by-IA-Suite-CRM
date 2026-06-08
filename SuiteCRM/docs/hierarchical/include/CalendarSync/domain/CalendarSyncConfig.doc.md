# CalendarSyncConfig.php

**Chemin :** `include/CalendarSync/domain/CalendarSyncConfig.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Service de gestion de la configuration du module CalendarSync. Lit les valeurs depuis la configuration globale Sugar (`sugar_config['calendar_sync']`), fournit des valeurs par defaut robustes, et persiste les modifications via le `Configurator` de SuiteCRM.

## Role technique

Implements `CalendarSyncConfigInterface`. Utilise `SugarConfig::getInstance()` pour lire la config globale. La persistance passe par `Configurator::saveConfig()` et invalide le cache apres ecriture. Chaque getter valide le type (bool, int, string) avec repli sur les constantes `DEFAULTS`.

---

## Dependances cles

- **Imports principaux :**
  - `ConflictResolution` (enum) — validation de la strategie configuree
  - `CalendarSyncConfigInterface` — interface implementee
  - `SugarConfig` — lecture de `$GLOBALS['sugar_config']`
  - `Configurator` (modules/Configurator) — ecriture en base/fichier

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `CalendarSyncConfig` | classe service | Gestionnaire de configuration |
| `CONFIG_KEY` | constante `'calendar_sync'` | Cle dans sugar_config |
| `DEFAULTS` | constante tableau | Valeurs par defaut |
| `getRunAsyncValue(): bool` | methode | Mode async (defaut: false) |
| `getMaxAccountsPerSync(): int` | methode | Limite de comptes par run (defaut: 30) |
| `getMaxOperationsPerAccount(): int` | methode | Limite d'operations par compte (defaut: 100) |
| `getSyncWindowPastDays(): int` | methode | Jours passes dans la fenetre (defaut: 30) |
| `getSyncWindowFutureDays(): int` | methode | Jours futurs dans la fenetre (defaut: 90) |
| `getConflictResolution(): string` | methode | Strategie de conflit (defaut: 'timestamp') |
| `allowInternalEventDeletion(): bool` | methode | Autoriser suppression interne (defaut: true) |
| `allowExternalEventDeletion(): bool` | methode | Autoriser suppression externe (defaut: true) |
| `enableCalendarSyncLogicHooks(): bool` | methode | Activer hooks logiques (defaut: false) |
| `set(array): bool` | methode | Persiste la configuration |

- **Consommateurs identifies :** `CalendarSync`, `CalendarSyncOrchestrator`, `CalendarSyncOperationDiscovery`, `AbstractCalendarProvider`

## Relations cles

- **Appele par :** toutes les couches de CalendarSync
- **Appelle :** `SugarConfig`, `Configurator`
- **Position dans le flux global :** source de verite de la configuration — consulte a chaque run

---

## Points d'attention

- `enable_calendar_sync_logic_hooks` est `false` par defaut — les synchronisations depuis les logic hooks (save de Meeting) sont inactives sans configuration explicite.
- `set()` convertit toutes les valeurs en string avant persistance (ligne 104) — les booleens `true`/`false` deviennent `'1'`/`''`, ce qui peut interagir avec `filter_var(FILTER_VALIDATE_BOOLEAN)` lors de la relecture.
- `getConflictResolution()` valide via `ConflictResolution::tryFrom()` — toute valeur inconnue est silencieusement remplacee par `'timestamp'`.
