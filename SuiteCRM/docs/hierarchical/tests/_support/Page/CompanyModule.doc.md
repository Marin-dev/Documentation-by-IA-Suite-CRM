# CompanyModule.php (helper)

**Chemin :** `tests/_support/Page/CompanyModule.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Page Object representant le module de test de type "Company" cree dynamiquement par les tests de ModuleBuilder. Fournit les constantes d'URL et de nom pour naviguer vers ce module de test dans les tests d'acceptance.

## Role technique

Classe de Page Object Codeception contenant uniquement des constantes statiques (`$URL`, `$PACKAGE_NAME`, `$NAME`) et une reference a l'`AcceptanceTester`. Pas de logique metier propre.

---

## Entrees / Dependances

- **Imports principaux :**
  - `AcceptanceTester` — injecte dans le constructeur

## Sorties / Exports

- `$URL` — chemin relatif vers `Test_CompanyModule/index`
- `$PACKAGE_NAME` — `'CompanyTestModule'`
- `$NAME` — `'CompanyTestModule'`
- **Consommateurs identifies dans le repo :**
  - `tests/acceptance/Core/CompanyModuleCest.php`

## Relations cles

- **Appele par :** `CompanyModuleCest`
- **Appelle :** rien
- **Position dans le flux global :** constantes de reference pour les tests acceptance du ModuleBuilder

---

## Points d'attention

- Le module `Test_CompanyModule` doit etre cree et deploye par `ModuleBuilder` avant que les tests qui utilisent cette page puissent s'executer.
