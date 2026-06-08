# AccountsModule.php (fixture / page object)

**Chemin :** `tests/_support/Page/AccountsModule.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Page Object représentant le module Accounts de SuiteCRM dans les tests d'acceptance. Centralise les constantes URL et libellés pour éviter la duplication dans les Cests.

## Type
fixture / page object

## Dependances cles
- `AcceptanceTester` — injecté dans le constructeur

## Scenarios couverts
Fournit : `$URL = 'index.php?module=Accounts'`, `$NAME = 'Accounts'`, `$CREATE_LINK = 'Create Account'`.

## Notes
- Utilisé par `ModuleBuilderFieldsCest` pour naviguer vers le module Accounts et créer des comptes.
- Namespace : `Page`.
