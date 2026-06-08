# Fichier : ModuleLanguage.php (container)

**Chemin :** `lib/API/v8/container/ModuleLanguage.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui instancie `SuiteCRM\Utility\ModuleLanguage` et l'enregistre dans le container DI sous la clé `'ModuleLanguage'`. Fournit les chaînes de traduction spécifiques à un module.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Description |
|---|---|---|
| `ModuleLanguage` | `SuiteCRM\Utility\ModuleLanguage` | Chaînes i18n d'un module spécifique |

---

## Interactions

**Consommé par :** `ModuleController::getModuleMetaLanguage()`
