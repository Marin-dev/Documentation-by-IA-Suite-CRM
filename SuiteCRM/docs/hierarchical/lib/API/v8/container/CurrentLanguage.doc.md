# Fichier : CurrentLanguage.php (container)

**Chemin :** `lib/API/v8/container/CurrentLanguage.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui instancie `SuiteCRM\Utility\CurrentLanguage` et l'enregistre dans le container DI sous la clé `'CurrentLanguage'`. Fournit la langue courante de l'utilisateur pour les traductions.

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Services injectés |
|---|---|---|
| `CurrentLanguage` | `SuiteCRM\Utility\CurrentLanguage` | `$container` |

---

## Interactions

**Consommé par :** `ModuleController::getModuleMetaLanguage()`, `getApplicationMetaLanguages()`
