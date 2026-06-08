# quicksearchQuery.php

**Chemin :** `modules/Home/quicksearchQuery.php`
**Type :** PHP - Helper (action AJAX)
**Dernière mise à jour doc :** 2026-06-02

---

## Rôle
Point d'entrée AJAX pour les requêtes de recherche rapide (quicksearch) dans les champs relate du CRM. Charge la classe `quicksearchQuery` (ou son override custom), décode la requête JSON, et appelle la méthode appropriée (par défaut `query`).

## Type
helper

## Dépendances clés
- `modules/Home/QuickSearch.php` — classe `quicksearchQuery`
- `getJSONobj()` — utilitaire JSON global
- `securexss()` — nettoyage XSS
- `$_REQUEST['data']` (JSON encodé), `$_REQUEST['query']`

## Exports / Symboles principaux
Aucune classe ni fonction exportée. Script procédural.

## Interactions
- **Appelé par :** requêtes AJAX JavaScript des champs relate (autocomplete) dans toute l'application
- **Appelle :** `quicksearchQuery::query()` (ou méthode spécifiée dans `data['method']`)

## Notes
- Supporte un override custom via `custom/modules/Home/QuickSearch.php`.
- La méthode à appeler est dynamique (`$data['method']`) — vérification via `method_exists()` avant appel.
- Les valeurs `field_list` sont nettoyées avec `securexss()`.
