# PersonModule.php (helper)

**Chemin :** `tests/_support/Page/PersonModule.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Page Object representant le module de test de type "Person" cree par les tests de ModuleBuilder. Fournit les constantes d'URL et de nom pour naviguer vers ce module de test dans les tests d'acceptance.

## Role technique

Classe de Page Object Codeception avec constantes statiques uniquement. Module de type "person" dans la taxonomie SugarObjectType (inclut des champs prenom/nom/email).

---

## Entrees / Dependances

- **Imports principaux :**
  - `AcceptanceTester` — injecte dans le constructeur

## Sorties / Exports

- `$URL` — chemin relatif vers `Test_PersonModule/index`
- `$PACKAGE_NAME` — `'PersonTestModule'`
- `$NAME` — `'PersonTestModule'`
- **Consommateurs identifies dans le repo :**
  - `tests/acceptance/Core/PersonModuleCest.php`

## Relations cles

- **Appele par :** `PersonModuleCest`
- **Position dans le flux global :** constantes de reference pour les tests acceptance du ModuleBuilder (type person)

---

## Points d'attention

- RAS
