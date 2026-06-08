# Fichier : ApiController.php

**Chemin :** `lib/API/v8/Controller/ApiController.php`
**Type :** PHP — controller (classe de base abstraite)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Classe parente de tous les contrôleurs de l'API v8 de SuiteCRM. Elle fournit les mécanismes communs de génération de réponses JSON:API, de gestion des erreurs, de négociation de contenu et de validation de schéma. Elle n'est pas instanciée directement : elle est étendue par `ModuleController`, `OAuth2Controller` et `SchemaController`.

**Type :** controller (classe de base / service)

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Interop\Container\Exception\ContainerException` | Gestion d'erreurs DI |
| `JsonSchema\Validator` | Validation payload JSON:API contre schéma JSON Schema |
| `Psr\Container\ContainerInterface` | Conteneur de dépendances Slim |
| `Psr\Http\Message\ResponseInterface` | Réponse HTTP PSR-7 |
| `Slim\Http\Request` | Requête HTTP Slim |
| `Psr\Log\LoggerAwareInterface` | Interface de logging PSR-3 |
| `SuiteCRM\API\JsonApi\v1\JsonApi` | Objet JsonApi (version, schéma) |
| `SuiteCRM\API\v8\Exception\ApiException` | Exception de base API v8 |
| `SuiteCRM\ErrorMessage` | Utilitaire de log d'erreur SuiteCRM |
| `SuiteCRM\JsonApiErrorObject` | Objet d'erreur JSON:API |
| `SuiteCRM\Utility\Paths` | Résolution des chemins projet |
| `SuiteCRM\Utility\SuiteLogger` | Logger SuiteCRM |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `ApiController` | classe | Classe de base des contrôleurs API v8 |
| `CONTENT_TYPE` | constante | `application/vnd.api+json` |
| `VERSION_MAJOR/MINOR/PATCH/STABILITY` | constantes | Version de l'API (8.0.0-ALPHA) |
| `generateJsonApiResponse()` | méthode protégée | Sérialise un payload en réponse JSON:API valide |
| `generateJsonApiErrorResponse()` | méthode publique | Génère une réponse d'erreur JSON:API |
| `handleExceptionIntoPayloadError()` | méthode protégée | Convertit une exception en entrée `errors[]` du payload |
| `negotiatedJsonApiContent()` | méthode protégée | Vérifie Content-Type et Accept de la requête |
| `validateRequestWithJsonApiSchema()` | méthode protégée | Valide le body de la requête contre le schéma JSON Schema |
| `setLogger()` / `getVersion*()` | méthodes publiques | Injection du logger, accesseurs version |

---

## Interactions

**Appelé par :**
- `lib/API/v8/container/ApiController.php` (instanciation via DI)
- Toutes les sous-classes : `ModuleController`, `OAuth2Controller`, `SchemaController`

**Appelle :**
- `SuiteCRM\API\JsonApi\v1\JsonApi` (via container `JsonApi`)
- `JsonSchema\Validator` (validation du payload)
- `SuiteCRM\JsonApiErrorObject` (objet d'erreur)
- `SuiteCRM\ErrorMessage::log()` (log en mode développeur)
- `SuiteCRM\Utility\SuiteLogger` (fallback logger)

---

## Notes

- La constante `VERSION_STABILITY = 'ALPHA'` indique que l'API v8 est en alpha — ligne 74.
- `generateJsonApiResponse()` valide la réponse sortante contre le schéma JSON Schema avant envoi (ligne 136). Si la validation échoue, les erreurs sont ajoutées au payload mais la réponse est quand même renvoyée.
- `negotiatedJsonApiContent()` lève `UnsupportedMediaTypeException` (415) si le Content-Type n'est pas `application/vnd.api+json`, et `NotAcceptableException` (406) si l'en-tête Accept est absent ou incorrect — strict conformité JSON:API.
- Le container Slim est injecté dans le constructeur et stocké dans `$this->containers`.
