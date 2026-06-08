# GetModuleCest.php (integration-test / API)

**Chemin :** `tests/api/V8/GetModuleCest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Tests d'intégration de la récupération d'un enregistrement unique via l'API REST V8 JSON:API (`GET /Api/V8/module/{moduleName}/{id}`).

## Type
integration-test (API)

## Dependances cles
- `ApiTester`, `Codeception\Example`
- Endpoint testé : `GET /Api/V8/module/Accounts/{id}`

## Scenarios couverts
**Cas de succes :**
- `shouldWork01` (withoutParams) : récupération complète d'un compte → 200, JSON avec type Account et ID
- `shouldWork02` (withFields) : filtrage par `?fields[Accounts]=name,account_type` → 200, exactement 2 attributs

**Cas d'echec :**
- `shouldNotWork01` : module name invalide → 400
- `shouldNotWork02` : ID non-UUID → 400
- `shouldNotWork03` : UUID valide mais inexistant → 400
- `shouldNotWork04` : paramètre de query invalide → 400
- `shouldNotWork05` : champs inexistants → 400 avec liste des champs manquants
- `shouldNotWork06` : clé de filtre sur module inexistant → 400

## Notes
- Namespace : `Test\Api\V8`.
