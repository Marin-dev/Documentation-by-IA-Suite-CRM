# Fichier : SchemaController.php

**Chemin :** `lib/API/v8/Controller/SchemaController.php`
**Type :** PHP — controller
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Contrôleur chargé d'exposer les schémas de l'API v8 : le schéma JSON:API (fichier JSON Schema utilisé pour valider les payloads) et le schéma Swagger/OpenAPI (`swagger.json`). Permet aux clients de découvrir la structure attendue de l'API.

**Type :** controller

---

## Dépendances clés

| Import | Rôle |
|---|---|
| `Psr\Http\Message\ResponseInterface` | Réponse HTTP PSR-7 |
| `Psr\Http\Message\ServerRequestInterface` | Requête HTTP PSR-7 |
| `SuiteCRM\API\JsonApi\v1\JsonApi` | Fournit le chemin du schéma JSON:API |
| `ApiController` (parent) | Classe de base (gestion erreurs, negotiation) |

---

## Exports / Symboles principaux

| Symbole | Type | Rôle |
|---|---|---|
| `SchemaController` | classe | Contrôleur d'exposition des schémas |
| `getJsonApiSchema()` | méthode publique | `GET /v8/schema` — retourne le schéma JSON:API |
| `getSwaggerSchema()` | méthode publique | `GET /v8/swagger.json` — retourne le schéma Swagger |

---

## Interactions

**Appelé par :**
- `lib/API/v8/route/schemaRoutes.php` → routes `GET /v8/schema` et `GET /v8/swagger.json`
- `lib/API/v8/container/SchemaController.php` (instanciation DI)

**Appelle :**
- `SuiteCRM\API\JsonApi\v1\JsonApi::getSchemaPath()` (chemin du fichier JSON Schema)
- `file_get_contents()` (lecture fichier)
- `ApiController::handleExceptionIntoPayloadError()` (héritage, gestion erreurs)

---

## Notes

- Le fichier Swagger est cherché à `dirname(__DIR__).'/swagger.json'`, soit `lib/API/v8/swagger.json` — ligne 103.
- Lève `NotFoundException` si les fichiers schéma n'existent pas sur disque.
- La réponse est renvoyée avec Content-Type `application/vnd.api+json`.
