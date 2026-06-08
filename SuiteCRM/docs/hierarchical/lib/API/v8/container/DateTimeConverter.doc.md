# Fichier : DateTimeConverter.php (container)

**Chemin :** `lib/API/v8/container/DateTimeConverter.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui expose la variable globale `$timedate` (objet `TimeDate` de SuiteCRM) dans le container DI sous la clé `'DateTimeConverter'`. Permet la conversion des dates entre les formats utilisateur, base de données et ISO 8601.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Valeur | Description |
|---|---|---|
| `DateTimeConverter` | `$timedate` (global) | Objet `TimeDate` SuiteCRM |

---

## Interactions

**Consommé par :** `ModuleController::getModulesMetaViewed()`, `getModuleRecordsViewed()` — conversion datetime pour les éléments récemment consultés.
