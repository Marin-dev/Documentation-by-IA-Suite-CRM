# Fichier : NotImplementedException.php

**Chemin :** `lib/API/v8/Exception/NotImplementedException.php`
**Type :** PHP — exception
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Exception levée pour les fonctionnalités prévues mais non encore implémentées. Retourne HTTP 500.

**Type :** exception

---

## Exports / Symboles principaux

| Symbole | Valeur | Description |
|---|---|---|
| `NotImplementedException` | classe | Hérite de `ApiException` |
| `MSG_PREFIX` | `[NotImplementedException]` | Préfixe |
| `DEFAULT_CODE` | `8035` | Code interne |
| `HTTP_STATUS` | `500` | Code HTTP |

---

## Notes

Le choix de HTTP 500 plutôt que 501 (Not Implemented) est inhabituel.
