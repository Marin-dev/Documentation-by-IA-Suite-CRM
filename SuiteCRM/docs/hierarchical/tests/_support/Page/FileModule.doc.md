# FileModule.php (helper)

**Chemin :** `tests/_support/Page/FileModule.php`
**Type :** PHP
**Derniere mise a jour doc :** 2026-06-02

---

## Role fonctionnel

Page Object representant le module de test de type "File" cree par les tests de ModuleBuilder. Fournit les constantes d'URL et de nom pour naviguer vers ce module de test dans les tests d'acceptance.

## Role technique

Classe de Page Object Codeception avec constantes statiques uniquement (`$URL`, `$PACKAGE_NAME`, `$NAME`). Module de type "file" dans la taxonomie SugarObjectType.

---

## Entrees / Dependances

- **Imports principaux :**
  - `AcceptanceTester` — injecte dans le constructeur

## Sorties / Exports

- `$URL` — chemin relatif vers `Test_FileModule/index`
- `$PACKAGE_NAME` — `'FileTestModule'`
- `$NAME` — `'FileTestModule'`
- **Consommateurs identifies dans le repo :**
  - `tests/acceptance/Core/FileModuleCest.php`

## Relations cles

- **Appele par :** `FileModuleCest`
- **Appelle :** rien
- **Position dans le flux global :** constantes de reference pour les tests acceptance du ModuleBuilder (type file)

---

## Points d'attention

- Identique en structure a `BasicModule`, `CompanyModule`, etc. — seuls les noms different.
