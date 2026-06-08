# OAuth2Cest.php (integration-test / API)

**Chemin :** `tests/api/V8/OAuth2Cest.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Tests d'intégration de l'authentification OAuth2 de l'API V8 SuiteCRM. Vérifie les cas valides et invalides du endpoint `/api/oauth/access_token`.

## Type
integration-test (API)

## Dependances cles
- `ApiTester` — acteur Codeception API
- `Helper\PhpBrowserDriverHelper` — URL d'instance
- Framework : Codeception + PhpBrowser
- Endpoint testé : `POST /api/oauth/access_token`

## Scenarios couverts
- `TestScenarioInvalidLogin` : credentials vides → HTTP 400
- `TestScenarioInvalidClient` : client_id/client_secret vides avec credentials admin valides → HTTP 401
- `TestScenarioGrantTypeNotAllowed` : grant `password` sans username/password → HTTP 400
- `TestScenarioLoginWithPasswordGrant` : login admin avec password grant → succès
- `TestScenarioLoginWithClientCredentialsGrant` : login avec client credentials grant, puis re-login password grant

## Notes
- `TestScenarioInvalidLogin` teste POST sans `grant_type` — le code 400 est attendu mais la raison exacte (missing grant_type vs credentials invalides) n'est pas vérifiée.
- Les credentials OAuth2 sont lus depuis les variables d'environnement via `PhpBrowserDriverHelper`.
