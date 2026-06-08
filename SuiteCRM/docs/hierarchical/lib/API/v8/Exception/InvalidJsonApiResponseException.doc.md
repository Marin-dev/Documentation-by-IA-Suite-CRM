# Fichier : InvalidJsonApiResponseException.php

**Chemin :** `lib/API/v8/Exception/InvalidJsonApiResponseException.php`
**Type :** PHP — exception
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Exception levée lorsque la réponse générée côté serveur ne respecte pas le schéma JSON:API. Retourne HTTP 400. Utilisée comme signal d'erreur interne dans les signatures de méthodes des contrôleurs.

**Type :** exception

---

## Exports / Symboles principaux

| Symbole | Valeur | Description |
|---|---|---|
| `InvalidJsonApiResponseException` | classe | Hérite de `ApiException` |
| `MSG_PREFIX` | `[InvalidJsonApiResponse]` | Préfixe |
| `DEFAULT_CODE` | `8010` | Code interne |
| `HTTP_STATUS` | `400` | Code HTTP |
| `DETAIL_TEXT_LABEL` | `LBL_INVALID_JSON_API_RESPONSE_EXCEPTION_DETAIL` | Clé i18n |

---

## Interactions

Référencée dans les signatures `@throws` de `OAuth2Controller::authenticate()`, `SchemaController::getJsonApiSchema()` et `getSwaggerSchema()`.
