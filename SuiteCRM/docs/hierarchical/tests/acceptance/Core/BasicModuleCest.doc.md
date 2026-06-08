# BasicModuleCest.php (acceptance-test)

**Chemin :** `tests/acceptance/Core/BasicModuleCest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Tests d'acceptance couvrant le cycle de vie complet d'un module de type "Basic" créé via le Module Builder : création du module, vue liste, création/édition/duplication/suppression d'enregistrement.

## Type
acceptance-test

## Dependances cles
- `AcceptanceTester`, `Step\Acceptance\ModuleBuilder`, `Step\Acceptance\Repair`, `Step\Acceptance\NavigationBarTester`, `Step\Acceptance\ListView`, `Step\Acceptance\EditView`, `Step\Acceptance\DetailView`
- `SuiteCRM\Enumerator\SugarObjectType`
- `Faker\Factory`
- `Page\BasicModule`
- Framework : Codeception + WebDriver

## Scenarios couverts
- `testScenarioCreateBasicModule` : création du module `BasicTestModule` via ModuleBuilder + Quick Repair & Rebuild
- `testScenarioViewBasicTestModule` : navigation vers le module et vérification de la liste
- `testScenarioCreateRecord` : création d'un enregistrement avec nom et description
- `testScenarioViewRecordFromListView` : recherche et affichage d'un enregistrement depuis la liste
- `testScenarioEditRecordFromDetailView` : édition d'un enregistrement depuis la vue détail
- `testScenarioDuplicateRecordFromDetailView` : duplication d'un enregistrement
- `testScenarioDeleteRecordFromDetailView` : suppression d'un enregistrement

## Notes
- Les tests sont ordonnés et dépendants : le module doit exister (créé par le premier test) pour les suivants.
- Le nettoyage du module est géré par `Helper\Acceptance::_beforeSuite()` / `_afterSuite()`.
- Utilise le seed Faker pour retrouver les mêmes données dans les tests de suite.
