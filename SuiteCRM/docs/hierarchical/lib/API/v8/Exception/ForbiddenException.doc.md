# Fichier : ForbiddenException.php

**Chemin :** `lib/API/v8/Exception/ForbiddenException.php`
**Type :** PHP — exception
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Exception levée lorsque l'utilisateur n'a pas les droits nécessaires pour effectuer l'opération demandée (type de relation invalide). Retourne un statut HTTP 403.

**Type :** exception

---

## Exports / Symboles principaux

| Symbole | Valeur | Description |
|---|---|---|
| `ForbiddenException` | classe | Hérite de `ApiException` |
| `MSG_PREFIX` | `[Forbidden]` | Préfixe |
| `DEFAULT_CODE` | `8020` | Code interne |
| `HTTP_STATUS` | `403` | Code HTTP |

---

## Interactions

**Appelé par :** `ModuleController::createModuleRelationship`, `deleteModuleRelationship` (type de relation non supporté)
