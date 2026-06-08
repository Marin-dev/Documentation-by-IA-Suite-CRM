# IssueModule.php (helper)

**Chemin :** `tests/_support/Page/IssueModule.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Page Object representant le module de test de type "Issue" cree par les tests de ModuleBuilder. Fournit les constantes d'URL et de nom pour naviguer vers ce module de test dans les tests d'acceptance.

## Role technique

Classe de Page Object Codeception avec constantes statiques uniquement. Module de type "issue" dans la taxonomie SugarObjectType.

---

## Entrees / Dependances

- **Imports principaux :**
  - `AcceptanceTester` — injecte dans le constructeur

## Sorties / Exports

- `$URL` — chemin relatif vers `Test_IssueModule/index`
- `$PACKAGE_NAME` — `'IssueTestModule'`
- `$NAME` — `'IssueTestModule'`
- **Consommateurs identifies dans le repo :**
  - `tests/acceptance/Core/IssueModuleCest.php`

## Relations cles

- **Appele par :** `IssueModuleCest`
- **Position dans le flux global :** constantes de reference pour les tests acceptance du ModuleBuilder (type issue)

---

## Points d'attention

- RAS
