# repairUniSearch.php

**Chemin :** `modules/Administration/repairUniSearch.php`
**Type :** PHP (action / maintenance)
**Derniere mise a jour doc :** 2026-05-31

---

## Role fonctionnel
Supprime le cache du module de recherche unifiee (`cache/modules/unified_search_modules.php`). Realisera la reconstruction du fichier au prochain acces.

## Role technique
Calcule le chemin du fichier cache via `sugar_cached()` et le supprime avec `unlink()` s'il existe.

---

## Interactions
- **Appele par :** Action d'administration (INCONNU - URL exacte)
- **Equivalent fonctionnel :** `RepairAndClear::clearSearchCache()`
