# UnifiedSearch.php

**Chemin :** `modules/Home/UnifiedSearch.php`
**Type :** PHP - Script
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Alias/proxy vers `Search.php`. Inclut simplement `modules/Home/Search.php` pour déclencher la recherche unifiée.

## Type
script (délégation)

## Dépendances clés
- `modules/Home/Search.php`

## Exports / Symboles principaux
Aucun (délégation pure).

## Interactions
- **Appelé par :** requêtes URL `?module=Home&action=UnifiedSearch`
- **Appelle :** `Search.php`

## Notes
- Fichier trivial d'une ligne utile (require_once).
