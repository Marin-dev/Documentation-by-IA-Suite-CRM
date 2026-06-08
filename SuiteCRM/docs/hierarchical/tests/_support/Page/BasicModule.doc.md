# BasicModule.php (fixture / page object)

**Chemin :** `tests/_support/Page/BasicModule.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Page Object pour le module de test `BasicTestModule` créé via le Module Builder lors des tests acceptance. Centralise les constantes URL, nom de package et nom de module.

## Type
fixture / page object

## Dependances cles
- `AcceptanceTester`

## Notes
- `$URL = 'index.php?module=Test_BasicModule&action=index'`, `$PACKAGE_NAME = 'BasicTestModule'`.
- Utilisé par `BasicModuleCest`.
- Namespace : `Page`.
