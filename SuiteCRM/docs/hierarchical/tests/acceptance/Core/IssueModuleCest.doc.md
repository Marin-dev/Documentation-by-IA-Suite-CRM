# IssueModuleCest.php (acceptance-test)

**Chemin :** `tests/acceptance/Core/IssueModuleCest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role

Tests d'acceptance pour un module de type "Issue" créé via le Module Builder.

## Type

acceptance-test

## Dependances cles

- `AcceptanceTester`, steps acceptance standard, `Page\IssueModule`
- `SuiteCRM\Enumerator\SugarObjectType::issue`
- Framework : Codeception + WebDriver

## Scenarios couverts

- Création du module Issue, CRUD d'enregistrements (pattern identique à BasicModuleCest)

## Notes

- Type `issue` : module de suivi de tickets/incidents.
