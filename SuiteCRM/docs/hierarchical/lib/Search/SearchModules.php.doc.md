# SearchModules.php

**Chemin :** `lib/Search/SearchModules.php`
**Type :** PHP — Service
**Derniere mise a jour doc :** 2026-05-30

---

## Role fonctionnel
Gere la liste des modules disponibles pour la recherche globale unifiee. Construit et maintient le cache des modules de recherche, gere les preferences d'affichage (modules actives/desactives) et permet de sauvegarder les parametres d'administration.

## Role technique
Classe statique. Lit/ecrit `custom/modules/unified_search_modules_display.php` pour les preferences d'affichage. Construit un cache `cache/modules/unified_search_modules.php` a partir des vardefs et `SearchFields` de chaque module. La methode `buildCache()` iterere sur `$beanList` global.

---

## Dependances cles
- `UnifiedSearchAdvanced` (`modules/Home/UnifiedSearchAdvanced.php`)
- `BeanFactory`, `VardefManager`
- `$beanList`, `$beanFiles`, `$dictionary` (globals SuiteCRM)

## Exports / Symboles principaux
- `SearchModules` — classe statique
  - `getModulesList(): array` — tous les modules (actives + desactives) avec labels
  - `getEnabledModules(): array` — modules actives uniquement
  - `getUnifiedSearchModulesDisplay(): array` — preferences d'affichage utilisateur
  - `getUnifiedSearchModules(): array` — depuis le cache
  - `saveGlobalSearchSettings(): void` — sauvegarde depuis `$_REQUEST['enabled_modules']`
  - `buildCache(): void` — reconstruit le cache des modules

## Relations cles
- **Appele par :** `SearchWrapper`, `SearchQuery`, `SearchFormView`
- **Position dans le flux global :** source de verite pour les modules de recherche

---

## Points d'attention
- `buildCache()` charge les vardefs de TOUS les modules — operation couteuse, ne pas appeler en boucle.
- Le fichier cache est a `cache/modules/unified_search_modules.php`.
- `writeUnifiedSearchModulesDisplayFile()` leve une `RuntimeException` si l'ecriture echoue.
