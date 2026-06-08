# LoginCest.php (acceptance-test)

**Chemin :** `tests/acceptance/LoginCest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Test d'acceptance minimal vérifiant que la connexion en tant qu'administrateur est fonctionnelle.

## Type
acceptance-test

## Dependances cles
- `AcceptanceTester` — acteur Codeception
- Framework : Codeception

## Scenarios couverts
- `testScenarioLoginAsAdministrator` : connexion en tant qu'administrateur via `loginAsAdmin()`

## Notes
- Test extrêmement minimal — ne vérifie pas ce qui est affiché après connexion.
- Sert de smoke test pour la disponibilité de l'instance SuiteCRM.
