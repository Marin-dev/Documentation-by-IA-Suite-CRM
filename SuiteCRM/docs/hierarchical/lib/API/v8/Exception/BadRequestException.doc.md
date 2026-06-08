# Fichier : BadRequestException.php

**Chemin :** `lib/API/v8/Exception/BadRequestException.php`
**Type :** PHP — exception
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Exception levée lorsque la requête client est syntaxiquement ou sémantiquement invalide (requête malformée, paramètre non supporté, fonctionnalité non implémentée). Retourne un statut HTTP 400.

**Type :** exception

---

## Exports / Symboles principaux

| Symbole | Valeur | Description |
|---|---|---|
| `BadRequestException` | classe | Hérite de `ApiException` |
| `MSG_PREFIX` | `[BadRequest]` | Préfixe du message d'erreur |
| `DEFAULT_CODE` | `8020` | Code d'erreur interne |
| `HTTP_STATUS` | `400` | Code HTTP retourné |
| `DETAIL_TEXT_LABEL` | `LBL_BAD_REQUEST_EXCEPTION_DETAIL` | Clé i18n du détail |

---

## Interactions

**Appelé par :** `ModuleController` (paramètres `include`/`filter` non implémentés, type de relation non supporté), `ModulesLib` (stratégie de filtre inconnue)

---

## Notes

Classe minimale : uniquement des constantes redéfinies. Toute la logique est dans `ApiException`.
