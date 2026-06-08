# Fichier : NotFoundException.php

**Chemin :** `lib/API/v8/Exception/NotFoundException.php`
**Type :** PHP — exception
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Exception levée lorsqu'un enregistrement, une relation ou un schéma demandé est introuvable. Retourne HTTP 404.

**Type :** exception

---

## Exports / Symboles principaux

| Symbole | Valeur | Description |
|---|---|---|
| `NotFoundException` | classe | Hérite de `ApiException` |
| `MSG_PREFIX` | `[Not Found]` | Préfixe |
| `DEFAULT_CODE` | `8005` | Code interne |
| `HTTP_STATUS` | `404` | Code HTTP |

---

## Interactions

**Appelé par :** `ModuleController` (bean inexistant, relation inexistante, layout inexistant), `SchemaController` (fichier schéma absent)
