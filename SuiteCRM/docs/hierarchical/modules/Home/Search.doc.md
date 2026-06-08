# Search.php

**Chemin :** `modules/Home/Search.php`
**Type :** PHP - Script de recherche
**Dernière mise à jour doc :** 2026-05-31

---

## Rôle
Point d'entrée pour la recherche unifiée SuiteCRM. Construit une `SearchQuery` depuis la requête GET, délègue l'exécution et l'affichage à `SearchWrapper`, et gère les exceptions/erreurs via `SearchThrowableHandler`.

## Type
controller / script

## Dépendances clés
- `SuiteCRM\Search\SearchQuery` — représente la requête de recherche
- `SuiteCRM\Search\SearchWrapper` — orchestre la recherche et l'affichage
- `SuiteCRM\Search\UI\SearchThrowableHandler` — gestion des erreurs d'affichage

## Exports / Symboles principaux
- `handleThrowable(Throwable, SearchQuery)` — fonction globale de gestion d'erreur

## Interactions
- **Appelé par :** `modules/Home/UnifiedSearch.php` (qui inclut ce fichier), requêtes GET de recherche
- **Appelle :** `SearchWrapper::searchAndDisplay()`, `SearchThrowableHandler::handle()`

## Notes
- La double capture `Exception` + `Throwable` assure la compatibilité PHP 5.x/7+.
