# Fichier : ReservedKeywordNotAllowedException.php

**Chemin :** `lib/API/v8/Exception/ReservedKeywordNotAllowedException.php`
**Type :** PHP — exception
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Exception levée lorsqu'un mot-clé réservé JSON:API est utilisé comme nom d'attribut ou de relation. Hérite de `ConflictException` (HTTP 409).

**Type :** exception

---

## Exports / Symboles principaux

| Symbole | Valeur | Description |
|---|---|---|
| `ReservedKeywordNotAllowedException` | classe | Hérite de `ConflictException` |
| `MSG_PREFIX` | `[ReservedKeywordNotAllowed]` | Préfixe |
| `DEFAULT_CODE` | `8040` | Code interne |

---

## Notes

Hérite du HTTP_STATUS 409 de `ConflictException`. Aucun consommateur direct identifié dans `lib/API/v8/` — peut être utilisé dans d'autres parties du code.
