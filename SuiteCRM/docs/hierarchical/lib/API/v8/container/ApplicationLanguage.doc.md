# Fichier : ApplicationLanguage.php (container)

**Chemin :** `lib/API/v8/container/ApplicationLanguage.php`
**Type :** PHP — configuration (DI factory)
**Dernière mise à jour doc :** 2026-05-30

---

## Rôle

Factory qui instancie `SuiteCRM\Utility\ApplicationLanguage` et l'enregistre dans le container DI sous la clé `'ApplicationLanguages'`. Fournit les chaînes de traduction de l'application (non spécifiques à un module).

**Type :** configuration

---

## Ce que ce fichier configure

| Clé container | Classe instanciée | Description |
|---|---|---|
| `ApplicationLanguages` | `SuiteCRM\Utility\ApplicationLanguage` | Chaînes i18n de l'application |

---

## Interactions

**Consommé par :** `ModuleController::getApplicationMetaLanguages()`
