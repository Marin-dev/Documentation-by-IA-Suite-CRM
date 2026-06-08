# Fichier : JsonApi.php (container)

**Chemin :** `lib/API/v8/container/JsonApi.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui instancie `SuiteCRM\API\JsonApi\v1\JsonApi` et l'enregistre dans le container DI sous la clé `'JsonApi'`. Cet objet fournit la version de l'API et le chemin du schéma JSON Schema de validation.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Services injectés |
|---|---|---|
| `JsonApi` | `SuiteCRM\API\JsonApi\v1\JsonApi` | `LoggerInterface` |

---

## Interactions

**Consommé par :** `ApiController::generateJsonApiResponse()`, `generateJsonApiErrorResponse()`, `validateRequestWithJsonApiSchema()`, `SchemaController::getJsonApiSchema()`
