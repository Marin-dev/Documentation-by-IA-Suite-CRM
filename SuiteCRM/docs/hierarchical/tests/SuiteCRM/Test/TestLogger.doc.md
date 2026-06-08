# TestLogger.php (helper / double de test)

**Chemin :** `tests/SuiteCRM/Test/TestLogger.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Implémentation factice du logger SuiteCRM (substitut de `LoggerManager`). Capture tous les appels de log (fatal, error, warn, info, debug…) en mémoire pour permettre aux tests unitaires de vérifier qu'un log précis a bien été déclenché.

## Type
helper / double de test (test double / spy)

## Dependances cles
- Aucune dépendance externe (classe autonome)

## Scenarios couverts
- Tout appel dynamique via `__call()` est capturé dans `$this->calls[niveau][]` et `$this->notes[]`
- `getNotes($levels)` : filtre les entrées capturées par niveau (ex: `'fatal'`, `'error,warn'`)
- `reset()` : réinitialise les tableaux entre les tests

## Notes
- Injecté dans `$GLOBALS['log']` par `SuitePHPUnitFrameworkTestCase::setUp()`.
- Le `__call` magique permet de gérer n'importe quel niveau de log sans interface formelle.
- Les tests vérifient typiquement `$GLOBALS['log']->calls['fatal']` pour s'assurer qu'une erreur a été loggée.
- Namespace : `SuiteCRM\Test`.
