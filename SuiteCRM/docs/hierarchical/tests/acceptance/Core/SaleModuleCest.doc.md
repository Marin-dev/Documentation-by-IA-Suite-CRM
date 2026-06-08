# SaleModuleCest.php (acceptance-test)

**Chemin :** `tests/acceptance/Core/SaleModuleCest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role

Tests d'acceptance pour un module de type "Sale" créé via le Module Builder.

## Type

acceptance-test

## Dependances cles

- `AcceptanceTester`, steps acceptance standard, `Page\SaleModule`
- `SuiteCRM\Enumerator\SugarObjectType::sale`
- Framework : Codeception + WebDriver

## Scenarios couverts

- Création du module Sale, CRUD d'enregistrements (pattern identique à BasicModuleCest)

## Notes

- Type `sale` : module orienté vente avec champs montant/devise.
