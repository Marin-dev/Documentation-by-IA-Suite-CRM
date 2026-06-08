# Fichier : NotAcceptableException.php

**Chemin :** `lib/API/v8/Exception/NotAcceptableException.php`
**Type :** PHP — exception
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Exception levée lorsque l'en-tête `Accept` de la requête est absent, multiple ou ne vaut pas `application/vnd.api+json`. Retourne HTTP 406.

**Type :** exception

---

## Exports / Symboles principaux

| Symbole | Valeur | Description |
|---|---|---|
| `NotAcceptableException` | classe | Hérite de `ApiException` |
| `MSG_PREFIX` | `[Not Acceptable]` | Préfixe |
| `DEFAULT_CODE` | `8005` | Code interne |
| `HTTP_STATUS` | `406` | Code HTTP |
| `DETAIL_TEXT_LABEL` | `LBL_NOT_ACCEPTABLE_EXCEPTION_DETAIL` | Clé i18n |

---

## Interactions

**Appelé par :** `ApiController::negotiatedJsonApiContent()` (lignes 285-293)
