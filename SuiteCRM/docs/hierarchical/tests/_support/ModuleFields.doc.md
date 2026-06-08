# ModuleFields.php (fixture / page object)

**Chemin :** `tests/_support/ModuleFields.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Page Object représentant le module de test `TestModuleFields` utilisé dans les tests de champs du Module Builder. Centralise les constantes URL, nom de package et nom de module pour éviter la duplication dans les Cests.

## Type
fixture / page object

## Dependances cles
- `AcceptanceTester` — injecté dans le constructeur

## Scenarios couverts
Pas de logique de test : fournit les constantes statiques `$URL`, `$PACKAGE_NAME`, `$NAME`.

## Notes
- Utilisé par `ModuleBuilderFieldsCest` pour référencer le module de test des champs.
- Namespace : `Page`.
