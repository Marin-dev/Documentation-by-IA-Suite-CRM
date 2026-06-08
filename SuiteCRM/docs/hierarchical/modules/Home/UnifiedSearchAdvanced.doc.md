# UnifiedSearchAdvanced.php

**Chemin :** `modules/Home/UnifiedSearchAdvanced.php`
**Type :** PHP - Classe utilitaire (dépréciée)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Classe dépréciée depuis v7.12.0 gérant la recherche globale unifiée dans SuiteCRM. Construit et gère le cache des modules searchables (`unified_search_modules.php`), exécute des recherches multi-modules, et sauvegarde les préférences de recherche utilisateur.

## Type
helper (deprecated)

## Dépendances clés
- `include/SearchForm/SearchForm2.php` — génération des clauses WHERE de recherche
- `include/ListView/ListViewSmarty.php` — affichage des résultats
- `sugar_cached('modules/unified_search_modules.php')` — fichier cache
- `custom/modules/unified_search_modules_display.php` — préférences d'affichage
- `VardefManager` — chargement des vardefs pour le cache
- `ACLController::checkAccess()` — contrôle des droits

## Exports / Symboles principaux
- `UnifiedSearchAdvanced` (classe, dépréciée depuis v7.12.0)
  - `getDropDownDiv()` — renvoie le HTML du menu déroulant de sélection des modules
  - `search()` — exécute la recherche et affiche les résultats
  - `buildCache()` — construit le fichier cache des modules searchables
  - `retrieveEnabledAndDisabledModules()` — liste les modules activés/désactivés
  - `saveGlobalSearchSettings()` — sauvegarde les modules sélectionnés par l'admin
  - `getUnifiedSearchModules()` — lit le cache des modules
  - `getUnifiedSearchModulesDisplay()` — lit les préférences d'affichage
- `unified_search_modules_cmp()` (fonction globale, dépréciée) — comparateur pour tri

## Interactions
- **Appelé par :** `modules/Home/Search.php` (qui remplace cette classe depuis v7.12.0), vues de recherche globale
- **Appelle :** `SearchForm`, `ListViewSmarty`, `VardefManager`, `ACLController`

## Notes
- Toute la classe est marquée `@deprecated since v7.12.0` — utiliser `Search.php` à la place.
- `buildCache()` parcourt tous les beans du CRM pour construire la liste des champs searchables.
- `getUnifiedSearchModulesDisplay()` écrit dans `custom/modules/unified_search_modules_display.php` si le fichier n'existe pas.
