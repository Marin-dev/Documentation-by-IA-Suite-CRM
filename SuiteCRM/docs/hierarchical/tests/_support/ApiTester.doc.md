# ApiTester.php (helper / acteur Codeception API)

**Chemin :** `tests/_support/ApiTester.php`
**Type :** PHP
**Dernière mise à jour doc :** 2026-06-02

---

## Role
Acteur Codeception spécialisé pour les tests de l'API REST V8 de SuiteCRM. Gère l'authentification OAuth2 (password grant et client credentials grant), la négociation de contenu JSON/JSON:API, et expose des helpers de création/suppression de données directement en base.

## Type
helper / acteur Codeception (integration/API)

## Dependances cles
- `Codeception\Actor` — classe parente
- `Helper\PhpBrowserDriverHelper` — récupération de l'URL d'instance et des credentials
- `Api\V8\Controller\BaseController` — constante `MEDIA_TYPE`
- `DBManagerFactory` — accès direct SQL pour création/suppression de fixtures
- Trait `_generated\ApiTesterActions`

## Scenarios couverts
- `loginWithPasswordGrant()` : POST sur `/api/oauth/access_token` avec grant `password`, stocke l'access token en statique
- `loginWithClientCredentialsGrant()` : POST avec grant `client_credentials`
- `sendJwtAuthorisation()` : injecte le header `Authorization: Bearer <token>`
- `sendJsonApiContentNegotiation()` / `seeJsonApiContentNegotiation()` : headers JSON:API
- `seeJsonAPISuccess()` / `seeJsonApiFailure()` : vérifie la présence/absence de la clé `errors` dans la réponse
- `createAccount()` / `createContact()` : insert SQL direct (temporaire — commentaire "fix this")
- `deleteBean()` / `deleteRelationship()` : suppression SQL directe

## Notes
- L'access token est stocké en `static` : partagé entre tous les tests d'une même suite, risque de pollution inter-tests.
- Les méthodes `createAccount`, `createContact`, `deleteBean` sont marquées comme temporaires dans le code source — à remplacer par des appels API propres.
- Le `logout()` est vide (ligne 162) : non implémenté.
