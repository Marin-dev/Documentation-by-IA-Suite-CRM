# Fichier : ConflictException.php

**Chemin :** `lib/API/v8/Exception/ConflictException.php`
**Type :** PHP — exception
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Exception levée lors d'un conflit de données : type de ressource incorrect dans le payload, échec d'ajout/suppression de relations, etc. Retourne un statut HTTP 409.

**Type :** exception

---

## Exports / Symboles principaux

| Symbole | Valeur | Description |
|---|---|---|
| `ConflictException` | classe | Hérite de `ApiException` |
| `MSG_PREFIX` | `[Conflict]` | Préfixe du message |
| `DEFAULT_CODE` | `8021` | Code d'erreur interne |
| `HTTP_STATUS` | `409` | Code HTTP retourné |

---

## Interactions

**Appelé par :** `ModuleController` (type incompatible, échec relation), `ModuleController::createModuleRecord` et `updateModuleRecord`

---

## Notes

Hérite de `ApiException`. `ReservedKeywordNotAllowedException` hérite de `ConflictException`.
