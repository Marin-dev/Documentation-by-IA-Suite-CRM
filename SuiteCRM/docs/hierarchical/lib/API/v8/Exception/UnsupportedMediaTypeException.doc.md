# Fichier : UnsupportedMediaTypeException.php

**Chemin :** `lib/API/v8/Exception/UnsupportedMediaTypeException.php`
**Type :** PHP — exception
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Exception levée lorsque l'en-tête `Content-Type` de la requête n'est pas `application/vnd.api+json`. Retourne HTTP 415 (Unsupported Media Type).

**Type :** exception

---

## Exports / Symboles principaux

| Symbole | Valeur | Description |
|---|---|---|
| `UnsupportedMediaTypeException` | classe | Hérite de `ApiException` |
| `MSG_PREFIX` | `[Unsupported Media Type]` | Préfixe |
| `DEFAULT_CODE` | `8005` | Code interne |
| `HTTP_STATUS` | `415` | Code HTTP |
| `DETAIL_TEXT_LABEL` | `LBL_UNSUPPORTED_MEDIA_TYPE_EXCEPTION_DETAIL` | Clé i18n |

---

## Interactions

**Appelé par :** `ApiController::negotiatedJsonApiContent()` (ligne 282) — Content-Type incorrect ou absent.
