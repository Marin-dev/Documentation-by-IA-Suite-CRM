# FileModuleCest.php (acceptance-test)

**Chemin :** `tests/acceptance/Core/FileModuleCest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role

Tests d'acceptance pour un module de type "File" créé via le Module Builder.

## Type

acceptance-test

## Dependances cles

- `AcceptanceTester`, steps acceptance standard, `Page\FileModule`
- `SuiteCRM\Enumerator\SugarObjectType::file`
- Framework : Codeception + WebDriver

## Scenarios couverts

- Création du module File, CRUD d'enregistrements (pattern identique à BasicModuleCest)

## Notes

- Type `file` dans SugarObjectType : module avec gestion de fichiers attachés.
