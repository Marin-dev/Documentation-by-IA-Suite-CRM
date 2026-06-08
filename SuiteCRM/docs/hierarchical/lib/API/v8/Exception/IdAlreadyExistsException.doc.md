# Fichier : IdAlreadyExistsException.php

**Chemin :** `lib/API/v8/Exception/IdAlreadyExistsException.php`
**Type :** PHP — exception
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Exception levée lors d'une tentative de création d'un bean avec un ID déjà existant en base. Retourne un statut HTTP 403.

**Type :** exception

---

## Exports / Symboles principaux

| Symbole | Valeur | Description |
|---|---|---|
| `IdAlreadyExistsException` | classe | Hérite de `ApiException` |
| `MSG_PREFIX` | `[IdAlreadyExists]` | Préfixe |
| `DEFAULT_CODE` | `8060` | Code interne |
| `HTTP_STATUS` | `403` | Code HTTP |

---

## Interactions

**Appelé par :** `ModuleController::createModuleRecord` (ligne 455) — quand l'ID fourni dans le payload existe déjà.

---

## Notes

Le code HTTP 403 est utilisé ici plutôt que 409 (Conflict), ce qui peut sembler contre-intuitif. La spécification JSON:API recommande 409 pour les conflits d'ID.
