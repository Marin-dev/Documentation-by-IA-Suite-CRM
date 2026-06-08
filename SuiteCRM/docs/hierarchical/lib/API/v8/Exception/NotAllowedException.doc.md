# Fichier : NotAllowedException.php

**Chemin :** `lib/API/v8/Exception/NotAllowedException.php`
**Type :** PHP — exception
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Exception levée lorsqu'un utilisateur tente d'effectuer une opération pour laquelle il n'a pas les droits ACL (view, save, delete). Retourne HTTP 403.

**Type :** exception

---

## Exports / Symboles principaux

| Symbole | Valeur | Description |
|---|---|---|
| `NotAllowedException` | classe | Hérite de `ApiException` |
| `MSG_PREFIX` | `[Not Allowed]` | Préfixe |
| `DEFAULT_CODE` | `8005` | Code interne |
| `HTTP_STATUS` | `403` | Code HTTP |

---

## Interactions

**Appelé par :** `ModuleController` — vérifications ACL : `ACLAccess('view')`, `ACLAccess('save')`, `ACLAccess('delete')`, `ACLAccess('list')`
