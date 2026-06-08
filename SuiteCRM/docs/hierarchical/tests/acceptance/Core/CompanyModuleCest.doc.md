# CompanyModuleCest.php (acceptance-test)

**Chemin :** `tests/acceptance/Core/CompanyModuleCest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role

Tests d'acceptance couvrant le cycle de vie complet d'un module de type "Company" créé via le Module Builder : création, vue, CRUD d'enregistrements.

## Type

acceptance-test

## Dependances cles

- `AcceptanceTester`, `Step\Acceptance\ModuleBuilder`, `Step\Acceptance\Repair`, `Step\Acceptance\NavigationBarTester`, `Step\Acceptance\ListView`, `Step\Acceptance\EditView`, `Step\Acceptance\DetailView`
- `SuiteCRM\Enumerator\SugarObjectType::company`
- `Page\CompanyModule`
- Framework : Codeception + WebDriver

## Scenarios couverts

- Création du module Company via ModuleBuilder + Repair
- Vue liste, création, édition, duplication, suppression d'enregistrement

## Notes

- Pattern identique à `BasicModuleCest` mais pour le type `company`.
- Nettoyage géré par `Helper\Acceptance`.
