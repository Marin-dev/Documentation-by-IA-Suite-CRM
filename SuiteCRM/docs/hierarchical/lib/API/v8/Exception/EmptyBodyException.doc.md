# Fichier : EmptyBodyException.php

**Chemin :** `lib/API/v8/Exception/EmptyBodyException.php`
**Type :** PHP — exception
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Exception levée lorsque le body de la requête est vide ou ne peut pas être décodé en JSON. Retourne un statut HTTP 400.

**Type :** exception

---

## Exports / Symboles principaux

| Symbole | Valeur | Description |
|---|---|---|
| `EmptyBodyException` | classe | Hérite de `ApiException` |
| `MSG_PREFIX` | `[EmptyBody]` | Préfixe du message |
| `DEFAULT_CODE` | `8015` | Code d'erreur interne |
| `HTTP_STATUS` | `400` | Code HTTP retourné |
| `DETAIL_TEXT_LABEL` | `LBL_EMPTY_BODY_EXCEPTION_DETAIL` | Clé i18n |

---

## Interactions

**Appelé par :** `ModuleController::createModuleRecord`, `updateModuleRecord`, `createModuleRelationship`, `updateModuleRelationship`
