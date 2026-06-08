# MigrationRegistry.php

**Chemin :** `include/CalendarSync/migrations/Services/MigrationRegistry.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Service de suivi de l'etat d'execution des migrations CalendarSync. Stocke un marqueur dans la table `config` (categorie `'migrations'`) pour chaque migration executee, permettant de detecter si une migration a deja ete jouee et d'eviter les executions multiples.

## Role technique

Utilise `DBManager` directement via `DBManagerFactory::getInstance()`. La detection utilise `SELECT COUNT(*)` sur la table `config`. L'enregistrement utilise `INSERT IGNORE` (idempotent, protege contre les race conditions en environnement multi-serveurs).

---

## Dependances cles

- **Imports principaux :**
  - `DBManagerFactory` — acces a la base de donnees
  - `LoggerManager` — logging

## Exports / Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `MigrationRegistry` | classe service | Suivi des migrations |
| `MIGRATION_CATEGORY` | constante `'migrations'` | Categorie config BDD |
| `GOOGLE_CALENDAR_SYNC_MIGRATION` | constante | ID de la migration Google |
| `CALENDAR_SYNC_HOOKS_INSTALLATION` | constante | ID de la migration hooks |
| `hasMigrationRun(string): bool` | methode | Verifie si migration executee |
| `recordMigrationCompletion(string): void` | methode | Enregistre la completion |

- **Consommateurs identifies :** `LegacyGoogleSyncMigrationService`, `SchedulerMigrationService` et autres services de migration (INCONNU — chercher `MigrationRegistry` dans le dossier migrations)

## Relations cles

- **Appele par :** services de migration (`include/CalendarSync/migrations/Services/`)
- **Appelle :** `DBManagerFactory::getInstance()`
- **Position dans le flux global :** registre de controle d'idempotence pour les migrations

---

## Points d'attention

- `hasMigrationRun()` retourne `false` en cas d'exception (comportement conservateur : re-execution possible). Surveiller les erreurs BDD.
- `recordMigrationCompletion()` lance une `RuntimeException` si l'insertion echoue — la migration devra etre rejouee.
- Utilise `INSERT IGNORE` : sur bases sans support (rare), le comportement peut differ.
