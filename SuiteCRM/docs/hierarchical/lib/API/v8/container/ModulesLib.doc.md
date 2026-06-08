# Fichier : ModulesLib.php (container)

**Chemin :** `lib/API/v8/container/ModulesLib.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui instancie `SuiteCRM\API\v8\Library\ModulesLib` et l'enregistre dans le container DI sous la clé `'ModulesLib'`.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Services injectés |
|---|---|---|
| `ModulesLib` | `SuiteCRM\API\v8\Library\ModulesLib` | `$container` |

---

## Interactions

**Consommé par :** `ModuleController::getModuleRecords()`
