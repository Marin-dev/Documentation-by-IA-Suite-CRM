# SaleModule.php (helper)

**Chemin :** `tests/_support/Page/SaleModule.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Page Object representant le module de test de type "Sale" cree par les tests de ModuleBuilder. Fournit les constantes d'URL et de nom pour naviguer vers ce module de test dans les tests d'acceptance.

## Role technique

Classe de Page Object Codeception avec constantes statiques uniquement. Module de type "sale" dans la taxonomie SugarObjectType (inclut des champs montant/devise).

---

## Entrees / Dependances

- **Imports principaux :**
  - `AcceptanceTester` — injecte dans le constructeur

## Sorties / Exports

- `$URL` — chemin relatif vers `Test_SaleModule/index`
- `$PACKAGE_NAME` — `'SaleTestModule'`
- `$NAME` — `'SaleTestModule'`
- **Consommateurs identifies dans le repo :**
  - `tests/acceptance/Core/SaleModuleCest.php`

## Relations cles

- **Appele par :** `SaleModuleCest`
- **Position dans le flux global :** constantes de reference pour les tests acceptance du ModuleBuilder (type sale)

---

## Points d'attention

- RAS
