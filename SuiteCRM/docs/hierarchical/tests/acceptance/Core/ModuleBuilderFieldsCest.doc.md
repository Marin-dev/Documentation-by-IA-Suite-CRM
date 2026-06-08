# ModuleBuilderFieldsCest.php (acceptance-test)

**Chemin :** `tests/acceptance/Core/ModuleBuilderFieldsCest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Tests d'acceptance couvrant la création de champs personnalisés (relate, HTML, integer) dans le Module Builder et leur ajout au layout EditView via drag-and-drop, puis le déploiement du module et la relation vers le module Accounts.

## Type
acceptance-test

## Dependances cles
- `AcceptanceTester`, `Step\Acceptance\ModuleBuilder`, `Step\Acceptance\Repair`, `Step\Acceptance\NavigationBarTester`, `Step\Acceptance\ListView`, `Step\Acceptance\EditView`, `Step\Acceptance\DetailView`, `Step\Acceptance\Accounts`
- `SuiteCRM\Enumerator\SugarObjectType`
- `Faker\Factory`
- `Page\ModuleFields`, `Page\AccountsModule`
- Framework : Codeception + WebDriver

## Scenarios couverts
- `testScenarioCreateFieldsModule` : création du module `TestModuleFields` via ModuleBuilder
- `testScenarioAddRelateField` : ajout d'un champ `relate` vers Accounts, drag-and-drop dans le layout EditView
- `testScenarioAddHtmlField` : ajout d'un champ HTML, drag-and-drop dans le layout
- `testScenarioAddIntField` : ajout d'un champ Integer, drag-and-drop dans le layout
- `testScenarioDeployModule` : déploiement du package (2 fois) + Quick Repair & Rebuild
- `testScenarioRelateToAccounts` : **désactivé** (`return;` en ligne 372) — test de relation avec Accounts marqué comme instable selon environnement

## Notes
- Le drag-and-drop (`dragAndDrop`) est sensible aux navigateurs et aux timings WebDriver.
- `testScenarioRelateToAccounts` est désactivé avec un commentaire explicite.
- Deux TODO non implémentés dans `configureInstaller` (lignes 139-140 d'`InstallTester`).
