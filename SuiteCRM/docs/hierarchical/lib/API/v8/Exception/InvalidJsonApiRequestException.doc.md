# Fichier : InvalidJsonApiRequestException.php

**Chemin :** `lib/API/v8/Exception/InvalidJsonApiRequestException.php`
**Type :** PHP — exception
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Exception levée lorsque le payload de la requête ne respecte pas le schéma JSON:API (validation JSON Schema). Retourne HTTP 400.

**Type :** exception

---

## Exports / Symboles principaux

| Symbole | Valeur | Description |
|---|---|---|
| `InvalidJsonApiRequestException` | classe | Hérite de `ApiException` |
| `MSG_PREFIX` | `[InvalidJsonApiRequest]` | Préfixe |
| `DEFAULT_CODE` | `8010` | Code interne |
| `HTTP_STATUS` | `400` | Code HTTP |
| `DETAIL_TEXT_LABEL` | `LBL_INVALID_JSON_API_REQUEST_EXCEPTION_DETAIL` | Clé i18n |

---

## Interactions

**Appelé par :** `ApiController::validateRequestWithJsonApiSchema()` (ligne 321)
