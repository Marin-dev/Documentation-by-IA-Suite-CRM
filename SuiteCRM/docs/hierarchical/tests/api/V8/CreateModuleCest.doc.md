# CreateModuleCest.php (integration-test / API)

**Chemin :** `tests/api/V8/CreateModuleCest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Tests d'intégration de la création de modules via l'API REST V8 JSON:API (`POST /Api/V8/module`). Vérifie les cas de succès et d'échec avec des data providers.

## Type
integration-test (API)

## Dependances cles
- `ApiTester` — acteur Codeception API
- `Codeception\Example` — data provider
- `Account` — classe SuiteCRM
- Framework : Codeception + PhpBrowser
- Endpoint testé : `POST /Api/V8/module`

## Scenarios couverts
**Cas de succes (shouldWork) :**
- `shouldWork01` (withId) : création d'un compte avec ID fourni → 201, JSON avec type Account et ID
- `shouldWork02` (withOutId) : création sans ID → 201, JSON avec type Account

**Cas d'echec (shouldNotWork) :**
- `shouldNotWork01` (withInvalidParameter) : paramètre `invalidParam` → 400 avec message d'erreur
- `shouldNotWork02` (withInvalidType) : type `InvalidModule` inexistant → 400
- `shouldNotWork03` (withInvalidId) : ID `111` non-UUID → 400
- `shouldNotWork04` (withInvalidAttribute) : attribut `invalidAttribute` inconnu → 400
- `shouldNotWork05` (withExistingBean) : ID d'un compte existant → 400

## Notes
- Chaque test de succès crée un compte et le supprime en fin de test via `deleteBean()`.
- Le commentaire ligne 46 questionne si 201 ou 200 est le code correct — pas de clarification dans le code.
- Namespace : `Test\Api\V8`.
