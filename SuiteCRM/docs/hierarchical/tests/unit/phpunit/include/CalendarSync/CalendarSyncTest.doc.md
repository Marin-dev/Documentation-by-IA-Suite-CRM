# CalendarSyncTest.php (unit-test)

**Chemin :** `tests/unit/phpunit/include/CalendarSync/CalendarSyncTest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Suite de tests unitaires couvrant la classe `CalendarSync`. Tests organisés en deux catégories : tests techniques/infrastructure (patterns architecturaux, gestion d'erreurs) et tests de logique métier (règles domaine, workflows).

## Type
unit-test

## Dependances cles
- `SuitePHPUnitFrameworkTestCase` — classe de base
- `CalendarSync` — classe testée (`include/CalendarSync/CalendarSync.php`)
- TestDoubles dans `TestDoubles/` : `FakeCalendarAccountEventFactory`, `FakeCalendarProviderRegistry`, `FakeCalendarSyncJobCleaner`, `FakeCalendarSyncJobFactory`, `FakeCalendarSyncOrchestrator`, `InMemoryCalendarAccountRepository`, `InMemoryCalendarAccountValidator`, `InMemoryCalendarSyncConfig`
- Framework : PHPUnit

## Scenarios couverts
- Pattern Singleton : vérifie qu'une seule instance de `CalendarSync` existe
- Tests de logique métier CalendarSync (détails des cas individuels : INCONNU sans lecture complète du fichier)

## Notes
- Organisation explicite en deux sections dans le code : infrastructure tests vs business logic tests.
- Les doubles de test `InMemory*` permettent des tests sans dépendance DB.
- Fichier récent (copyright 2025 SuiteCRM Ltd vs 2021 pour les autres).
