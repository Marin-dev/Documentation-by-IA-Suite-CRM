# DeleteModuleCest.php (integration-test / API)

**Chemin :** `tests/api/V8/DeleteModuleCest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Tests d'intégration de la suppression d'un enregistrement via l'API REST V8 (`DELETE /Api/V8/module/Accounts/{id}`).

## Type
integration-test (API)

## Dependances cles
- `ApiTester`
- Endpoint testé : `DELETE /Api/V8/module/Accounts/{id}`

## Scenarios couverts
- `shouldWork` : création d'un compte, suppression via DELETE → 200, message de confirmation JSON, puis suppression physique via `deleteBean()`
- `shouldNotWork` : suppression physique préalable, puis GET sur l'ID supprimé → 400 avec message "not found"

## Notes
- La suppression API est une soft-delete (le record reste en DB avec `deleted=1`). `deleteBean()` fait la suppression physique.
- `shouldNotWork` teste un GET (pas un DELETE) sur un ID inexistant — incohérence potentielle dans le test.
- Namespace : `Test\Api\V8`.
