# AccountsCest.php (acceptance-test)

**Chemin :** `tests/acceptance/modules/Accounts/AccountsCest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Tests d'acceptance couvrant les opérations CRUD et l'édition inline sur le module Accounts de SuiteCRM.

## Type
acceptance-test

## Dependances cles
- `AcceptanceTester`, `Step\Acceptance\ListView`, `Step\Acceptance\DetailView`, `Step\Acceptance\EditView`, `Step\Acceptance\SideBar`, `Step\Acceptance\Accounts`
- `Faker\Factory` — génération de données aléatoires
- Framework : Codeception + WebDriver

## Scenarios couverts
- `testScenarioViewAccountsModule` : navigation vers la liste des comptes, vérification du titre
- `testScenarioCreateAccount` : création d'un compte avec tous les champs principaux (nom, téléphone, site web, email, adresse, type, secteur), suppression ensuite
- `testScenarioInlineEditListView` : création d'un compte puis édition inline du nom depuis la liste
- `testScenarioCreateAccountChild` : création d'un compte parent, ajout d'un compte enfant via le sous-panneau "Member Organizations", vérification et suppression

## Notes
- Utilise des données Faker avec seed reproductible pour pouvoir retrouver les données créées dans les tests suivants.
- Le nettoyage (suppression) est inclus en fin de chaque test.
- `testScenarioInlineEditListView` dépend d'un double-clic sur `.inlineEditIcon` qui peut être instable selon le timing.
