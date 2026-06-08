# PersonModuleCest.php (acceptance-test)

**Chemin :** `tests/acceptance/Core/PersonModuleCest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role

Tests d'acceptance pour un module de type "Person" créé via le Module Builder.

## Type

acceptance-test

## Dependances cles

- `AcceptanceTester`, steps acceptance standard, `Page\PersonModule`
- `SuiteCRM\Enumerator\SugarObjectType::person`
- Framework : Codeception + WebDriver

## Scenarios couverts

- Création du module Person, CRUD d'enregistrements (pattern identique à BasicModuleCest)

## Notes

- Type `person` : module avec champs prénom/nom/email typiques d'une personne.
