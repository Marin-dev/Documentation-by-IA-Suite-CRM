# Acceptance.php (helper Codeception)

**Chemin :** `tests/_support/Helper/Acceptance.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Module Codeception de support pour la suite acceptance. Assure le nettoyage des fichiers et dossiers créés par les tests du Module Builder avant et après chaque suite, et expose un helper `seePageHas()` pour les vérifications conditionnelles de contenu.

## Type
helper Codeception (acceptance)

## Dependances cles
- `Codeception\Module` — classe parente
- `SuiteCRM\Test\Driver\WebDriver` — pour appel à `see()`
- `PHPUnit\Framework\AssertionFailedError`

## Scenarios couverts
- `seePageHas($text, $selector)` : retourne `bool` au lieu de lever une exception
- `_beforeSuite()` / `_afterSuite()` : nettoyage des modules de test (`BasicTestModule`, `CompanyTestModule`, `FileTestModule`, `IssueTestModule`, `PersonTestModule`, `SaleTestModule`, `TestModuleFields`)
- `deleteModuleFiles($module)` : supprime les répertoires `custom/modulebuilder/builds/`, `custom/modulebuilder/packages/`, `modules/Test_{module}` et les fichiers d'extension associés

## Notes
- Le nettoyage est fait AVANT et APRES la suite pour gérer les interruptions de tests.
- Namespace : `Helper`.
