# QuickRepairAndRebuild.php

**Chemin :** `modules/Administration/QuickRepairAndRebuild.php`
**Type :** PHP (Model / service)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Classe centrale des operations de maintenance et reparation de SuiteCRM. Permet de vider les caches (templates, JS, vardefs, dashlets, feed, theme, langue, recherche), reconstruire les extensions, reparer les tables BDD, et reconstruire les tables d'audit. C'est le coeur de la section "Quick Repair & Rebuild" du panneau d'administration.

## Role technique
Classe `RepairAndClear` avec une methode facade `repairAndClearAll()` qui dispatche vers des methodes specialisees selon une liste d'actions. Chaque methode cible un sous-repertoire du cache et supprime recursivement les fichiers par extension. Utilise `ModuleInstaller::rebuild_all()` pour les extensions, `DBManager::repairTable()` pour la BDD, `LanguageManager::clearLanguageCache()` pour les langues.

---

## Dependances cles
| Element | Role |
|---|---|
| `ModuleInstall/ModuleInstaller.php` | Reconstruction extensions |
| `include/modules.php` | Liste $beanFiles pour reparation BDD |
| `SugarThemeRegistry::clearAllCaches()` | Vider cache themes |
| `SugarFeed::flushBackendCache()` | Vider cache SugarFeed |
| `LanguageManager::clearLanguageCache()` | Vider cache langue |
| `ExternalAPIFactory::clearCache()` | Vider cache API externes |
| `DynamicField` | Reparation champs personnalises |
| `Api\Core\Config\ApiConfig` (use) | INCONNU - import present mais non utilise visiblement |

## Symboles principaux

| Symbole | Type | Role |
|---|---|---|
| `RepairAndClear` | Classe | Service de maintenance |
| `repairAndClearAll($selected_actions, $modules, $autoexecute, $show_output)` | Methode | Facade : execute toutes les actions demandees |
| `repairDatabase()` | Methode | Inclut `repairDatabase.php` pour reparation BDD globale |
| `repairDatabaseSelectModules()` | Methode | Repare la BDD pour une selection de modules |
| `rebuildExtensions()` | Methode | Reconstruit toutes les extensions via ModuleInstaller |
| `clearTpls()` | Methode | Supprime les .tpl compiles du cache |
| `clearJsFiles()` | Methode | Supprime les .js du cache modules |
| `clearVardefs()` | Methode | Supprime les vardefs.php du cache |
| `clearJsLangFiles()` | Methode | Supprime les fichiers JS de langue |
| `clearLanguageCache()` | Methode | Vide cache langue modules et app_strings |
| `clearDashlets()` | Methode | Supprime cache dashlets |
| `clearThemeCache()` | Methode | Vide cache themes |
| `clearSearchCache()` | Methode | Supprime `unified_search_modules.php` en cache |
| `rebuildAuditTables()` | Methode | Cree les tables d'audit manquantes pour les beans actives |
| `clearAll` (action) | Constante action | Chaine complete de toutes les operations de nettoyage |

## Interactions
- **Appele par :** `views/view.repair.php`, pages Rebuild individuelles (`RebuildDashlets.php`, `RebuildRelationship.php`, etc.)
- **Appelle :** `ModuleInstaller`, `DBManager`, `LanguageManager`, `SugarThemeRegistry`, `repairDatabase.php` (include)
- **Position :** Coeur de la section "Repair" de l'administration

---

## Notes
- `repairAndClearAll()` ajoute toujours `repairDatabase` a la liste d'actions et appelle `clearVardefs()` + `clearLanguageCache()` en premier.
- `rebuildAuditTables()` verifie `$focus->is_AuditEnabled()` avant de creer une table — silencieuse si desactivee.
- `_clearCache()` est recursive et supprime par extension — risque de supprimer trop si l'extension est courante (ex: `.php` pour dashlets).
- L'import `Api\Core\Config\ApiConfig` est present mais son usage n'est pas visible dans ce fichier.
