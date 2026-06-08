# Fichier : ModuleNotFoundException.php

**Chemin :** `lib/API/v8/Exception/ModuleNotFoundException.php`
**Type :** PHP — exception
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Exception levée lorsque le module demandé n'existe pas ou que `BeanFactory` ne peut pas créer un bean pour ce module. Retourne HTTP 406 (Not Acceptable).

**Type :** exception

---

## Exports / Symboles principaux

| Symbole | Valeur | Description |
|---|---|---|
| `ModuleNotFoundException` | classe | Hérite de `ApiException` |
| `MSG_PREFIX` | `[Module Not Found]` | Préfixe |
| `DEFAULT_CODE` | `8015` | Code interne |
| `HTTP_STATUS` | `406` | Code HTTP (Not Acceptable) |
| `DETAIL_TEXT_LABEL` | `LBL_MODULE_NOT_FOUND_EXCEPTION_DETAIL` | Clé i18n |

---

## Interactions

**Appelé par :** `ModuleController` (toutes les méthodes vérifiant l'existence d'un module), `ModulesLib::generatePaginatedModuleRecords()`

---

## Notes

Le choix de HTTP 406 (Not Acceptable) plutôt que 404 pour un module non trouvé est inhabituel — cela peut prêter à confusion.
